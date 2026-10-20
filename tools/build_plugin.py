#!/usr/bin/env python3
"""Copy the shared sources into each department skill and check every assets/ reference.

The sources live once at the repository root (data/procedures, docs, guides, templates,
dashboard). After install, a skill can only read files inside its own folder, so this
script copies each shared file into plugin/skills/<dept>/assets/ and then checks that
every `assets/...` path a skill mentions exists inside that skill.

Usage: python3 tools/build_plugin.py [--check] [--zip]
  --check  only check references, copy nothing
  --zip    also build dist/mh-shaheen-<version>.zip and dist/SHA256SUMS.txt
"""
import pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS = ROOT / "plugin" / "skills"

# (source, destination inside a department skill, departments)
COPIES = [
    ("data/procedures", "assets/procedures", ["for-formation"]),
    ("docs/procedure-tags.md", "assets/docs/procedure-tags.md", ["for-formation"]),
    ("docs/procedure-guard.md", "assets/docs/procedure-guard.md", ["for-formation"]),
    ("templates/procedure.schema.yaml", "assets/docs/procedure.schema.yaml", ["for-formation"]),
    ("templates/shirkati", "assets/shirkati", ["ceo-office"]),
    ("templates/org.schema.json", "assets/org.schema.json", ["ceo-office"]),
    ("dashboard/template.html", "assets/dashboard/template.html", ["ceo-office"]),
    ("dashboard/fonts", "assets/dashboard/fonts", ["ceo-office"]),
    ("guides/whatsapp.md", "assets/guides/whatsapp.md", ["cs-customer-service", "mkt-marketing"]),
    ("guides/instagram.md", "assets/guides/instagram.md", ["cs-customer-service"]),
    ("guides/calls.md", "assets/guides/calls.md", ["cs-customer-service"]),
    ("guides/sales-systems.md", "assets/guides/sales-systems.md", ["sal-sales"]),
]

# (source, destination inside plugin/) for files that ship with the whole plugin
PLUGIN_COPIES = [("LICENSE", "LICENSE.txt"), ("NOTICE", "NOTICE.txt")]

# release whitelist (G3 F1): anything else stops the build
ALLOWED_EXT = {".md", ".json", ".yaml", ".html", ".ttf", ".txt"}

REF = re.compile(r"assets/[A-Za-z0-9_./-]+[A-Za-z0-9_]")


def copy_all():
    for src, dst, depts in COPIES:
        s = ROOT / src
        if not s.exists():
            sys.exit(f"missing source: {src}")
        if s.is_symlink():
            sys.exit(f"symlink source not allowed: {src}")
        for d in depts:
            t = SKILLS / d / dst
            if t.exists():
                shutil.rmtree(t) if t.is_dir() else t.unlink()
            t.parent.mkdir(parents=True, exist_ok=True)
            if s.is_dir():
                for q in s.rglob("*"):
                    if q.is_symlink():
                        sys.exit(f"symlink in source: {q.relative_to(ROOT)}")
                shutil.copytree(s, t, ignore=shutil.ignore_patterns(".*", "__pycache__"))
            else:
                shutil.copy2(s, t)
            print(f"copied {src} -> {d}/{dst}")
    for src, dst in PLUGIN_COPIES:
        if (ROOT / src).is_symlink():
            sys.exit(f"symlink source not allowed: {src}")
        shutil.copy2(ROOT / src, ROOT / "plugin" / dst)
        print(f"copied {src} -> plugin/{dst}")


def check_refs():
    missing = 0
    for dept in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        for md in dept.rglob("*.md"):
            if "assets" in md.relative_to(dept).parts:
                continue
            for ref in sorted(set(REF.findall(md.read_text(encoding="utf-8")))):
                if not (dept / ref).exists():
                    print(f"MISSING {md.relative_to(SKILLS)}: {ref}")
                    missing += 1
    for md in SKILLS.rglob("*.md"):
        if "for-formation" in md.parts or "assets" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        for bad in ("`procedures/", "docs/procedure-"):
            if bad in text:
                print(f"OUTSIDE-FOR {md.relative_to(SKILLS)}: {bad}")
                missing += 1
    print(f"TOTAL MISSING {missing}")
    return missing


def check_template_pin():
    """G8: CSP hashes = the template's inline blocks · CEO-06 pins the same CSP line and fingerprint"""
    import base64, hashlib
    tpl = (ROOT / "dashboard/template.html").read_bytes().decode("utf-8")
    pb = (SKILLS / "ceo-office/playbooks/ceo-06-dashboard.md").read_bytes().decode("utf-8")
    bad = 0
    csp = [l for l in tpl.split("\n") if "Content-Security-Policy" in l]
    if len(csp) != 1:
        print(f"PIN template has {len(csp)} CSP lines, expected 1")
        return 1
    csp = csp[0].strip()
    want = set(re.findall(r"'sha256-([A-Za-z0-9+/=]+)'", csp))
    got = set()
    for m in re.finditer(r"<(script|style)\b([^>]*)>(.*?)</\1>", tpl, re.S):
        if 'type="application/json"' in m.group(2):
            continue
        got.add(base64.b64encode(hashlib.sha256(m.group(3).encode("utf-8")).digest()).decode())
    if want != got:
        print(f"PIN CSP {sorted(want)} != inline blocks {sorted(got)}")
        bad += 1
    if csp not in [l.strip() for l in pb.split("\n")]:
        print("PIN CEO-06 CSP line differs from the template")
        bad += 1
    t = tpl.replace("\r\n", "\n")
    t = re.sub(r'(<script type="application/json" id="data">).*?(</script>)', r"\1@@DATA@@\2", t, count=1, flags=re.S)
    fp = hashlib.sha256(t.encode("utf-8")).hexdigest()
    if f"`{fp}`" not in pb:
        print(f"PIN CEO-06 fingerprint is not {fp}")
        bad += 1
    print(f"TEMPLATE PIN {'OK' if not bad else 'FAIL'} · {fp}")
    return bad


def release_files():
    files = []
    for p in sorted((ROOT / "plugin").rglob("*")):
        rel = p.relative_to(ROOT)
        if p.is_symlink():
            sys.exit(f"symlink not allowed: {rel}")
        if p.is_dir() or p.name == ".DS_Store":
            continue
        if any(x.startswith(".") and x != ".claude-plugin" for x in rel.parts):
            sys.exit(f"hidden path not allowed: {rel}")
        if p.suffix.lower() not in ALLOWED_EXT:
            sys.exit(f"unexpected file type: {rel}")
        files.append(p)
    return files


def build_zip():
    """dist/mh-shaheen-<version>.zip with plugin/ at its root, plus SHA256SUMS.txt"""
    import hashlib, json, zipfile
    version = json.loads((ROOT / "plugin/.claude-plugin/plugin.json").read_text())["version"]
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())["plugins"][0]["version"]
    if version != market:
        sys.exit(f"version mismatch: plugin.json {version} vs marketplace.json {market}")
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / f"mh-shaheen-{version}.zip"
    files = release_files()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            info = zipfile.ZipInfo(p.relative_to(ROOT).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes(), compresslevel=9)
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    (dist / "SHA256SUMS.txt").write_text(f"{digest}  {out.name}\n")
    print(f"zip {out.relative_to(ROOT)} · {len(files)} files · sha256 {digest}")


if __name__ == "__main__":
    if "--check" in sys.argv and "--zip" in sys.argv:
        sys.exit("--zip always copies first, drop --check")
    if "--check" not in sys.argv:
        copy_all()
    missing = check_refs() + check_template_pin()
    if missing:
        sys.exit(1)
    if "--zip" in sys.argv:
        build_zip()
