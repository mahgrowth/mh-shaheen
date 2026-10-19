---
id: AE-FOR-CT-REG
schema_version: "0.2.0"
country: AE
emirate: FED
jurisdiction: mainland
title_ar: "التسجيل في ضريبة الشركات"
service_ar: "Corporate Tax Registration"
authority_ar: "الهيئة الاتحادية للضرائب · منصة EmaraTax"
legal_form: ["كل الأشكال القانونية"]
step_order: 11
official_url: "https://tax.gov.ae/en/services/corporate.tax.registration.aspx"
portal_url: null
applies_to: [dubai_mainland, abu_dhabi_mainland, juridical_person, natural_person_revenue_over_1m, topic_tax]
fields:
  fee:
    amount: 0
    currency: AED
    note_ar: "الخدمة بدون رسوم"
    source_url: "https://tax.gov.ae/en/services/corporate.tax.registration.aspx"
    source_quote: "Free of charge"
  duration:
    text_ar: "20 business days from the date the completed application was received"
    days: 20
  documents:
    - "مستندات التأسيس أو عقد الشراكة"
    - "شهادة السجل التجاري"
    - "رخصة تجارية سارية مع رخص الفروع إن وجدت"
    - "الهوية الإماراتية والجواز للملاك اللي يملكون أكثر من 25% وللمفوضين بالتوقيع"
    - "ما يثبت صلاحية المفوّض بالتوقيع"
  conditions:
    - "All juridical persons subject to Corporate Tax are required to register with the Federal Tax Authority"
    - "A natural person is required to register if the total revenue generated from conducting business exceeds AED 1 million within a calendar year"
    - "Yes, an administrative penalty of AED 10,000 is imposed for late registration for Corporate Tax"
    - "FTA services are only available through UAEPass!"
legal_refs:
  - "Federal Tax Authority Decision No. (3) of 2024"
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
    change: "تغيير الرمز من AE-FIN-CT-REG إلى AE-FOR-CT-REG حسب الصيغة 0.2.0 (كل السجلات بكود FOR) · بدون تغيير بالمحتوى"
    by: "فريق الحزمة"
  - date: "2026-10-18"
    change: "توحيد الوسوم حسب docs/procedure-tags.md 0.1.0: وسم البحث topic_tax انضاف · ولا معلومة ثانية تغيرت"
    by: "فريق الحزمة"
notes_ar: "lang:en (service_ar والاقتباسات بلغة الصفحة) · المستندات ملخصة من الصفحة مو منقولة حرفياً، والملفات PDF بحد أقصى 15 ميغا للملف · إيراد الشخص الطبيعي ما يشمل الراتب ودخل الاستثمار الخاص والاستثمار العقاري · مبادرة الإعفاء من غرامة التأخير: تنشال الغرامة لو انقدم أول إقرار ضريبي خلال 7 شهور من نهاية أول فترة ضريبية · فروع الشركة المحلية داخل الدولة تتبع الشركة الأم وما تسجّل لحالها · نسبة الضريبة مو بهالصفحة"
---

# التسجيل في ضريبة الشركات · الإمارات (اتحادي)

> **[مؤكد]** من صفحة الخدمة الرسمية للهيئة الاتحادية للضرائب · آخر تحقق 17/10/2026

- الشخص الاعتباري لازم يسجّل، والشخص الطبيعي لو إيراد نشاطه تعدى مليون درهم بالسنة الميلادية (المصدر: الهيئة الاتحادية للضرائب · 17/10/2026)
- غرامة التسجيل المتأخر 10,000 درهم، وفيه مبادرة إعفاء بشروط
- بدون رسوم، والمعالجة 20 يوم عمل
