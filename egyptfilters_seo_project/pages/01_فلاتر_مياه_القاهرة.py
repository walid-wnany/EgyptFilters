import streamlit as st
from seo_utils import inject_styles, page_header, contact_cta, navigation_links

st.set_page_config(page_title="فلاتر مياه في القاهرة | المصرية للفلاتر", page_icon="💧", layout="wide")
inject_styles()
page_header("فلاتر مياه في القاهرة", "خدمات تركيب وصيانة فلاتر المياه وتغيير الشمعات وقطع الغيار للعملاء في القاهرة.", "📍 خدمات فلاتر المياه في القاهرة")

st.markdown('''<section class="seo-card"><h2>تركيب وصيانة فلاتر المياه في القاهرة</h2><p>تقدم المصرية للفلاتر خدمات فحص وتركيب وصيانة فلاتر المياه، مع تغيير الشمعات واستبدال قطع الغيار عند الحاجة. يمكن إرسال طلب الخدمة مباشرة للتنسيق وتحديد التفاصيل.</p><h3>الخدمات المتاحة</h3><ul><li>تركيب فلاتر المياه وضبط التوصيلات.</li><li>فحص الأعطال والتسريب وضعف ضغط المياه.</li><li>تغيير شمعات الفلتر حسب حالتها ونوع النظام.</li><li>استبدال قطع الغيار المناسبة للفلتر.</li></ul></section>''', unsafe_allow_html=True)
contact_cta("خدمة فلاتر المياه في القاهرة")
navigation_links()
st.markdown('<div class="footer">المصرية للفلاتر — خدمات فلاتر المياه في القاهرة</div>', unsafe_allow_html=True)
