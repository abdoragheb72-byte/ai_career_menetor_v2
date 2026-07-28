import streamlit as st
from database import (
    get_all_cv_evaluations,
    get_all_cover_letters,
    get_all_interviews
)
from style import apply_custom_font

apply_custom_font()

st.title("📜 Previous History")

# ---------------- CV Evaluations ----------------

st.subheader("📊 تقييمات الـ CV السابقة")

evaluations = get_all_cv_evaluations()

if evaluations:

    for evaluation in reversed(evaluations):

        with st.expander(f"📅 {evaluation[5]}"):

            st.write(evaluation[4])

else:

    st.info("لا توجد تقييمات محفوظة حتى الآن.")

st.divider()

# ---------------- Cover Letters ----------------

st.subheader("✉️ Cover Letters السابقة")

letters = get_all_cover_letters()

if letters:

    for letter in reversed(letters):

        with st.expander(f"📅 {letter[3]}"):

            st.write(letter[2])

else:

    st.info("لا توجد Cover Letters محفوظة حتى الآن.")

st.divider()

# ---------------- Interviews ----------------

st.subheader("💬 المقابلات السابقة")

interviews = get_all_interviews()

if interviews:

    for interview in reversed(interviews):

        with st.container():

            st.markdown(f"**❓ السؤال:** {interview[2]}")

            st.markdown(f"**💬 الإجابة:** {interview[3]}")

            st.caption(f"📅 {interview[4]}")

            st.divider()

else:

    st.info("لا توجد مقابلات محفوظة حتى الآن.")