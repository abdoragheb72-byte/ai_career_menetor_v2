import os
from groq import Groq
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = "llama-3.3-70b-versatile"


# ---------------------------
# إرسال الطلب إلى Groq
# ---------------------------

def generate_response(prompt: str) -> str:

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=1500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ Error:\n{e}"


# ---------------------------
# تحليل الـ CV
# ---------------------------

def analyze_cv(cv_text: str, job_title: str) -> str:

    prompt = f"""
أنت خبير توظيف (HR Recruiter).

حلل السيرة الذاتية بالنسبة لوظيفة:

{job_title}

نص السيرة الذاتية:

{cv_text}

أعطني:

1- Match Score من 100

2- نقاط القوة

3- المهارات الناقصة

4- نقاط الضعف

5- أهم 5 اقتراحات للتحسين

6- القرار النهائي وهل تنصح بتوظيف المرشح أم لا.
"""

    return generate_response(prompt)


# ---------------------------
# إنشاء Cover Letter
# ---------------------------

def generate_cover_letter(
    cv_text: str,
    job_title: str,
    company_name: str = "Target Company"
):

    prompt = f"""
Write a professional Cover Letter in English.

Company:
{company_name}

Job Title:
{job_title}

Candidate CV:

{cv_text}

Requirements:
- Professional.
- Three paragraphs.
- Suitable for applying for this position.
"""

    return generate_response(prompt)