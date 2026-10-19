---
id: AE-FOR-VAT-REG
schema_version: "0.2.0"
country: AE
emirate: FED
jurisdiction: mainland
title_ar: "التسجيل في ضريبة القيمة المضافة"
service_ar: "Value Added Tax (VAT) Registration"
authority_ar: "الهيئة الاتحادية للضرائب · منصة EmaraTax"
legal_form: ["كل الأشكال القانونية"]
step_order: 10
official_url: "https://tax.gov.ae/en/services/vat.registration.aspx"
portal_url: null
applies_to: [dubai_mainland, abu_dhabi_mainland, taxable_supplies_over_threshold, topic_tax]
fields:
  fee:
    amount: 0
    currency: AED
    note_ar: "الخدمة بدون رسوم"
    source_url: "https://tax.gov.ae/en/services/vat.registration.aspx"
    source_quote: "Free"
  duration:
    text_ar: "20 business days from the date the completed application was received"
    days: 20
  documents:
    - "Commercial registration certificate, or any official document issued by the licensing authority"
    - "A valid trade license, along with branch licenses (if any)"
    - "Emirates ID and passport copies of owners and authorized signatories"
    - "Official declaration letter stating the total taxable supplies and monthly sales"
  conditions:
    - "إلزامي لما: The total value of taxable supplies and imports exceeds AED 375,000 over the past 12 months (أو المتوقع خلال 30 يوم القادمة)"
    - "اختياري لما التوريدات أو الواردات أو المصروفات الخاضعة تتعدى AED 187,500 (the voluntary registration threshold)"
    - "الطلب ينقدم خلال 30 يوم من صيرورة التسجيل إلزامي، وإلا فيه غرامة تأخير (الصفحة ما تذكر مبلغها)"
    - "FTA services are only available through UAEPass!"
legal_refs: []
status: confirmed
source_quality: official
last_verified: "2026-10-17"
verified_by: "فريق الحزمة"
verification_method: human
max_age_days: 90
change_log:
  - date: "2026-10-17"
    change: "إنشاء من قراءة مباشرة للصفحة الرسمية (آخر تحديث للصفحة 19/08/2026)"
    by: "فريق الحزمة"
  - date: "2026-10-17"
    change: "تغيير الرمز من AE-FIN-VAT-REG إلى AE-FOR-VAT-REG حسب الصيغة 0.2.0 (كل السجلات بكود FOR) · بدون تغيير بالمحتوى"
    by: "فريق الحزمة"
  - date: "2026-10-18"
    change: "توحيد الوسوم حسب docs/procedure-tags.md 0.1.0: وسم البحث topic_tax انضاف · ولا معلومة ثانية تغيرت"
    by: "فريق الحزمة"
  - date: "2026-10-18"
    change: "صياغة حسب دليل الأسلوب §1: كلمة ممنوعة صارت «القادمة» بالشرط الأول · المعنى ما تغير"
    by: "فريق الحزمة"
notes_ar: "lang:en (service_ar والمستندات بلغة الصفحة) · الصفحة تقدّر وقت تعبئة الطلب بـ45 دقيقة · المستندات بالصفحة عامة للأشخاص الطبيعيين والاعتباريين، مو مفصلة حسب الشكل القانوني · نسبة الضريبة نفسها مو بهالصفحة"
---

# التسجيل في ضريبة القيمة المضافة · الإمارات (اتحادي)

> **[مؤكد]** من صفحة الخدمة الرسمية للهيئة الاتحادية للضرائب · آخر تحقق 17/10/2026

- إلزامي لو توريداتك ووارداتك الخاضعة تعدت 375,000 درهم خلال آخر 12 شهر (المصدر: الهيئة الاتحادية للضرائب · 17/10/2026)
- اختياري من 187,500 درهم
- بدون رسوم، والمعالجة 20 يوم عمل
