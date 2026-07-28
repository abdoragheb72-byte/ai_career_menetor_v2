import streamlit as st
from style import apply_custom_font

# تطبيق الخط المخصص
apply_custom_font()

# إعداد الصفحة
st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="💼",
    layout="wide"
)

# عنوان المشروع
st.title("💼 AI Career Mentor")
st.markdown("### مرحبًا بك في مساعدك الذكي للاستعداد لسوق العمل")

st.write(
    """
يساعدك هذا المشروع على:

- 📄 تحليل السيرة الذاتية (CV)
- 🎤 إجراء مقابلة عمل بالذكاء الاصطناعي
- 📝 إنشاء Cover Letter
- 📊 متابعة نتائجك وتقييم أدائك
"""
)

st.divider()

# بيانات المستخدم
st.subheader("👤 بيانات المستخدم")

name = st.text_input(
    "اكتب اسمك",
    placeholder="مثال: Ahmed Mohamed"
)

if st.button("💾 حفظ الاسم", use_container_width=True):

    if name.strip():

        st.session_state["user_name"] = name.strip()

        st.success(f"مرحبًا {name} 👋")

    else:
        st.warning("من فضلك اكتب اسمك أولاً.")

# عرض الاسم الحالي
if "user_name" in st.session_state:

    st.info(f"👤 المستخدم الحالي: {st.session_state['user_name']}")

st.divider()

# معلومات عن المشروع
st.subheader("🚀 مميزات المشروع")

col1, col2 = st.columns(2)

with col1:
    st.success("📄 تحليل الـ CV")
    st.success("🎤 مقابلة عمل ذكية")
    st.success("📝 إنشاء Cover Letter")

with col2:
    st.success("📊 تقييم الأداء")
    st.success("🤖 مدعوم بالذكاء الاصطناعي")
    st.success("💾 حفظ النتائج")

st.divider()

st.caption("AI Career Mentor © 2026")