# الإمارات · فهرس سجلات الإجراءات

- **النطاق (الإصدار 1):** البر الرئيسي لدبي + البر الرئيسي لأبوظبي + الإجراءات الاتحادية + دليل المناطق الحرة
- **المرجع:** `data/sources/AE.md` · الصيغة: `templates/procedure.schema.yaml` (0.3.2) · الوسوم: `docs/procedure-tags.md` (0.1.4)
- **المسارات:** `data/procedures/` بالمستودع = `assets/procedures/` بعد التركيب · `docs/` و`templates/procedure.schema.yaml` = `assets/docs/` بعد التركيب · كلها داخل إدارة التأسيس
- **الرسوم بالخريطة:** خطوة مكتوب جنبها «اختياري» أو «(كل سنة)» تنكتب بخريطة الأوراق بسطر لحالها برا المجموع (FOR-02 الخطوة 4)
- **الإفصاحات:** ما فيه سجل إفصاح (وسم `topic_disclosure`) بهالإصدار · فحص الإفصاحات (FOR-08) يقولها صريح ويعرض المراجع القانونية بس (§4)
- **الحالة:** 33 سجل (24 إجراء + 9 مرجعية) · confirmed 31 · likely 2 · to_verify 0 · آخر تحديث 2026-10-18
- **الأقسام (نفس الترقيم بالدول الثلاث):** §1 النطاقات الرسمية · §2 المسارات (للإمارات حسب الإمارة والجهة) · §3 كل السجلات · §4 السجلات المرجعية
- **التنبيه الثابت:** مسودة، راجعها مع مختص · مبنية على الصفحات الرسمية بتاريخ آخر تحقق المكتوب جنب كل خطوة · الإجراءات والرسوم تتغير، والمسؤولية القانونية على المؤسس

## قيم خاصة
| الحقل | القيمة | المعنى |
|---|---|---|
| `emirate` | `DXB` | إمارة دبي |
| `emirate` | `AUH` | إمارة أبوظبي |
| `emirate` | `FED` | إجراء اتحادي ينطبق على الإمارتين بهالإصدار |
| `jurisdiction` | `freezone:all` | دليل عام للمناطق الحرة، مو منطقة بعينها |
| `notes_ar` | يبدأ بـ`lang:en` | `service_ar` مكتوب بلغة الصفحة الرسمية (إنجليزي) عشان فحص هوية الصفحة |

## 1. النطاقات الرسمية (قائمة الحارس)
الحارس يفتح الرابط الرسمي (`official_url`) ويعرض رابط البوابة (`portal_url`) بس لو اسم الخادم من هالقائمة حسب عمود «النوع»: «حكومي» = النطاق نفسه أو أي نطاق فرعي تحته · «بالضبط» = النطاق نفسه بس، بدون أي نطاق فرعي حتى `www.` · ممنوع سطر لاحقة عامة (مثل `gov.ae` أو `ae` أو `abudhabi`) وممنوع منفذ · المرجع: `docs/procedure-guard.md` §4.2

| النطاق | النوع | ملاحظة |
|---|---|---|
| `dgov.tdra.gov.ae` | حكومي | |
| `growth.gov.ae` | حكومي | |
| `investindubai.gov.ae` | حكومي | |
| `dubaidet.gov.ae` | حكومي | |
| `dubailand.gov.ae` | حكومي | |
| `dlp.dubai.gov.ae` | حكومي | |
| `gdrfad.gov.ae` | حكومي | |
| `added.gov.ae` | حكومي | |
| `tax.gov.ae` | حكومي | |
| `mohre.gov.ae` | حكومي | |
| `icp.gov.ae` | حكومي | |
| `moet.gov.ae` | حكومي | |
| `dubai.ae` | حكومي | بوابة حكومة دبي الرسمية · السجلات تستخدم `www.dubai.ae` و`invest.dubai.ae` |
| `tamm.abudhabi` | حكومي | بوابة حكومة أبوظبي الرسمية · السجلات تستخدم `www.tamm.abudhabi` |
| `u.ae` | بالضبط | البوابة الرسمية لحكومة الإمارات |
| `uaepass.ae` | بالضبط | الهوية الرقمية |
| `mediaoffice.ae` | بالضبط | المكتب الإعلامي لحكومة دبي |
| `dubaichambers.com` | بالضبط | غرف دبي |
| `www.dubaichambers.com` | بالضبط | غرف دبي، نفس الموقع بـ`www.` (الرابط الرسمي بـAE-FOR-DXB-CHAMBER) |
| `connect.dubaichamber.com` | بالضبط | منصة DC Connect لغرف دبي، لرابط البوابة بس · المصدر: خبر المكتب الإعلامي لحكومة دبي «To access DC Connect, please visit: https://connect.dubaichamber.com» (mediaoffice.ae، 10/02/2026، اطلاع 18/10/2026) · `dubaichamber.com` نفسه (بالمفرد) مو على القائمة |
| `abudhabichamber.ae` | بالضبط | غرفة أبوظبي |
| `www.abudhabichamber.ae` | بالضبط | غرفة أبوظبي، نفس الموقع بـ`www.` (الرابط الرسمي بـAE-FOR-AUH-CHAMBER) |
| `khalifafund.ae` | بالضبط | موقع صندوق خليفة الرسمي · جديد 18/10 |
| `www.khalifafund.ae` | بالضبط | صندوق خليفة، نفس الموقع بـ`www.` (الرابط الرسمي بـAE-FOR-REF-AUH-KHALIFA) |

ملاحظة: دليل الوجيز من دائرة الاقتصاد والسياحة مستضاف على `dubaitourism.getbynder.com` · ينذكر كمصدر داعم بالسجلات، وما ينضاف لهالقائمة

## 2. المسارات حسب الإمارة والجهة

### 2.0 المسار الأساسي (شرط الإطلاق: كله confirmed من مصدر رسمي)

المسار الأساسي = الأشكال القانونية واختيار الجهة، وحجز الاسم، والعنوان (عقد الإيجار)، والترخيص وبدائله، والرسوم، والجهة والبوابة · نفس تعريف الكويت والسعودية · الخطوات من الأقسام 2.1 إلى 2.3

| الخطوة | السجل | الحالة | آخر تحقق |
|---|---|---|---|
| 1 · الدخول للبوابة | AE-FOR-UAEPASS | confirmed | 2026-10-17 |
| 2 · بر رئيسي ولا منطقة حرة | AE-FOR-FZ-CHOOSE | confirmed | 2026-10-17 |
| 2 · سلطة التسجيل (لو اخترت منطقة حرة) | AE-FOR-FZ-REGISTRARS | confirmed | 2026-10-17 |
| 3 · الأشكال القانونية وخطوات البر الرئيسي | AE-FOR-MAINLAND-STEPS | confirmed | 2026-10-17 |
| 4 · الاستعلام عن توفر الاسم | AE-FOR-NER-SEARCH | confirmed | 2026-10-17 |
| 5 · دبي: حجز الاسم والموافقة المبدئية | AE-FOR-DXB-NAME-IA | confirmed | 2026-10-18 |
| 6 · دبي: العنوان (تسجيل عقد الإيجار) | AE-FOR-DXB-EJARI | confirmed | 2026-10-17 |
| 7 · دبي: الرخصة | AE-FOR-DXB-LICENCE | confirmed | 2026-10-18 |
| 7 بديل · دبي: الرخصة الفورية | AE-FOR-DXB-INSTANT | confirmed | 2026-10-18 |
| 7 بديل · دبي: انطلاق | AE-FOR-DXB-INTELAQ | confirmed | 2026-10-18 |
| 7 بديل · دبي: تاجر | AE-FOR-DXB-ETRADER | confirmed | 2026-10-18 |
| 5 · أبوظبي: خطوات التأسيس والترخيص | AE-FOR-AUH-SETUP-STEPS | confirmed | 2026-10-17 |
| 6 · أبوظبي: العنوان (توثيق عقد الإيجار) | AE-FOR-AUH-TAWTHEEQ | confirmed | 2026-10-18 |
| 7 بديل · أبوظبي: تاجر أبوظبي | AE-FOR-AUH-TAJER | confirmed | 2026-10-18 |
| 7 بديل · أبوظبي: المستقل | AE-FOR-AUH-FREELANCER | confirmed | 2026-10-18 |

- **النتيجة:** 15 سجل · 15 confirmed · جزئين داخل سجلين مؤكدين للحين [مرجح] ومكتوبين كذا بالسجل: رسم الموافقة المبدئية 120 بـAE-FOR-DXB-NAME-IA (صفحتها انشالت، و620 للاسم مؤكد) · وشرط الجنسية بـAE-FOR-DXB-ETRADER (الصفحات الرسمية الحالية ما تذكره)
- **برا المسار الأساسي (بعد الترخيص):** عضوية الغرفة (AE-FOR-DXB-CHAMBER · AE-FOR-AUH-CHAMBER، confirmed) · بطاقات المنشأة (AE-FOR-DXB-GDRFA-EST-CARD confirmed · AE-FOR-MOHRE-EST-CARD likely · AE-FOR-ICP-EST-CARD likely) · الضرائب والتوظيف والعلامة (AE-FOR-VAT-REG · AE-FOR-CT-REG · AE-FOR-ILOE · AE-FOR-TM-REG، confirmed) · نفس معاملة الغرفة والضريبة والتوظيف بالسعودية
- **ملاحظة:** عضوية غرفة دبي (300) مذكورة مع رسوم الرخصة بصفحة خدمة إصدار الرخصة (سجل تاجر)، فالرقم مؤكد من صفحة الرخصة حتى لو سجل الغرفة برا المسار الأساسي
- **قرار مفتوح:** تعريف المسار الأساسي بالإمارات (وإن خطوة الدخول داخله مثل الكويت، مو برا مثل السعودية) اقتراح يحتاج اعتماد صاحب الشرط

### 2.1 قبل ما تختار: بر رئيسي ولا منطقة حرة
| الخطوة | السجل | الحالة |
|---|---|---|
| 1 | AE-FOR-UAEPASS | [مؤكد] |
| 2 | AE-FOR-FZ-CHOOSE | [مؤكد] |
| 3 | AE-FOR-FZ-REGISTRARS (لو اخترت منطقة حرة) | [مؤكد] |

### 2.2 دبي · بر رئيسي (الطريق العادي)
| الخطوة | السجل | الحالة |
|---|---|---|
| 1 | AE-FOR-UAEPASS | [مؤكد] |
| 2 | AE-FOR-MAINLAND-STEPS | [مؤكد] |
| 3 | AE-FOR-NER-SEARCH | [مؤكد] |
| 4 | AE-FOR-DXB-NAME-IA | [مؤكد] |
| 5 | AE-FOR-DXB-EJARI | [مؤكد] |
| 6 | AE-FOR-DXB-LICENCE | [مؤكد] |
| 7 | AE-FOR-DXB-CHAMBER (كل سنة) | [مؤكد] |
| 8 | AE-FOR-MOHRE-EST-CARD | [مرجح] |
| 9 | AE-FOR-DXB-GDRFA-EST-CARD | [مؤكد] |
| 10 | AE-FOR-VAT-REG | [مؤكد] |
| 11 | AE-FOR-CT-REG | [مؤكد] |
| 12 | AE-FOR-ILOE (لما توظّف) | [مؤكد] |
| 13 | AE-FOR-TM-REG (اختياري) | [مؤكد] |

**بدائل للخطوات 4 إلى 6**
| الشرط | السجل | الحالة |
|---|---|---|
| نشاط ما يحتاج موافقات خارجية | AE-FOR-DXB-INSTANT | [مؤكد] |
| مشروع منزلي لمواطن إماراتي أو خليجي مقيم بدبي | AE-FOR-DXB-INTELAQ (كل سنة) | [مؤكد] |
| بيع أونلاين من البيت بمؤسسة فردية | AE-FOR-DXB-ETRADER | [مؤكد] |

### 2.3 أبوظبي · بر رئيسي
| الخطوة | السجل | الحالة |
|---|---|---|
| 1 | AE-FOR-UAEPASS | [مؤكد] |
| 2 | AE-FOR-MAINLAND-STEPS | [مؤكد] |
| 3 | AE-FOR-AUH-SETUP-STEPS | [مؤكد] |
| 4 | AE-FOR-AUH-TAWTHEEQ | [مؤكد] |
| 5 | AE-FOR-AUH-CHAMBER | [مؤكد] |
| 6 | AE-FOR-ICP-EST-CARD | [مرجح] (الرسوم: أي بند ينطبق مو واضح) |
| 7 | AE-FOR-MOHRE-EST-CARD | [مرجح] |
| 8 | AE-FOR-VAT-REG | [مؤكد] |
| 9 | AE-FOR-CT-REG | [مؤكد] |
| 10 | AE-FOR-ILOE (لما توظّف) | [مؤكد] |
| 11 | AE-FOR-TM-REG (اختياري) | [مؤكد] |

**بدائل للخطوات 3 إلى 5 (بدون مقر)**
| الشرط | السجل | الحالة |
|---|---|---|
| أنشطة تجارية محددة لمواطن أو مقيم | AE-FOR-AUH-TAJER | [مؤكد] |
| نشاط مهني فردي عن بعد | AE-FOR-AUH-FREELANCER | [مؤكد] |

- `step_order` بكل سجل = مكانه بأول مسار يظهر فيه · الترتيب الكامل لكل مسار من هالجداول

## 3. كل السجلات
الحالة وتاريخ التحقق هني نسخة من السجل نفسه (`status` و`last_verified`)، ولو اختلفوا السجل يغلب · الرسوم من السجل عن طريق الحارس

| السجل | الإمارة | الجهة | الحالة | آخر تحقق |
|---|---|---|---|---|
| AE-FOR-UAEPASS | FED | الهوية الرقمية UAE PASS (هيئة تنظيم الاتصالات والحكومة الرقمية) | confirmed | 2026-10-17 |
| AE-FOR-FZ-CHOOSE | FED | البوابة الرسمية لحكومة الإمارات · سلطة كل منطقة حرة | confirmed | 2026-10-17 |
| AE-FOR-FZ-REGISTRARS | FED | وزارة الاقتصاد والسياحة | confirmed | 2026-10-17 |
| AE-FOR-MAINLAND-STEPS | FED | البوابة الرسمية لحكومة الإمارات · دوائر الاقتصاد بدبي وأبوظبي | confirmed | 2026-10-17 |
| AE-FOR-NER-SEARCH | FED | السجل الاقتصادي الوطني | confirmed | 2026-10-17 |
| AE-FOR-DXB-NAME-IA | DXB | دائرة الاقتصاد والسياحة بدبي | confirmed | 2026-10-18 |
| AE-FOR-DXB-EJARI | DXB | دائرة الأراضي والأملاك في دبي | confirmed | 2026-10-17 |
| AE-FOR-DXB-LICENCE | DXB | دائرة الاقتصاد والسياحة بدبي | confirmed | 2026-10-18 |
| AE-FOR-DXB-INSTANT | DXB | دائرة الاقتصاد والسياحة بدبي | confirmed | 2026-10-18 |
| AE-FOR-DXB-INTELAQ | DXB | دائرة الاقتصاد والسياحة بدبي | confirmed | 2026-10-18 |
| AE-FOR-DXB-ETRADER | DXB | دائرة الاقتصاد والسياحة بدبي | confirmed | 2026-10-18 |
| AE-FOR-DXB-CHAMBER | DXB | غرف دبي | confirmed | 2026-10-17 |
| AE-FOR-DXB-GDRFA-EST-CARD | DXB | الإدارة العامة للإقامة وشؤون الأجانب · دبي | confirmed | 2026-10-17 |
| AE-FOR-AUH-SETUP-STEPS | AUH | دائرة التنمية الاقتصادية · أبوظبي | confirmed | 2026-10-17 |
| AE-FOR-AUH-TAWTHEEQ | AUH | دائرة البلديات والنقل · أبوظبي | confirmed | 2026-10-18 |
| AE-FOR-AUH-TAJER | AUH | دائرة التنمية الاقتصادية · أبوظبي | confirmed | 2026-10-18 |
| AE-FOR-AUH-FREELANCER | AUH | دائرة التنمية الاقتصادية · أبوظبي | confirmed | 2026-10-18 |
| AE-FOR-AUH-CHAMBER | AUH | غرفة تجارة وصناعة أبوظبي | confirmed | 2026-10-17 |
| AE-FOR-ICP-EST-CARD | AUH | الهيئة الاتحادية للهوية والجنسية والجمارك وأمن المنافذ | likely | 2026-10-18 |
| AE-FOR-MOHRE-EST-CARD | FED | وزارة الموارد البشرية والتوطين | likely | 2026-10-17 |
| AE-FOR-VAT-REG | FED | الهيئة الاتحادية للضرائب | confirmed | 2026-10-17 |
| AE-FOR-CT-REG | FED | الهيئة الاتحادية للضرائب | confirmed | 2026-10-17 |
| AE-FOR-ILOE | FED | نظام التأمين ضد التعطل عن العمل | confirmed | 2026-10-17 |
| AE-FOR-TM-REG | FED | وزارة الاقتصاد والسياحة | confirmed | 2026-10-17 |
| AE-FOR-REF-PRIVACY | FED | مكتب الإمارات للبيانات | confirmed | 2026-10-18 |
| AE-FOR-REF-ECOMMERCE | FED | وزارة الاقتصاد والسياحة | confirmed | 2026-10-18 |
| AE-FOR-REF-CONSUMER | FED | وزارة الاقتصاد والسياحة | confirmed | 2026-10-18 |
| AE-FOR-REF-LABOUR | FED | وزارة الموارد البشرية والتوطين | confirmed | 2026-10-18 |
| AE-FOR-REF-COMPANIES | FED | وزارة الاقتصاد والسياحة | confirmed | 2026-10-18 |
| AE-FOR-REF-TRADEMARK | FED | وزارة الاقتصاد والسياحة | confirmed | 2026-10-18 |
| AE-FOR-REF-DXB-SME | DXB | حكومة دبي · Dubai SME | confirmed | 2026-10-18 |
| AE-FOR-REF-AUH-KHALIFA | AUH | صندوق خليفة لتطوير المشاريع | confirmed | 2026-10-18 |
| AE-FOR-REF-FOREIGN-OWNERSHIP | FED | البوابة الرسمية لحكومة الإمارات | confirmed | 2026-10-18 |

## 4. السجلات المرجعية (رابط + جملة + إحالة، بدون خطوات)
| السجل | الإمارة | الموضوع | الحالة |
|---|---|---|---|
| AE-FOR-REF-PRIVACY | FED | حماية البيانات الشخصية (مرسوم بقانون اتحادي 45 لسنة 2021) | [مؤكد] |
| AE-FOR-REF-ECOMMERCE | FED | التجارة عبر وسائل التقنية الحديثة (مرسوم بقانون اتحادي 14 لسنة 2023) | [مؤكد] |
| AE-FOR-REF-CONSUMER | FED | حماية المستهلك (قانون اتحادي 15 لسنة 2020 وتعديله 5 لسنة 2023) | [مؤكد] |
| AE-FOR-REF-LABOUR | FED | تنظيم علاقات العمل (مرسوم بقانون اتحادي 33 لسنة 2021 وتعديله 20 لسنة 2023) | [مؤكد] |
| AE-FOR-REF-COMPANIES | FED | الشركات التجارية (مرسوم بقانون اتحادي 32 لسنة 2021 وتعديله 20 لسنة 2025) | [مؤكد] |
| AE-FOR-REF-TRADEMARK | FED | العلامات التجارية (مرسوم بقانون اتحادي 36 لسنة 2021) | [مؤكد] |
| AE-FOR-REF-DXB-SME | DXB | برامج دعم المشاريع الصغيرة والمتوسطة بدبي | [مؤكد] |
| AE-FOR-REF-AUH-KHALIFA | AUH | صندوق خليفة لتطوير المشاريع | [مؤكد] |
| AE-FOR-REF-FOREIGN-OWNERSHIP | FED | تملك الأجنبي لشركات البر الرئيسي والأنشطة المستثناة (المرسوم بقانون اتحادي 26 لسنة 2020 و32 لسنة 2021) · وسم `foreign_owner` لـFOR-09 | [مؤكد] |

- بوابة التشريعات uaelegislation.gov.ae وموقع sme.ae رجعوا 403 يوم 18/10، فالسجلات على u.ae وmoet.gov.ae وdubai.ae وkhalifafund.ae · وsme.ae مو على قائمة النطاقات، فما ينحط كرابط بوابة لين ينضاف بمصدر رسمي

## الأكواد (مطابقة مع قائمة المصادر)
كل `id` بصيغة `<الدولة>-FOR-<اسم قصير>` (الصيغة 0.2.0: قاعدة الإجراءات ملك إدارة FOR حتى لو تقراها مهارة ضرائب أو عمالة)، فالأكواد المقترحة بقائمة المصادر تغيرت لهالصيغة
| قائمة المصادر | السجل |
|---|---|
| AE-ID-UAEPASS | AE-FOR-UAEPASS |
| AE-FOR-MAINLAND-STEPS | AE-FOR-MAINLAND-STEPS |
| AE-DXB-NAME-IA | AE-FOR-DXB-NAME-IA |
| AE-DXB-LICENCE | AE-FOR-DXB-LICENCE |
| AE-DXB-INSTANT | AE-FOR-DXB-INSTANT |
| AE-DXB-INTELAQ | AE-FOR-DXB-INTELAQ |
| AE-DXB-EJARI | AE-FOR-DXB-EJARI |
| AE-DXB-CHAMBER | AE-FOR-DXB-CHAMBER |
| AE-AUH-SETUP-STEPS | AE-FOR-AUH-SETUP-STEPS |
| AE-AUH-TAJER | AE-FOR-AUH-TAJER |
| AE-AUH-FREELANCER | AE-FOR-AUH-FREELANCER |
| AE-AUH-TAWTHEEQ | AE-FOR-AUH-TAWTHEEQ |
| AE-AUH-CHAMBER | AE-FOR-AUH-CHAMBER |
| AE-LAB-MOHRE-EST | AE-FOR-MOHRE-EST-CARD |
| AE-ICP-EST-CARD | AE-FOR-ICP-EST-CARD |
| AE-TAX-VAT-REG | AE-FOR-VAT-REG |
| AE-TAX-CT-REG | AE-FOR-CT-REG |
| AE-LAB-ILOE | AE-FOR-ILOE |
| AE-IP-TM-REG | AE-FOR-TM-REG |
| AE-REG-NER | AE-FOR-NER-SEARCH |
| AE-FZ-CHOOSE | AE-FOR-FZ-CHOOSE |
| AE-FZ-REGISTRARS | AE-FOR-FZ-REGISTRARS |
| (إضافة بعد P1) | AE-FOR-DXB-ETRADER |
| (إضافة بعد P1) | AE-FOR-DXB-GDRFA-EST-CARD |
| (إضافة بعد G2) | AE-FOR-REF-FOREIGN-OWNERSHIP |

## الحالة بالأرقام
- confirmed 31 من 33 (94%) · likely 2 (AE-FOR-MOHRE-EST-CARD · AE-FOR-ICP-EST-CARD: أي بند رسوم ينطبق مو واضح) · to_verify 0 · كلها من مصادر رسمية
- المسار الأساسي (§2.0): 15 من 15 confirmed، مع جزئين [مرجح] داخل سجلين (رسم الموافقة المبدئية بدبي، وشرط الجنسية لرخصة تاجر)
- دبي بر رئيسي (§2.2 مع بدائله): 15 من 16 confirmed (MOHRE-EST-CARD likely) · أبوظبي بر رئيسي (§2.3 مع بدائله): 11 من 13 confirmed (MOHRE-EST-CARD وICP-EST-CARD likely)

---
| الإصدار | التاريخ | التغيير |
|---|---|---|
| 0.1 | 2026-10-17 | إنشاء مع الدفعة 1 |
| 0.2 | 2026-10-17 | الدفعة 2 (12 سجل) · مسار أبوظبي الكامل · مسار المناطق الحرة · ما بعد الترخيص |
| 0.3 | 2026-10-17 | 3 رموز تغيرت لصيغة FOR حسب الصيغة 0.2.0: AE-FOR-VAT-REG · AE-FOR-CT-REG · AE-FOR-ILOE |
| 0.4 | 2026-10-17 | سجلين جداد بعد توسيع النطاق لـ24: AE-FOR-DXB-ETRADER · AE-FOR-DXB-GDRFA-EST-CARD |
| 0.5 | 2026-10-18 | 8 سجلات مرجعية (6 قوانين اتحادية + دعم المشاريع بدبي وأبوظبي) بالصيغة 0.2.1 · نطاق جديد khalifafund.ae |
| 0.6 | 2026-10-18 | المراجعة الأمنية G3: القائمة صارت جدول بعمود «النوع» (حكومي · بالضبط) وجملة القاعدة الموحدة مع الكويت والسعودية · الغرف والصندوق ومنصاتها «بالضبط» مع سطر `www.` لحاله للي تستخدمه السجلات · `connect.dubaichamber.com` لرابط البوابة بمصدره · AE-FOR-REF-DXB-SME بدون `portal_url` (نطاق موقع الجهة ما له مصدر رسمي على القائمة) |
| 0.7 | 2026-10-18 | اختبار G2: ترقيم الأقسام نفسه بالدول الثلاث (§1 النطاقات · §2 المسارات · §3 كل السجلات · §4 المرجعية) · قسم «كل السجلات» جديد · حالة 8 سجلات بالجداول صارت confirmed مثل السجلات نفسها (الاسم والموافقة · الرخصة · الفورية · انطلاق · تاجر · توثيق · تاجر أبوظبي · المستقل)، ونصوصها تحت تحدّثت · العدّادات: confirmed من 23 إلى 31 |
| 0.8 | 2026-10-18 | اختبار G2 (M03): سجل مرجعي جديد AE-FOR-REF-FOREIGN-OWNERSHIP بوسم `foreign_owner` من صفحة u.ae الرسمية، عشان FOR-09 يلقى شروط تملك الأجنبي بدون ما ينضاف الوسم لسجل الرخصة كشرط · المجموع 33 · عدّاد أبوظبي تصحّح بعد ما صار ICP-EST-CARD likely |
| 0.9 | 2026-10-18 | التحقق القانوني الثاني (الجولة 2): جدول «2.0 المسار الأساسي» صريح مثل الكويت والسعودية (15 سجل، كلها confirmed) وقائمة اللي برا المسار (الغرف وبطاقات المنشأة والضرائب والتوظيف) · تصحيحات نصية بأربع سجلات (الاسم والموافقة · تاجر · الفورية · تاجر أبوظبي) بدون تغيير حالة ولا رقم |
| 0.10 | 2026-10-18 | اختبار G2 الجولة 2: AE-FOR-DXB-LICENCE وAE-FOR-DXB-INSTANT رسومهم صارت متغيرة (`variable: true`) باقتباس صفحة الخدمة «The fees for the service vary…» (N03) · AE-FOR-TM-REG وسمه `wants_trademark` بدل `all_founders` (N02) · «(كل سنة)» جنب غرفة دبي وانطلاق (N01) · سطر «ما فيه سجل إفصاح بهالإصدار» (N14) · سطري المسارات والرسوم بالخريطة (N08) · ولا حالة ولا رقم تغير |
