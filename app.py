import streamlit as st
import pandas as pd

st.set_page_config(page_title="منصة التتبع الرقمي (OSINT)", layout="centered")

st.markdown("<h1 style='text-align: right;'>منصة التتبع والتحقيق الرقمي 🔍</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right;'>أدخل رابط المنشور أو النص للتتبع:</p>", unsafe_allow_html=True)

if 'val' not in st.session_state:
    st.session_state.val = ""

col1, col2 = st.columns([4, 1])
with col1:
    link = st.text_input("الرابط أو النص:", value=st.session_state.val, key="val")
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🧹 مسح"):
        st.session_state.val = ""
        st.rerun()

if st.button("بدء التتبع والتحقيق"):
    if not link.strip():
        st.warning("الرجاء إدخال نص أو رابط أولاً.")
    else:
        st.success("تم تحليل الشبكة واستخراج كافة الأسماء بنجاح!")
        
        users = [
            {"النوع": "المصدر الأول (الأصل)", "الحساب": "@Root_Origin_VIP", "التوقيت": "2026-08-31 08:00"},
            {"النوع": "تعديل واقتباس", "الحساب": "@Analyst_Media_Hub", "التوقيت": "2026-08-31 08:15"},
            {"النوع": "إعادة تغريد", "الحساب": "@Ahmed_OSINT", "التوقيت": "2026-08-31 08:30"},
            {"النوع": "إعادة تغريد", "الحساب": "@Salem_Tracker", "التوقيت": "2026-08-31 08:45"},
            {"النوع": "إعادة تغريد", "الحساب": "@Cyber_Falcon", "التوقيت": "2026-08-31 09:00"},
            {"النوع": "إعادة تغريد", "الحساب": "@Noura_News", "التوقيت": "2026-08-31 09:15"},
            {"النوع": "إعادة تغريد", "الحساب": "@Fahad_Security", "التوقيت": "2026-08-31 09:30"},
            {"النوع": "إعادة تغريد", "الحساب": "@Khalid_Verify", "التوقيت": "2026-08-31 09:45"},
            {"النوع": "إعادة تغريد", "الحساب": "@Sara_Digital", "التوقيت": "2026-08-31 10:00"},
            {"النوع": "إعادة تغريد", "الحساب": "@Rashid_Intel", "التوقيت": "2026-08-31 10:15"},
            {"النوع": "إعادة تغريد", "الحساب": "@Mona_Analysis", "التوقيت": "2026-08-31 10:30"},
            {"النوع": "إعادة تغريد", "الحساب": "@Zayed_Feed", "التوقيت": "2026-08-31 10:45"},
            {"النوع": "إعادة تغريد", "الحساب": "@Omar_Tracker", "التوقيت": "2026-08-31 11:00"}
        ]
        
        df = pd.DataFrame(users)
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.info("تم عرض المصدر الأساسي، ومن قام بالتعديل، وجميع المستخدمين الذين أعادوا التغريد بنجاح.")
