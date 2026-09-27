import streamlit as st
from seo_utils import inject_styles, page_header, contact_cta, navigation_links

st.set_page_config(page_title="تغيير شمعات فلاتر المياه | المصرية للفلاتر", page_icon="💧", layout="wide")
inject_styles()
page_header("تغيير شمعات فلاتر المياه", "خدمة تغيير شمعات الفلتر ومراجعة مراحل الفلترة حسب نوع الفلتر وحالته ومعدل الاستخدام.", "💧 تغيير شمعات الفلاتر")
st.markdown('''<section class="seo-card"><h2>خدمة تغيير الشمعات</h2><p>الشمعات جزء أساسي من مراحل فلتر المياه، وموعد تغييرها يختلف حسب نوع الفلتر وجودة المياه ومعدل الاستخدام. يمكن فحص حالة المراحل وتحديد الشمعات التي تحتاج إلى استبدال.</p><h3>الخدمة تشمل</h3><ul><li>فحص مراحل الفلتر.</li><li>تحديد الشمعات المطلوب تغييرها.</li><li>استبدال الشمعات المناسبة لنوع الفلتر.</li><li>مراجعة التوصيلات بعد التغيير.</li></ul></section>''', unsafe_allow_html=True)
contact_cta("تغيير شمعات الفلتر")
navigation_links()
