import os
import tempfile
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr


DURATION = 8
SAMPLE_RATE = 44100


def speech_to_text(language="ar-EG"):
    recognizer = sr.Recognizer()

    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.8
    recognizer.energy_threshold = 250

    print("\n🎤 تحدث الآن...\n")

    try:
        recording = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16",
        )

        sd.wait()

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as temp_audio:

            temp_file = temp_audio.name

        sf.write(temp_file, recording, SAMPLE_RATE)

        with sr.AudioFile(temp_file) as source:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.3,
            )

            audio = recognizer.record(source)

        text = recognizer.recognize_google(
            audio,
            language=language,
        )

        print(f"🎤 أنت: {text}")

        os.remove(temp_file)

        return text

    except sr.UnknownValueError:
        print("❌ لم يتم التعرف على الكلام.")
        return None

    except sr.RequestError:
        print("❌ لا يوجد اتصال بالإنترنت.")
        return None

    except Exception as e:
        print(f"❌ {e}")
        return None

    finally:
        try:
            if 'temp_file' in locals() and os.path.exists(temp_file):
                os.remove(temp_file)
        except:
            pass


if __name__ == "__main__":
    speech_to_text()