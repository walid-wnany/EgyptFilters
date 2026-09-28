import streamlit as st
from seo_utils import inject_styles, navigation_links, page_header, contact_cta, LOGO

st.set_page_config(
    page_title="المصرية للفلاتر | فلاتر مياه وصيانة وتركيب",
    page_icon=LOGO,
    layout="wide",
)

inject_styles()
page_header(
    "فلاتر مياه وتركيب وصيانة في مصر",
    "خدمات تركيب وصيانة فلاتر المياه وتغيير الشمعات وقطع الغيار في القاهرة والجيزة والقليوبية.",
    "💧 المصرية للفلاتر",
)

st.markdown(
    """
    <section class="seo-card">
        <h2>خدمات المصرية للفلاتر</h2>
        <p>تعرف على خدمات تركيب وصيانة فلاتر المياه، تغيير الشمعات، وقطع الغيار، واختر الصفحة المناسبة حسب المنطقة أو نوع الخدمة.</p>
        <h3>مناطق الخدمة</h3>
        <ul>
            <li><strong>القاهرة:</strong> 15 مايو (50 فدان، 120 فدان، 290 فدان) والقاهرة الجديدة.</li>
            <li><strong>الجيزة:</strong> 6 أكتوبر وكمباونداتها.</li>
            <li><strong>القليوبية ومناطق الخدمة:</strong> العبور، العاشر من رمضان، الرحاب، مدينتي، والشروق.</li>
        </ul>
        <h3>الخدمات</h3>
        <ul>
            <li>تركيب فلاتر المياه وضبط التوصيلات.</li>
            <li>صيانة الفلاتر وفحص التسريب وضعف التدفق.</li>
            <li>تغيير الشمعات وقطع الغيار المناسبة.</li>
        </ul>
    </section>
    """,
    unsafe_allow_html=True,
)

contact_cta("الخدمة المطلوبة")
navigation_links()
st.markdown('<div class="footer">المصرية للفلاتر — خدمات فلاتر المياه في مصر — flatermasr.com</div>', unsafe_allow_html=True)
