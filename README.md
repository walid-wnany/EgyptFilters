# المصرية للفلاتر — نسخة كاملة جاهزة لـ Streamlit Cloud

## الملفات
- `app.py` — نقطة تشغيل التطبيق والتنقل الرئيسي.
- `home.py` — الصفحة الرئيسية.
- `seo_utils.py` — التصميم المشترك، RTL، الروابط، CTA، وقالب الصفحات.
- `pages/` — صفحات المناطق والخدمات.
- `requirements.txt` — الاعتمادات.
- `.streamlit/config.toml` — إعدادات Streamlit.

## الرفع
ارفع محتويات هذا المجلد إلى مستودع GitHub واحد، ثم اجعل `app.py` هو Main file في Streamlit Cloud.

النسخة تتضمن:
- إصلاح `StreamlitPageNotFoundError`.
- إصلاح `ImportError` الخاص بـ `render_service_page`.
- تقليل التكرار بين الصفحات.
- اتجاه RTL موحد.
- روابط داخلية باستخدام نفس `st.Page` objects.
