import streamlit as st
from seo_utils import inject_styles, page_header, contact_cta, navigation_links

st.set_page_config(page_title="فلاتر مياه في الجيزة | المصرية للفلاتر", page_icon="💧", layout="wide")
inject_styles()
page_header("فلاتر مياه في الجيزة", "خدمات فحص وتركيب وصيانة فلاتر المياه وتغيير الشمعات وقطع الغيار في الجيزة.", "📍 خدمات فلاتر المياه في الجيزة")

st.markdown('''<section class="seo-card"><h2>خدمات فلاتر المياه في الجيزة</h2><p>إذا كان فلتر المياه يحتاج إلى تركيب أو صيانة أو تغيير شمعات، يمكنك التواصل مع المصرية للفلاتر وشرح نوع الخدمة المطلوبة. يتم تحديد احتياج الفلتر بناءً على حالته ونوعه وتفاصيل العطل أو الخدمة.</p><h3>متى تطلب الصيانة؟</h3><ul><li>وجود تسريب أو ضعف في تدفق المياه.</li><li>الحاجة إلى تغيير الشمعات.</li><li>وجود جزء يحتاج إلى استبدال.</li><li>تركيب فلتر جديد أو إعادة ضبط التوصيلات.</li></ul></section>''', unsafe_allow_html=True)
contact_cta("خدمة فلاتر المياه في الجيزة")
navigation_links()
st.markdown('<div class="footer">المصرية للفلاتر — خدمات فلاتر المياه في الجيزة</div>', unsafe_allow_html=True)
