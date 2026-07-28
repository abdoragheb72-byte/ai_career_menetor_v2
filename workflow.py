from document_reader import extract_text
from ai_engine import analyze_cv, generate_cover_letter
from database import (
    save_cv_evaluation,
    save_cover_letter,
    save_interview,
)
import datetime


def process_and_save_cv(user_id, file_path, job_title):
    """
    قراءة الـ CV وتحليله وإنشاء Cover Letter ثم حفظ النتائج.
    """

    try:
        # استخراج النص من الـ CV
        cv_text = extract_text(file_path)

        # تحليل الـ CV
        feedback = analyze_cv(cv_text, job_title)

        # إنشاء Cover Letter
        cover_letter = generate_cover_letter(cv_text, job_title)

        # التاريخ الحالي
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # حفظ النتائج
        save_cv_evaluation(
            user_id=user_id,
            cv_text=cv_text,
            score=0,
            feedback=feedback,
            date=date,
        )

        save_cover_letter(
            user_id=user_id,
            letter_text=cover_letter,
            date=date,
        )

        return feedback, cover_letter

    except Exception as e:
        raise Exception(f"Error while processing CV: {e}")


def process_interview(user_id, question, history=""):
    """
    إرسال السؤال للذكاء الاصطناعي وحفظ النتيجة.
    """

    from AI_services_team_final_with_key import interview_chat

    try:
        answer = interview_chat(question, history)

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        save_interview(
            user_id=user_id,
            question=question,
            answer=answer,
            date=date,
        )

        return answer

    except Exception as e:
        return f"حدث خطأ أثناء المقابلة:\n{e}"


if __name__ == "__main__":

    print("Workflow module loaded successfully.")