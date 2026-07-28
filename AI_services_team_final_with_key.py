import os
from groq import Groq
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("يرجى إضافة GROQ_API_KEY داخل ملف .env")

client = Groq(api_key=API_KEY)


def interview_chat(user_answer, history=None):
    """
    إجراء مقابلة عمل باستخدام Groq AI.
    """

    if history is None:
        history = []

    system_prompt = """
أنت مسؤول توظيف (HR) محترف.

يجب أن يكون الرد باللغة العربية فقط.

بعد كل إجابة من المتقدم قم بالآتي:

1- تقييم الإجابة من 10.
2- ذكر نقطة قوة.
3- ذكر نقطة تحتاج للتحسين.
4- تقديم نصيحة قصيرة.
5- طرح سؤال مقابلة جديد واحد فقط.

التزم بالتنسيق التالي:

التقييم: /10

نقطة القوة:
...

نقطة التحسين:
...

النصيحة:
...

السؤال التالي:
...
"""

    messages = [{"role": "system", "content": system_prompt}]

    messages.extend(history)

    messages.append({
        "role": "user",
        "content": user_answer
    })

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.6,
            max_tokens=700,
        )

        reply = response.choices[0].message.content.strip()

        history.append({
            "role": "user",
            "content": user_answer
        })

        history.append({
            "role": "assistant",
            "content": reply
        })

        return reply, history

    except Exception as e:
        return f"حدث خطأ أثناء الاتصال بـ Groq:\n{str(e)}", history


if __name__ == "__main__":

    history = []

    print("=" * 50)
    print(" AI Career Mentor ")
    print("=" * 50)
    print("اكتب exit للخروج.\n")

    while True:

        user = input("أنت: ")

        if user.lower() == "exit":
            print("تم إنهاء المقابلة.")
            break

        reply, history = interview_chat(user, history)

        print("\nHR:\n")
        print(reply)
        print("-" * 50)