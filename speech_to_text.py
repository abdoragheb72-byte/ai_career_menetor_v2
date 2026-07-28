import streamlit as st
import speech_recognition as sr
import tempfile
import os


def speech_to_text(language="ar-EG"):
    st.write("🎤 اضغط على الزر وسجل صوتك")

    audio_file = st.audio_input("سجل إجابتك")

    if audio_file is None:
        return None

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_file.read())
        temp_file = f.name

    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(temp_file) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(
            audio,
            language=language
        )

        st.success(f"🎤 أنت: {text}")

        return text

    except sr.UnknownValueError:
        st.error("لم أستطع فهم الكلام.")
        return None

    except sr.RequestError:
        st.error("حدث خطأ في خدمة التعرف على الصوت.")
        return None

    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)