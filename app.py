import streamlit as st
import pandas as pd
import re

# إعداد الصفحة
st.set_page_config(
    page_title="منصة الاستخبارات الرقمية الصارمة (OSINT)",
    page_icon="🛡️",
    layout="centered"
)

# تخصيص واجهة المستخدم CSS
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

st.markdown("<h1 style='text-align: right; font-size: 28px;'>🛡️ منصة الاستخبارات الرقمية الصارمة (Strict OSINT)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right; color: #94a3b8;'>النظام المحدث: كتابة 'لا يوجد' في حال عدم توفر البيانات الحقيقية المؤكدة.</p><hr style='border-color: #1f2937;'>", unsafe_allow_html=True)

if 'target_query' not in st.session_state:
    st.session_state.target_query = ""

def clear_query():
    st.session_state.target_query = ""

col_input, col_clear = st.columns([4, 1])
with col_input:
    target_input = st.text_input(
        "أدخل الهدف (رابط، اسم مستخدم، أو بريد إلكتروني):", 
        value=st.session_state.target_query, 
        key="target_query", 
        placeholder="مثال: user@example.com أو @username"
    )
with col_clear:
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🧹 مسح المدخل", on_click=clear_query)

st.markdown("<br>", unsafe_allow_html=True)

tab_all, tab_qr, tab_posts, tab_social = st.tabs([
    "🔍 التحليل الشامل الصارم", 
    "📷 مسح وقراءة الباركود (QR)", 
    "📝 تحليل المنشورات وصاحب التغريدة", 
    "🌐 كشف الحسابات المرتبطة والمقترحات"
])

# محرك صارم يعيد "لا يوجد" لعدم وجود ربط برمجي بقواعد بيانات حية خارجية
def strict_osint_lookup(query):
    q = query.strip()
    if not q:
        return None
    
    # استخراج دقيق لأي يوزر إن وجد في النص أو الرابط
    username = "لا يوجد"
    if q.startswith("@"):
        username = q
    elif "@" in q and "." in q:
        username = "@" + q.split('@')[0]
    else:
        match = re.search(r'(?:https?://)?(?:www\.)?(?:twitter\.com|x\.com|instagram\.com|t\.me)/([A-Za-z0-9_.]+)', q)
        if match:
            username = "@" + match.group(1)

    # التحقق من الإيميل الحقيقي المدخل
    email = q if ("@" in q and "." in q and not q.startswith("http") and not q.startswith("@")) else "لا يوجد"

    return {
        "query": q,
        "username": username,
        "device": "لا يوجد (يتطلب تفعيل تتبع الأجهزة عبر API)",
        "email": email,
        "phone": "لا يوجد",
        "server": "لا يوجد",
        "location": "لا يوجد",
        "social": "لا يوجد",
        "similar": "لا يوجد"
    }

with tab_all:
    st.markdown("<h3>التحليل الشامل (الوضع الصارم)</h3>", unsafe_allow_html=True)
    
    if st.button("🚀 بدء الفحص الصارم"):
        if not target_input.strip():
            st.warning("⚠️ الرجاء إدخال الهدف أولاً.")
        else:
            data = strict_osint_lookup(target_input)
            st.success("تم الفحص. البيانات غير المتوفرة تم تحديدها بـ 'لا يوجد'.")
            st.markdown("---")
            
            df_data = [
                {"المؤشر": "الهدف المدخل", "النتيجة الحقيقية": data["query"]},
                {"المؤشر": "اسم المستخدم", "النتيجة الحقيقية": data["username"]},
                {"المؤشر": "نوع الجهاز", "النتيجة الحقيقية": data["device"]},
                {"المؤشر": "البريد الإلكتروني", "النتيجة الحقيقية": data["email"]},
                {"المؤشر": "رقم الهاتف", "النتيجة الحقيقية": data["phone"]},
                {"المؤشر": "الخادم الرقمي", "النتيجة الحقيقية": data["server"]},
                {"الموقع الجغرافي": "الموقع", "النتيجة الحقيقية": data["location"]}
            ]
            st.dataframe(pd.DataFrame(df_data), use_container_width=True, hide_index=True)

with tab_qr:
    st.markdown("<h3>ماسح الباركود</h3>", unsafe_allow_html=True)
    uploaded_qr = st.file_uploader("اختر صورة الباركود:", type=["png", "jpg", "jpeg"], key="qr_strict")
    if uploaded_qr is not None:
        st.image(uploaded_qr, width=300)
        if st.button("🔍 قراءة الباركود"):
            st.code(f"الملف: {uploaded_qr.name}\nالبيانات المضمنة: لا يوجد تحليل نصي مباشر متاح حالياً\nنوع الجهاز المنشئ: لا يوجد\nالموقع: لا يوجد")

with tab_posts:
    st.markdown("<h3>محلل المنشورات وصاحب التغريدة الأولى</h3>", unsafe_allow_html=True)
    media_file = st.file_uploader("ارفع صورة أو فيديو:", type=["png", "jpg", "jpeg", "mp4"], key="media_strict")
    
    if st.button("📊 فحص المنشور وسلسلة الانتشار"):
        st.info("لعدم توفر اتصال مباشر بخوادم المنصات الحية لاستخراج سجلات التعديل والناشرين بدقة تامة:")
        st.markdown("""
        * **صاحب التغريدة الأولى:** لا يوجد
        * **من قام بالنشر أو التعديل:** لا يوجد
        * **بيانات الصور والمقاطع (EXIF):** لا يوجد (أو تظهر الحقول الخالية كـ 'لا يوجد' لغياب الأدوات السحابية المرخصة).
        """)

with tab_social:
    st.markdown("<h3>كشف الحسابات المرتبطة والمقترحات</h3>", unsafe_allow_html=True)
    if st.button("🌐 فحص الحسابات المقترحة"):
        if not target_input.strip():
            st.warning("⚠️ الرجاء إدخال الهدف في خانة البحث.")
        else:
            st.markdown("* **الحسابات المؤكدة المرتبطة:** لا يوجد")
            st.markdown("* **المربع الاحتياطي للحسابات المشابهة أو البديلة:** لا يوجد حسابات مطابقة مرتبطة حالياً في السجلات العامة.")
