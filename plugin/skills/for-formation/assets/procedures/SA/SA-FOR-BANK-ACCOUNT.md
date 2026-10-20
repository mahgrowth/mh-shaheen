---
id: SA-FOR-BANK-ACCOUNT
schema_version: "0.3.2"
country: SA
emirate: null
jurisdiction: mainland
title_ar: "حساب بنكي باسم المنشأة لدى جهات التمويل والبنوك"
service_ar: "15. Time Period for Opening the Bank Accounts"
authority_ar: "البنوك المرخصة · القواعد من البنك المركزي السعودي (ساما)"
legal_form: ["مؤسسة فردية", "شركة ذات مسؤولية محدودة"]
step_order: 7
official_url: "https://rulebook.sama.gov.sa/en/15-time-period-opening-bank-accounts"
portal_url: null
applies_to: [license_holder, topic_payments]
fields:
  fee:
    amount: null
    currency: SAR
    note_ar: "قواعد ساما ما تذكر رسوم فتح · الرسوم والشروط التجارية حسب البنك"
    source_url: "https://rulebook.sama.gov.sa/en/15-time-period-opening-bank-accounts"
    source_quote: ""
  duration:
    text_ar: "within one business day if they meet all bank requirements · and within two business days for those who need approvals"
    days: 1
  documents:
    - "المؤسسة الفردية والمحل (القاعدة 300.1.1 Licensed Businesses and Shops): «Obtaining a copy of the entity's commercial register, or license if it is the only item required»"
    - "«Verifying the identity of the owner of the entity against his/her name in the commercial register or license» (300.1.1)"
    - "«Obtaining copies of the IDs of individuals authorized to mange and operate the accounts» (300.1.1، الخطأ الإملائي من الأصل)"
    - "الشركة المقيمة (القاعدة 300.1.3 Resident Companies): «A copy of the commercial register shall be obtained»"
    - "«Obtaining a copy of the memorandum of association or the articles of association and their annexes» (300.1.3)"
    - "«Obtaining a copy of the ID of the manager in charge» (300.1.3)"
    - "«Verifying the identity of board members» (300.1.3)"
    - "«Obtaining copies of the IDs of individuals authorized to sign for and operate the accounts» (300.1.3)"
    - "وكالة من كاتب عدل أو موثق، أو تفويض مسجل لدى البنك حسب القاعدة، «authorizing natural persons to sign for and operate the accounts» (300.1.3)"
  conditions:
    - "«The applicant must be informed in writing of any missing or additional requirements upon application» (القاعدة 15)"
    - "اتفاقية الحساب للشخص الاعتباري فيها بيانات مجلس الإدارة والمديرين والمفوضين بالتوقيع، والتحقق من هيكل الملكية للوصول للمستفيد الحقيقي (القاعدة 2 · https://rulebook.sama.gov.sa/en/2-documents-required-open-bank-account-are-follows)"
    - "حساب بنكي تجاري مربوط بالمتجر شرط لتوثيق المتجر الإلكتروني (SA-FOR-ECOM-AUTH)، وحساب للمنشأة شرط لحماية الأجور (SA-FOR-WPS)"
legal_refs:
  - "قواعد الحسابات البنكية · البنك المركزي السعودي · رقم 65681/67 وتاريخ 1/11/1440هـ (3/7/2019)، الحالة: In-Force (كما ورد بصفحة القاعدة)"
status: confirmed
source_quality: official
last_verified: "2026-10-20"
verified_by: "فريق الحزمة"
verification_method: human
max_age_days: 90
change_log:
  - date: "2026-10-18"
    change: "إنشاء · قاعدة مدة الفتح والقاعدة 2 انقرت مباشرة من كتيب قواعد ساما · قائمة المستندات من نص الفهرس للقواعد · الحالة likely لين تنقرا قاعدة المستندات مباشرة"
    by: "فريق الحزمة"
  - date: "2026-10-20"
    change: "قراءة مباشرة لقاعدتي المستندات 300.1.1 (Licensed Businesses and Shops) و300.1.3 (Resident Companies) وإعادة قراءة القاعدتين 2 و15 من كتيب قواعد ساما (الحالة In-Force، القرار 65681/67 بتاريخ 1/11/1440هـ) · المستندات صارت بحرف القواعد بدل نص الفهرس · likely ← confirmed · schema_version من 0.2.1 إلى 0.3.2"
    by: "فريق الحزمة"
notes_ar: "lang:en (service_ar والاقتباسات بلغة الصفحة) · روابط قواعد المستندات: https://rulebook.sama.gov.sa/en/30011-licensed-businesses-and-shops و https://rulebook.sama.gov.sa/en/30013-resident-companies · القاعدة 300.1.1 ما تستخدم كلمة «مؤسسة فردية»، عنوانها «الأنشطة والمحلات المرخصة» · فيه قواعد للفتح عن بعد للمؤسسات الفردية (القاعدة 4) والشركات المقيمة (القاعدة 5) · تعديل 2025 لمواءمة القواعد مع نظام السجل التجاري الجديد: البنك يجمّد الحساب لو السجل تعلّق أو انشطب (نص الفهرس، مو من القراءة المباشرة) [للتحقق] · الحزمة ما ترشح بنك، وقارن الرسوم والخدمات بنفسك · الصياغة بالحزمة لجهات التمويل والبنوك كلها"
---

# حساب بنكي باسم المنشأة · السعودية

> **[مؤكد]** من كتيب قواعد البنك المركزي السعودي (ساما) · آخر تحقق 20/10/2026

**ليش تحتاجه**
- توثيق المتجر الإلكتروني وحماية الأجور يطلبون حساب باسم المنشأة

**شنو تسوي**
- افتح الحساب عند البنك اللي تختاره بالسجل التجاري وهويتك، وعقد التأسيس لو شركة
- البنك يفتحه خلال يوم عمل لو اكتملت متطلباته، ويومين لو يحتاج موافقات، ولازم يبلغك كتابياً بأي نقص (المصدر: قواعد ساما · 20/10/2026)

**انتبه**
- الرسوم حسب البنك، والحزمة ما ترشح جهة
- لو تعلّق سجلك التجاري، البنك يجمّد الحساب
