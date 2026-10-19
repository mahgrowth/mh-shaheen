---
name: xxx-english-dept-slug
description: "What this department covers and the founder requests that should route here; use when the user types the English and Arabic trigger words of any playbook inside it; max 1024 characters, between double quotes, no angle brackets, no inner double quotes and no period anywhere, parts joined with a semicolon · سطر عربي يوصف الإدارة"
license: CC-BY-NC-SA-4.0
metadata:
  dept: "xxx"
  version: "0.1.0"
  default_state: "dormant"
  playbooks: "XXX-01 XXX-02 XXX-03"
---

<!--
قالب ملف الإدارة (SKILL.md) · الإصدار 0.1.1 · 18/10/2026 (الـdescription بين "" وبدون نقاط)
القرار الهندسي بالمواصفة §3.1: كل إدارة = SKILL.md واحد + مجلد playbooks/ فيه مهاراتها
- هالملف هو اللي يختاره Claude · الـplaybooks يقراها بس لما يحتاجها (Progressive disclosure)
- name لازم يطابق اسم مجلد الإدارة بالضبط (شرط مواصفة Agent Skills)
- خلّه تحت 200 سطر · التفاصيل كلها بالـplaybooks
- كل playbook مكتوب بقالب SKILL-TEMPLATE.md وfrontmatter صالح لحاله، عشان لو تجربة Cowork بـP1 طلّعت إن مهارة لكل ملف أفضل، ننقل الملفات بدون إعادة كتابة
-->

# إدارة <الاسم بالعربي> (XXX)

## قبل أي شي
1. اقرا `COMPANY.md` و`org.json`
2. لو حالة `xxx` بـ`org.json` «خامل» أو «موقوف»: لا تشتغل · رجّع للـCEO (CEO-02) الطلب بسطر وليش يحتاج هالإدارة
3. لو الإدارة «فعّال»: شوف جدول الـplaybooks تحت واقرا الملف المناسب بس

## الـplaybooks

| الكود | المهارة | متى تقراه | الملف |
|---|---|---|---|
| XXX-01 | | | `playbooks/xxx-01-slug.md` |

**لو الطلب ما يطابق أي playbook:** لا ترتجل مهارة جديدة · رجّعه للـCEO (CEO-02) يوجهه

## قواعد الإدارة الثابتة
- البوابة: أي إجراء برا يوقف ويتسلّم لـCEO-04 (النص الكامل بأي playbook، قسم «بوابة الموافقات»)
- أي معلومة حكومية من قاعدة الإجراءات عن طريق FOR-10 بس
- <!-- قاعدة خاصة بالإدارة، مثل: كل مخرج يبدأ بـ«⚠️ مسودة، راجعها مع مختص» (LEG وFIN) -->

---
| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1.0 | YYYY-MM-DD | إنشاء |
