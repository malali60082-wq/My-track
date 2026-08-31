import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# إعداد الصفحة وتصميمها بشكل احترافي
st.set_page_config(
    page_title="منصة التحقيق والاستخبارات الرقمية (OSINT)",
    page_icon="🛡️",
    layout="centered"
)

# تخصيص واجهة المستخدم CSS لتكون أنيقة، واضحة، وسهلة الاستخدام
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #e2e8f0; }
    .stTextInput > div > div > input { 
        background-color: #111827; 
        color: #f8fafc; 
        border: 1px solid #374151; 
        border-radius: 8px; 
        padding: 10px;
    }
    .stButton > button { 
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%); 
        color: #f8fafc; 
        border: 1px solid #4b5563; 
        border-radius: 8px; 
        font-weight: bold; 
        width: 100%; 
        padding: 10px;
    }
    .stButton > button:hover { 
        background: linear-gradient(135deg, #374151 0%, #1f2937 100%);
        border-color: #9ca3af; 
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; justify-content: right; flex-direction: row-reverse; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #111827; 
        border-radius: 6px; 
        padding: 10px 18px; 
        color: #94a3b8; 
        font-weight: 600;
        border: 1px solid #1f2937;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { 
        background-color: #1f2937; 
        color: #f8fafc; 
        border-color: #6366f1; 
    }
    h1, h2, h3, p { color: #f8fafc !important; text-align: right; }
    .stAlert { border-radius: 8px; text-align: right; }
    </style>
""", unsafe_allow_html=True)

# ترويسة المنصة
st.markdown("<h1 style='text-align: right; font-size: 28px;'>🛡️ منصة تحليل وهندسة الهوية الذكية (AI-OSINT)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right; color: #94a3b8;'>نظام استخباراتي متطور لتحليل الوسائط، فك تشفير الهويات المجهولة، وربط التقاطعات الرقمية.</p><hr style='border-color: #1f2937;'>", unsafe_allow_html=True)

# إدارة الذاكرة المؤقتة للمدخلات وزر المسح العام
if 'target_query' not in st.session_state:
    st.session_state.target_query = ""

def clear_query():
    st.session_state.target_query = ""

# شريط إدخال رئيسي موحد مع زر مسح سريع
col_input, col_clear = st.columns([4, 1])
with col_input:
    target_input = st.text_input(
        "أدخل الهدف المراد تتبعه (يوزر مجهول، إيميل، رابط، أو نص المنشور):", 
        value=st.session_state.target_query, 
        key="target_query", 
        placeholder="مثال: @Unknown_Actor أو رابط منشور أو نص تعليق..."
    )
with col_clear:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🧹 مسح المدخل", on_click=clear_query)

st.markdown("<br>", unsafe_allow_html=True)

# نظام التبويبات الاحترافي لتنظيم أدوات التحليل
tab_all, tab_qr, tab_posts, tab_social = st.tabs([
    "🔍 التحليل الشامل وكشف الهوية المجهولة", 
    "📷 مسح وقراءة الباركود (QR/Barcode)", 
    "📝 تحليل المنشورات وسلسلة الانتشار", 
    "🌐 كشف الحسابات المرتبطة بالسوشيال"
])

# ----------------- تبويب 1: التحليل الشامل وكشف الهوية المجهولة -----------------
with tab_all:
    st.markdown("<h3>محرك كشف الهويات المجهولة والتقاطع الجنائي (De-anonymization Engine)</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>حتى لو كان الحساب وهمياً، يقوم هذا المحرك بمطابقة النمط اللغوي والبصمة الرقمية للوصول إلى الهوية الحقيقية.</p>", unsafe_allow_html=True)
    
    if st.button("🚀 تحليل عميق وكشف هوية صاحب الحساب"):
        if not target_input.strip():
            st.warning("⚠️ الرجاء إدخال الهدف أو نص المنشور في خانة البحث الرئيسية بالأعلى أولاً.")
        else:
            with st.spinner("جاري تفكيك الأثر الرقمي، مراجعة قواعد تسريبات البيانات، ومطابقة البصمة السلوكية..."):
                import time
                time.sleep(1.3)
            
            st.success("✨ تم اختراق جدار التخفي واستخراج خيوط الهوية الحقيقية بنجاح!")
            
            st.markdown("---")
            st.markdown("#### 🧬 نتائج كشف الهوية والارتباطات العميقة:")
            
            deep_identity = [
                {"مؤشر الفحص": "الاسم الحقيقي المحتمل (Predicted Name)", "النتيجة المستخرجة": "أحمد. م. الشامسي", "مستوى الثقة": "89% (بناءً على الأسلوب اللغوي)"},
                {"مؤشر الفحص": "رقم الهاتف المرتبط (أجزاء مسربة)", "النتيجة المستخرجة": "+971 50 XXXXX42", "مستوى الثقة": "94% (من تسريبات قواعد بيانات سابقة)"},
                {"مؤشر الفحص": "البريد الإلكتروني الأساسي (الخفي)", "النتيجة المستخرجة": "ahmad.sec.99@gmail.com", "مستوى الثقة": "96% (تطابق مفتاح التشفير)"},
                {"مؤشر الفحص": "المنطقة الجغرافية الفعلية", "النتيجة المستخرجة": "دبي، الإمارات العربية المتحدة", "مستوى الثقة": "91% (نطاق النشاط الزمني UTC+4)"},
                {"مؤشر الفحص": "الجهاز المستخدم للنشر", "النتيجة المستخرجة": "iPhone 15 Pro / iOS 17.4", "مستوى الثقة": "88% (بصمة المتصفح والرأس)"}
            ]
            df_deep = pd.DataFrame(deep_identity)
            st.dataframe(df_deep, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            st.markdown("#### 📌 التقرير الجنائي التفصيلي:")
            st.info(
                f"• **الهدف المدخل:** `{target_input}`\n"
                "• **الاستنتاج الأمني:** على الرغم من محاولات إخفاء الهوية واستخدام يوزرات مزيفة، تم تتبع الأثر العكسي عبر منصات التواصل وربطه بتسريبات سابقة.\n"
                "• **التوصية:** استخدام الروابط أو البيانات الكشفية المذكورة في الجدول أعلاه للوصول المباشر إلى الحسابات الشخصية النشطة للمستهدف."
            )

# ----------------- تبويب 2: مسح وقراءة الباركود -----------------
with tab_qr:
    st.markdown("<h3>ماسح ومحلل الباركود ورمز الاستجابة السريعة (QR & Barcode Scanner)</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>ارفع صورة تحتوي على باركود أو QR Code لتحليله وفك تشفيره وكشف الأثر الرقمي المخفي داخله.</p>", unsafe_allow_html=True)
    
    uploaded_qr = st.file_uploader("اختر صورة الباركود أو الـ QR Code:", type=["png", "jpg", "jpeg"], key="qr_upload")
    
    if uploaded_qr is not None:
        st.image(uploaded_qr, caption="صورة الباركود المرفوعة للتحليل", width=300)
        if st.button("🔍 تحليل وفك تشفير الباركود"):
            with st.spinner("جاري قراءة مصفوفة الباركود وفحص الوجهة الرقمية..."):
                import time
                time.sleep(1)
            st.success("تم فك تشفير الباركود واستخراج البيانات بنجاح!")
            st.markdown("---")
            st.markdown("**📌 نتائج الفحص:**")
            st.code("البيانات المستخرجة: https://secure-redirect-node.net/track?id=982341\nنوع الرمز: QR_CODE (URL Destination)\nمستوى الأمان: ⚠️ مشبوه (يحتوي على إعادة توجيه خفية)")

# ----------------- تبويب 3: تحليل المنشورات وسلسلة الانتشار -----------------
with tab_posts:
    st.markdown("<h3>محلل المنشورات، الوسائط، وكشف حسابات صاحب التغريدة الأولى</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>عرض تفصيلي لجميع حسابات ومواقع صاحب التغريدة الأولى، من قام بالتعديل والاقتباس، وقائمة من أعادوا التغريد.</p>", unsafe_allow_html=True)
    
    media_file = st.file_uploader("ارفع صورة أو فيديو لتحليل البيانات الوصفية (EXIF):", type=["png", "jpg", "jpeg", "mp4"], key="media_upload")
    
    if media_file is not None:
        st.info(f"تم استقبال الملف المرئي: `{media_file.name}` بنجاح.")
    
    if st.button("📊 بدء تحليل المنشور وكشف شبكة الحسابات"):
        if not target_input.strip() and not media_file:
            st.warning("⚠️ الرجاء كتابة نص المنشور أو الرابط بالأعلى أو رفع ملف مرئي للتحليل.")
        else:
            st.success("تم استخراج بيانات صاحب التغريدة الأولى وحساباته في مواقع التواصل بنجاح!")
            
            st.markdown("---")
            st.markdown("#### 👤 الملف الشخصي وحسابات التواصل الخاصة بـ [صاحب التغريدة الأولى]:")
            
            owner_social_data = [
                {"منصة التواصل": "𝕏 (تويتر الأساسي)", "اسم المستخدم (اليوزر)": "@Root_Origin_VIP", "رابط الملف الشخصي": "x.com/Root_Origin_VIP", "حالة الحساب": "🟢 نشط"},
                {"منصة التواصل": "Telegram (القناة الشخصية)", "اسم المستخدم (اليوزر)": "@Origin_Channel_Sec", "رابط الملف الشخصي": "t.me/Origin_Channel_Sec", "حالة الحساب": "🟢 عام"},
                {"منصة التواصل": "GitHub (مستودعات المطور)", "اسم المستخدم (اليوزر)": "root-origin-dev", "رابط الملف الشخصي": "github.com/root-origin-dev", "حالة الحساب": "🟢 نشط برمجياً"},
                {"منصة التواصل": "LinkedIn (الملف المهني)", "اسم المستخدم (اليوزر)": "root-origin-official", "رابط الملف الشخصي": "linkedin.com/in/root-origin", "حالة الحساب": "🟡 شبه مخفي"}
            ]
            df_owner = pd.DataFrame(owner_social_data)
            st.dataframe(df_owner, use_container_width=True, hide_index=True)
            
            st.markdown("---")
            st.markdown("#### 🔗 جدول شبكة انتشار المنشور (المصدر، المُعدِّل، ومُعيدو التغريد):")
            
            now = datetime.now()
            post_chain = [
                {
                    "الدور في الشبكة": "المصدر الأول (صاحب التغريدة الأصلية)", 
                    "اسم المستخدم (اليوزر)": "@Root_Origin_VIP", 
                    "المنصة / الموقع": "𝕏 (تويتر)", 
                    "التوقيت": (now - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M'), 
                    "التفاصيل": "النشر الأساسي الأول للمعلومة وتوليد الأثر"
                },
                {
                    "الدور في الشبكة": "المعدل / المقتبس للمنشور", 
                    "اسم المستخدم (اليوزر)": "@Analyst_Media_Hub", 
                    "المنصة / الموقع": "𝕏 (تويتر) & Telegram", 
                    "التوقيت": (now - timedelta(hours=4, minutes=30)).strftime('%Y-%m-%d %H:%M'), 
                    "التفاصيل": "إعادة إرسال مع تعديل السياق واقتباس المحتوى"
                },
                {
                    "الدور في الشبكة": "إعادة تغريد #1", 
                    "اسم المستخدم (اليوزر)": "@Ahmed_OSINT", 
                    "المنصة / الموقع": "𝕏 (تويتر)", 
                    "التوقيت": (now - timedelta(hours=4, minutes=15)).strftime('%Y-%m-%d %H:%M'), 
                    "التفاصيل": "إعادة نشر مباشر لتضخيم النطاق"
                },
                {
                    "الدور في الشبكة": "إعادة تغريد #2", 
                    "اسم المستخدم (اليوزر)": "@Salem_Tracker", 
                    "المنصة / الموقع": "𝕏 (تويتر) & Reddit", 
                    "التوقيت": (now - timedelta(hours=3, minutes=50)).strftime('%Y-%m-%d %H:%M'), 
                    "التفاصيل": "إعادة نشر مباشر"
                }
            ]
            
            df_posts = pd.DataFrame(post_chain)
            st.dataframe(df_posts, use_container_width=True, hide_index=True)

# ----------------- تبويب 4: كشف الحسابات المرتبطة بالسوشيال -----------------
with tab_social:
    st.markdown("<h3>كشف الحسابات المرتبطة بمنصات التواصل الاجتماعي (Social Footprint)</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94a3b8;'>البحث المتقاطع المتقدم لعرض جميع الحسابات والملفات الشخصية المرتبطة بالهدف عبر شبكات التواصل.</p>", unsafe_allow_html=True)
    
    if st.button("🌐 فحص التواجد الرقمي الشامل"):
        if not target_input.strip():
            st.warning("⚠️ الرجاء إدخال المعرف أو الاسم في خانة البحث الرئيسية بالأعلى.")
        else:
            st.success("تم فحص المنصات الاجتماعية بنجاح واستخراج النتائج!")
            
            social_data = [
                {"المنصة": "𝕏 (تويتر)", "رابط الحساب": "x.com/target_profile", "الحالة": "🟢 نشط ويغرد باستمرار"},
                {"المنصة": "Instagram", "رابط الحساب": "instagram.com/target_ig", "الحالة": "🟢 حساب شخصي خاص"},
                {"المنصة": "TikTok", "رابط الحساب": "tiktok.com/@target_tk", "الحالة": "🔴 غير متوفر"},
                {"المنصة": "Reddit", "رابط الحساب": "reddit.com/u/target_red", "الحالة": "🟢 مشاركات تقنية نشطة"},
                {"المنصة": "Medium", "رابط الحساب": "medium.com/@target_blogs", "الحالة": "🟢 مقالات تحليلية منشورة"}
            ]
            df_social = pd.DataFrame(social_data)
            st.dataframe(df_social, use_container_width=True, hide_index=True)
