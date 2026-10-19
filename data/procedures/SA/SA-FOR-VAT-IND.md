---
id: SA-FOR-VAT-IND
schema_version: "0.3.0"
country: SA
emirate: null
jurisdiction: mainland
title_ar: "التسجيل في ضريبة القيمة المضافة (أفراد يمارسون نشاط)"
service_ar: "VAT Registration for Individuals"
authority_ar: "هيئة الزكاة والضريبة والجمارك"
legal_form: ["وثيقة عمل حر (بدون سجل تجاري)"]
step_order: 4
official_url: "https://zatca.gov.sa/en/eServices/Pages/eServices-002.aspx"
portal_url: "https://zatca.gov.sa"
applies_to: [freelancer, taxable_supplies_over_threshold, topic_tax]
fields:
  fee:
    amount: 0
    currency: SAR
    note_ar: "خانة تكلفة الخدمة فاضية، وقنوات الدفع مكتوب فيها «Free»"
    source_url: "https://zatca.gov.sa/en/eServices/Pages/eServices-002.aspx"
    source_quote: "Free"
  rate:
    percent: 15
    base_ar: "سعر البيع النهائي للسلعة أو الخدمة الخاضعة للنسبة الأساسية"
    on_price: true
    source_url: "https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/Guideline-for-Tax-Invoicing-and-Records-under-VAT-Provisions.pdf"
    source_quote: "يجب عليهم فرض ضريبة بنسبة 15%(على افتراض أن النسبة الأساسية تنطبق على تلك التوريدات) تُضاف إلى سعر البيع النهائي"
    note_ar: "الدليل الإرشادي للفواتير الضريبية وحفظ السجلات، النسخة الثالثة، مايو 2026، ص7 · الدليل موجّه «لجميع الأشخاص الطبيعيين والاعتباريين الذين يمارسون نشاطًا اقتصاديًا» (ص8)، فيشمل الفرد"
  duration:
    text_ar: "الصفحة فيها خانة المدة بدون قيمة"
    days: null
  documents:
    - "الصفحة تحيل لتبويب المستندات، ومحتواه ما ظهر بالقراءة"
  conditions:
    - "Individuals whose annual revenues exceed SAR 375,000"
    - "Registration is optional for those whose annual revenues exceed SAR 187,500 and less than SAR 375,000"
    - "الإلزام بنص الهيئة: «يعتبر التسجيل إلزاميًا على جميع الأشخاص الذين تتجاوز إيراداتهم السنوية حدًا معيناً للتسجيل»، والحد «375,000 ريال سعودي «حد التسجيل الإلزامي»» خلال اثنى عشر شهرًا (الدليل الإرشادي للفواتير الضريبية، مايو 2026، ص10 · https://zatca.gov.sa/ar/HelpCenter/guidelines/Documents/Guideline-for-Tax-Invoicing-and-Records-under-VAT-Provisions.pdf · 18/10/2026)"
    - "الفرد بنص الدليل: «يمكن ممارسة النشاط الاقتصادي من قبل الأشخاص الطبيعيين والاعتباريين على حد سواء» (نفس الدليل، ص9)"
    - "غرامة «عدم التسجيل لأغراض ضريبة القيمة المضافة خلال الفترة المحددة للتسجيل»: «(10,000) ريال سعودي» (نفس الدليل، ص41)"
legal_refs:
  - "نظام ضريبة القيمة المضافة الصادر بالمرسوم الملكي رقم (م/113) وتاريخ 2 ذي القعدة 1438هـ (كما ورد بالدليل الإرشادي، مايو 2026، ص7)"
status: confirmed
source_quality: official
last_verified: "2026-10-18"
verified_by: "فريق الحزمة"
verification_method: human
max_age_days: 90
change_log:
  - date: "2026-10-18"
    change: "إنشاء من قراءة مباشرة لصفحة الخدمة"
    by: "فريق الحزمة"
  - date: "2026-10-18"
    change: "تصحيح بعد التحقق الثاني: كلمة «إلزامي» بالجسم ما كان لها نص بالصفحة · انضاف نص الإلزام والنسبة من الدليل الإرشادي للفواتير الضريبية (النسخة الثالثة، مايو 2026، ص7 وص9 وص10 وص41) · النسبة 15% انتقلت لحقل rate · الصيغة 0.3.0"
    by: "فريق الحزمة"
notes_ar: "lang:en (service_ar والاقتباسين الأولين بلغة الصفحة) · الوصف بالصفحة: «This e-service is for individuals who are engaged in economic activity in the Kingdom» · بعد التسجيل يطلع رقم حساب ضريبي · المستندات المطلوبة ما ظهرت بالقراءة [للتحقق] · الدليل يقول فيه «قواعد خاصة» لتحديد إذا نشاط الشخص الطبيعي داخل نطاق الضريبة، فراجع وضعك مع محاسب"
---

# التسجيل في ضريبة القيمة المضافة للأفراد · السعودية

> **[مؤكد]** من صفحة الخدمة الرسمية ودليل الهيئة الإرشادي (مايو 2026) · آخر تحقق 18/10/2026

- لو تشتغل كفرد (مثلاً بوثيقة عمل حر) وإيراداتك السنوية فوق 375,000 ريال التسجيل إلزامي، وفوق 187,500 اختياري (المصدر: هيئة الزكاة والضريبة والجمارك · 18/10/2026)
- الرسوم: بدون رسوم (المصدر: صفحة الخدمة · 18/10/2026)
- النسبة الأساسية 15% وتنضاف على سعر البيع حيث تنطبق (المصدر: الدليل الإرشادي، مايو 2026 · 18/10/2026)
