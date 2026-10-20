---
id: AE-FOR-MOHRE-EST-CARD
schema_version: "0.3.2"
country: AE
emirate: FED
jurisdiction: mainland
title_ar: "فتح ملف المنشأة (بطاقة المنشأة) لدى وزارة الموارد البشرية والتوطين"
service_ar: "Issuance of Establishment Card"
authority_ar: "وزارة الموارد البشرية والتوطين"
legal_form: ["كل الأشكال القانونية"]
step_order: 8
official_url: "https://www.mohre.gov.ae/en/services/issuance-of-establishment-card-2022"
portal_url: null
applies_to: [dubai_mainland, abu_dhabi_mainland, has_employees, topic_employment]
fields:
  fee:
    amount: null
    currency: AED
    note_ar: "الرسوم ما انقرت من المصدر: الصفحة انقرت 20/10/2026 بس بنودها ما تركب على مبلغ واحد · البنود حرفياً: «Business centers charge a maximum commission of AED72» · «Ta’qeem fees: 406 dirhams» · «The service is provided free of charge through MOHRE website and App. (only government fees are applicable)» · «Please note that the fees shown above do not include tax and collection charges» · الصفحة ما توضح هل رسوم Ta’qeem تنطبق على كل طلب بطاقة منشأة (شروط الخدمة ما تطلب تقرير Ta’qeem)، فما تركب على رقم ولا نطاق ولا «متغيرة» بالصيغة · نفس حالة AE-FOR-ICP-EST-CARD (قائمة بنود) · source_quote باقي null لين يتقرر شكل «قائمة البنود» بالصيغة، مو لأن الصفحة ما انقرت"
    source_url: "https://www.mohre.gov.ae/en/services/issuance-of-establishment-card-2022"
    source_quote: null
  duration:
    text_ar: "2 working days"
    days: 2
  documents:
    - "A valid trade license"
    - "الصفحة ما تعدد مستندات ثانية: خطوة التقديم تقول «attach the required documents» بدون قائمة"
  conditions:
    - "A valid trade license"
    - "It is mandatory for owners, partners, service agents, and authorized signatories to obtain a Ministry-issued personal identification number"
    - "A licensee or a service agent shall be at least 18 years of age"
    - "The authorized signatory in the Ministry must also be authorized to sign in the Federal Authority for Identity, Nationality, Customs and Port Security"
    - "Citizens of the GCC are treated as UAE nationals"
    - "خبر الوزارة 09/02/2026 (انقرا 20/10/2026): بطاقة المنشأة «now being processed automatically upon submission of the request to the Departments of Economic Development» · «meaning zero customer visits are required»"
legal_refs: []
status: likely
source_quality: official
last_verified: "2026-10-20"
verified_by: "فريق الحزمة"
verification_method: human
max_age_days: 90
change_log:
  - date: "2026-10-17"
    change: "إنشاء · موقع الوزارة رفض الاتصال من أداة القراءة · القيم من نص الصفحات بالفهرس · الحالة likely لين تنقرا الصفحة"
    by: "فريق الحزمة"
  - date: "2026-10-18"
    change: "توحيد الوسوم حسب docs/procedure-tags.md 0.1.0: plans_to_hire ← has_employees · وسم البحث topic_employment انضاف · ولا معلومة ثانية تغيرت"
    by: "فريق الحزمة"
  - date: "2026-10-20"
    change: "قراءة مباشرة لصفحة الخدمة وخبر الوزارة 09/02/2026 (عبر أداة قراءة وسيطة r.jina.ai لأن الموقع يرفض الاتصال المباشر من أداة القراءة) · المدة والشروط والمستندات صارت بحرف الصفحة · انشالت مستندات الفهرس (نسخة الهوية، عقد الإيجار) لأن الصفحة الحالية ما تذكرها · الرسوم انقرت بس ما تركب على حالة بالصيغة (قائمة بنود، تطبيقها مو واضح) ← source_quote من \"\" (كان غلط: يعني المصدر ما يذكر رسوم) إلى null · الحالة باقية likely لين قرار شكل «قائمة البنود» بالصيغة · schema_version من 0.1.0 إلى 0.3.2"
    by: "فريق الحزمة"
notes_ar: "lang:en (service_ar والاقتباسات بلغة الصفحة) · الصفحة منشورة 2025-04-11 حسب بياناتها · خبر الوزارة 09/02/2026 (انقرا مباشرة 20/10/2026): خدمة «Issuance of Establishment Card» صارت تنعالج آلياً أول ما يوصل الطلب لدوائر التنمية الاقتصادية بدون أي زيارة، ونفس الشي لتحديث ملف المنشأة · صفحة الخدمة (منشورة قبل الخبر) للحين تعرض خطوات التقديم اليدوي والدفع، فالحزمة تعرض الاثنين · سبب بقاء likely: الرسوم بس (قائمة بنود)، وباقي الحقول انقرت حرفياً 20/10/2026 · رابط الخبر: https://www.mohre.gov.ae/en/media-center/news/9/2/2026/mohre-launches-range-of-services-eliminating-most-required-documents-in-person-visits-and"
---

# بطاقة المنشأة لدى وزارة الموارد البشرية والتوطين · الإمارات (اتحادي)

> **[مرجح]** صفحة الوزارة انقرت، بس أي بند رسوم ينطبق عليك مو واضح فيها · آخر تحقق 20/10/2026

- تحتاجها قبل ما توظّف أو تطلب تصاريح عمل
- حسب خبر الوزارة 2026 الطلب ينعالج آلياً لما يوصل لدائرة التنمية الاقتصادية، بدون زيارة
- الرسوم: الصفحة تذكر رسوم Ta’qeem 406 درهم، وإن الخدمة مجانية بموقع الوزارة وتطبيقها (رسوم حكومية بس)، وعمولة مراكز الخدمة 72 درهم حد أعلى، والمبالغ بدون الضريبة ورسوم التحصيل · تأكد من المبلغ النهائي قبل الدفع
