import streamlit as st
from seo_utils import inject_styles, page_header, contact_cta, navigation_links

st.set_page_config(page_title="تركيب فلاتر المياه | المصرية للفلاتر", page_icon="🔧", layout="wide")
inject_styles()
page_header("تركيب فلاتر المياه", "خدمة تركيب فلاتر المياه وضبط التوصيلات والتأكد من التشغيل السليم في القاهرة والجيزة والقليوبية.", "🔧 تركيب فلاتر المياه")
st.markdown('''<section class="seo-card"><h2>خدمة تركيب فلتر المياه</h2><p>يشمل تركيب فلتر المياه تجهيز التوصيلات المناسبة، تركيب المراحل والأجزاء، مراجعة نقاط الربط والتأكد من عدم وجود تسريب وتشغيل النظام بالشكل الصحيح.</p><h3>قبل التركيب</h3><ul><li>تحديد نوع الفلتر ومكوناته.</li><li>مراجعة مكان التركيب والتوصيلات المتاحة.</li><li>تحديد القطع أو المستلزمات المطلوبة عند الحاجة.</li></ul></section>''', unsafe_allow_html=True)
contact_cta("تركيب فلتر المياه")
navigation_links()
