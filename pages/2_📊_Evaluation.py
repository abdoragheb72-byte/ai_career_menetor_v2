import streamlit as st
import tempfile
import os
import datetime

from style import apply_custom_font
from ai_engine import analyze_cv, generate_cover_letter
from document_reader import extract_text
from database import init_db, save_cv_evaluation, save_cover_letter

apply_custom_font()

# إنشاء قاعدة البيانات إذا لم تكن موجودة
init_db()

st.title("📊 CV Evaluation")

# التأكد من رفع الـ CV واختيار الوظيفة
if "job_title" not in st.session_state or "uploaded_file" not in st.session_state:
    st.warning("⚠️ ارفع الـ CV وحدد الوظيفة أولاً من صفحة Upload CV")
    st.stop()

job_title = st.session_state["job_title"]
uploaded_file = st.session_state["uploaded_file"]

file_extension = os.path.splitext(uploaded_file.name)[1]
tmp_path = None

try:
    # حفظ الملف مؤقتاً
    with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    # استخراج النص من الملف
    cv_text = extract_text(tmp_path)

except Exception as e:
    st.error(f"حدث خطأ أثناء قراءة الملف: {e}")
    cv_text = None

finally:
    if tmp_path and os.path.exists(tmp_path):
        os.remove(tmp_path)

# زر التحليل
if cv_text and st.button("Analyze CV"):

    with st.spinner("🔍 جاري تحليل الـ CV..."):
        result = analyze_cv(cv_text, job_title)

    with st.spinner("✍️ جاري إنشاء Cover Letter..."):
        cover_letter = generate_cover_letter(cv_text, job_title)

    # حفظ النتائج داخل Session
    st.session_state["analysis_result"] = result
    st.session_state["cover_letter_result"] = cover_letter

    # حفظ النتائج داخل قاعدة البيانات
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        save_cv_evaluation(
            user_id=1,
            cv_text=cv_text,
            score=0,
            feedback=result,
            date=date
        )

        save_cover_letter(
            user_id=1,
            letter_text=cover_letter,
            date=date
        )

    except Exception as db_error:
        st.warning(f"تعذر حفظ البيانات في قاعدة البيانات: {db_error}")

# عرض النتائج إن وجدت
if "analysis_result" in st.session_state:

    st.subheader("📊 نتيجة تقييم الـ CV")
    st.write(st.session_state["analysis_result"])

    st.subheader("✍️ Cover Letter المقترح")

    st.text_area(
        "Cover Letter",
        st.session_state["cover_letter_result"],
        height=250
    )