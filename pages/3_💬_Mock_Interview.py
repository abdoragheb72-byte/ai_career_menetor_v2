import streamlit as st
import datetime

from database import save_interview
from AI_services_team_final_with_key import interview_chat
from style import apply_custom_font

apply_custom_font()

st.title("💬 Mock Interview")

# ---------------- Session State ----------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "أهلاً! جاهز نبدأ المقابلة؟ احكيلي عن نفسك."
        }
    ]

if "voice_history" not in st.session_state:
    st.session_state.voice_history = []

# ---------------- إرسال رسالة ----------------

def send_message(prompt):

    if not prompt:
        return

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    reply, st.session_state.voice_history = interview_chat(
        prompt,
        st.session_state.voice_history
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        save_interview(
            user_id=1,
            question=prompt,
            answer=reply,
            date=date
        )
    except Exception as e:
        st.warning(f"تعذر حفظ المقابلة: {e}")

# ---------------- عرض المحادثة ----------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- الكتابة ----------------

prompt = st.chat_input("اكتب إجابتك هنا...")

if prompt:
    send_message(prompt)
    st.rerun()