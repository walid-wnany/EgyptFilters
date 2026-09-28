# المصرية للفلاتر — نسخة Streamlit Community Cloud

هذه النسخة مخصصة للرفع مباشرة على Streamlit Community Cloud.

## محتويات الباكدج
- `app.py` نقطة تشغيل التطبيق.
- `home.py` الصفحة الرئيسية.
- `seo_utils.py` التصميم المشترك وRTL واللوجو.
- `pages/` صفحات المناطق والخدمات.
- `assets/logo.png` اللوجو المرفق.
- `.streamlit/config.toml` إعدادات Streamlit.
- `requirements.txt` الاعتماديات المطلوبة.

## الرفع
1. فك الضغط.
2. ارفع **محتويات المجلد** إلى Root في GitHub، بحيث يكون `app.py` في Root.
3. في Streamlit Community Cloud اختر المستودع والفرع ثم ملف التشغيل `app.py`.
4. Deploy.

## مهم
- لا تضع الملفات داخل مجلد إضافي داخل المستودع.
- هذه النسخة لا تحتاج Docker أو Nginx على Streamlit Community Cloud.
- اللوجو مدمج في التطبيق والـ Sidebar وأيقونة الصفحة.
- اتجاه التطبيق بالكامل RTL.
- روابط الصفحات تستخدم نفس كائنات `st.Page` لتجنب خطأ `StreamlitPageNotFoundError`.

## الدومين
Streamlit Community Cloud يعطي رابطاً على `streamlit.app`. استخدام `https://flatermasr.com/` نفسه يحتاج خدمة/استضافة تدعم Custom Domain أو Reverse Proxy خارج Community Cloud.


## مناطق الخدمة المضافة
- القاهرة: 15 مايو (50 فدان، 120 فدان، 290 فدان) والقاهرة الجديدة.
- الجيزة: 6 أكتوبر وكمباونداتها.
- القليوبية ومناطق الخدمة: العبور، العاشر من رمضان، الرحاب، مدينتي، الشروق.
