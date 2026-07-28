import os
import tempfile
import streamlit as st
from gtts import gTTS


def text_to_speech(text, language="ar"):
    """
    تحويل النص إلى صوت وتشغيله داخل Streamlit.
    """

    temp_file = None

    try:
        with tempfile.NamedTemporaryFile(
            suffix=".mp3",
            delete=False
        ) as temp:
            temp_file = temp.name

        tts = gTTS(
            text=text,
            lang=language,
            slow=False
        )

        tts.save(temp_file)

        with open(temp_file, "rb") as audio:
            st.audio(audio.read(), format="audio/mp3", autoplay=True)

        return True

    except Exception as e:
        st.error(f"❌ خطأ في تحويل النص إلى صوت:\n{e}")
        return False

    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)


if __name__ == "__main__":
    st.title("Text To Speech Test")

    if st.button("تشغيل"):
        text_to_speech("مرحباً بك في مشروع AI Career Mentor.")