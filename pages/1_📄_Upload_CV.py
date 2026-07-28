import streamlit as st
from style import apply_custom_font

apply_custom_font()

st.title("📄 Upload Your CV")

st.write("ارفع السيرة الذاتية الخاصة بك ثم اكتب الوظيفة المستهدفة لبدء التحليل.")

uploaded_file = st.file_uploader(
    "ارفع الـ CV بتاعك (PDF أو Word)",
    type=["pdf", "docx"]
)

if uploaded_file:
    st.info(f"📁 تم اختيار الملف: {uploaded_file.name}")

job_title = st.text_input(
    "الوظيفة اللي بتقدم عليها",
    placeholder="مثال: Data Scientist"
)

if st.button("Analyze CV"):

    if uploaded_file is None:
        st.warning("⚠️ من فضلك ارفع ملف الـ CV أولاً.")

    elif not job_title.strip():
        st.warning("⚠️ من فضلك اكتب اسم الوظيفة.")

    else:
        st.session_state["uploaded_file"] = uploaded_file
        st.session_state["job_title"] = job_title

        st.success("✅ تم رفع البيانات بنجاح، انتقل إلى صفحة Evaluation.")