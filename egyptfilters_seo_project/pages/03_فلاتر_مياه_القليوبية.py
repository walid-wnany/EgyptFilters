import streamlit as st
from seo_utils import inject_styles, page_header, contact_cta, navigation_links

st.set_page_config(page_title="فلاتر مياه في القليوبية | المصرية للفلاتر", page_icon="💧", layout="wide")
inject_styles()
page_header("فلاتر مياه في القليوبية", "خدمات تركيب وصيانة فلاتر المياه وتغيير الشمعات وقطع الغيار في القليوبية.", "📍 خدمات فلاتر المياه في القليوبية")

st.markdown('''<section class="seo-card"><h2>تركيب وصيانة فلاتر المياه في القليوبية</h2><p>المصرية للفلاتر توفر خدمات فلاتر المياه للعملاء في القليوبية، بداية من تركيب الفلتر وفحص التوصيلات وحتى الصيانة وتغيير الشمعات وقطع الغيار المطلوبة.</p><h3>الخدمات</h3><ul><li>تركيب فلتر مياه جديد.</li><li>صيانة وإصلاح مشاكل الفلتر.</li><li>تغيير شمعات مراحل الفلترة.</li><li>استبدال القطع التي تحتاج إلى تغيير.</li></ul></section>''', unsafe_allow_html=True)
contact_cta("خدمة فلاتر المياه في القليوبية")
navigation_links()
st.markdown('<div class="footer">المصرية للفلاتر — خدمات فلاتر المياه في القليوبية</div>', unsafe_allow_html=True)
