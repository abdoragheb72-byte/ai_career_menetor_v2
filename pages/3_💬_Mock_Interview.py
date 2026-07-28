import streamlit as st
import datetime

from database import save_interview
from AI_services_team_final_with_key import interview_chat
from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from voice_assistant import voice_interview_round
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

# التاريخ الخاص بالمحادثة مع الـ AI
if "voice_history" not in st.session_state:
    st.session_state.voice_history = []

if "auto_interview" not in st.session_state:
    st.session_state.auto_interview = False

if "first_question_spoken" not in st.session_state:
    text_to_speech(st.session_state.messages[0]["content"])
    st.session_state.first_question_spoken = True


# ---------------- إرسال رسالة ----------------

def send_message(prompt):

    if not prompt:
        return

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    reply, st.session_state.voice_history = interview_chat(
        prompt,
        st.session_state.voice_history
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    text_to_speech(reply)

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

prompt = st.chat_input("اكتب إجابتك...")

if prompt:
    send_message(prompt)
    st.rerun()


# ---------------- الأزرار ----------------

col1, col2 = st.columns(2)

with col1:

    if st.button("🎤 Speak مرة واحدة"):

        with st.spinner("🎙️ جاري الاستماع..."):
            voice = speech_to_text()

        if voice:
            send_message(voice)
            st.rerun()

with col2:

    if not st.session_state.auto_interview:

        if st.button("▶️ Start Voice Interview"):
            st.session_state.auto_interview = True
            st.rerun()

    else:

        if st.button("⏹️ Stop Interview"):
            st.session_state.auto_interview = False
            st.success("تم إيقاف المقابلة.")
            st.rerun()


# ---------------- المقابلة المستمرة ----------------

if st.session_state.auto_interview:

    with st.spinner("🎤 جاري الاستماع..."):

        user_text, ai_response, new_history = voice_interview_round(
            st.session_state.voice_history
        )

    st.session_state.voice_history = new_history

    if user_text == "توقف":

        st.session_state.auto_interview = False
        st.success("تم إنهاء المقابلة.")
        st.rerun()

    elif user_text:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_text
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )

        text_to_speech(ai_response)

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            save_interview(
                user_id=1,
                question=user_text,
                answer=ai_response,
                date=date
            )
        except Exception as e:
            st.warning(f"تعذر حفظ المقابلة: {e}")

        st.rerun()