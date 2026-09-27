import streamlit as st
from seo_utils import inject_styles, page_header, contact_cta, navigation_links

st.set_page_config(page_title="صيانة فلاتر المياه | المصرية للفلاتر", page_icon="🛠️", layout="wide")
inject_styles()
page_header("صيانة فلاتر المياه", "فحص وإصلاح مشاكل فلاتر المياه مثل التسريب وضعف التدفق والحاجة إلى استبدال بعض المكونات.", "🛠️ صيانة فلاتر المياه")
st.markdown('''<section class="seo-card"><h2>فحص وصيانة فلتر المياه</h2><p>تبدأ الصيانة بفحص حالة الفلتر والتوصيلات ومراحل الفلترة وتحديد الجزء الذي يحتاج إلى تنظيف أو تغيير أو إصلاح. تختلف الصيانة المطلوبة حسب نوع الفلتر وحالته ومعدل الاستخدام.</p><h3>مشاكل يمكن فحصها</h3><ul><li>تسريب المياه من التوصيلات.</li><li>ضعف تدفق المياه.</li><li>مشاكل بعض مراحل الفلترة.</li><li>الحاجة إلى تغيير الشمعات أو قطع الغيار.</li></ul></section>''', unsafe_allow_html=True)
contact_cta("صيانة فلتر المياه")
navigation_links()
