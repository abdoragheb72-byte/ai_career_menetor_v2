#!/bin/bash

# سكريبت تشغيل مشروع AI Career Mentor
# استخدميه بالأمر: bash start.sh

# يروح لمكان المشروع (نفس المكان اللي فيه السكريبت ده)
cd "$(dirname "$0")"

# إعدادات الترميز عشان النصوص العربية تشتغل صح مع Gemini API
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export PYTHONUTF8=1

echo "🚀 جاري تشغيل AI Career Mentor..."
echo "📁 من المسار: $(pwd)"
echo ""

# تشغيل التطبيق
python3 -m streamlit run ai_career.py
