import streamlit as st
from seo_utils import inject_styles, page_header, contact_cta, navigation_links

st.set_page_config(page_title="قطع غيار فلاتر المياه | المصرية للفلاتر", page_icon="🔩", layout="wide")
inject_styles()
page_header("قطع غيار فلاتر المياه", "فحص واستبدال قطع الغيار التي تحتاج إلى تغيير ضمن أعمال صيانة وتركيب فلاتر المياه.", "🔩 قطع غيار فلاتر المياه")
st.markdown('''<section class="seo-card"><h2>استبدال قطع غيار الفلاتر</h2><p>عند وجود قطعة تالفة أو مستهلكة في فلتر المياه، يتم فحصها وتحديد البديل المناسب وفق نوع الفلتر والمكون المطلوب. الهدف هو إعادة التشغيل بشكل سليم بعد الاستبدال.</p><h3>متى تحتاج إلى قطعة غيار؟</h3><ul><li>وجود تلف واضح في أحد المكونات.</li><li>تسريب مرتبط بقطعة أو وصلة.</li><li>ضعف أداء جزء من النظام.</li><li>الحاجة إلى استبدال مكون أثناء الصيانة.</li></ul></section>''', unsafe_allow_html=True)
contact_cta("قطع غيار فلتر المياه")
navigation_links()
