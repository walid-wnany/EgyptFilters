import streamlit as st
from seo_utils import inject_styles, navigation_links

st.set_page_config(
    page_title="المصرية للفلاتر | فلاتر مياه وصيانة وتركيب",
    page_icon="💧",
    layout="wide",
)

inject_styles()

st.markdown(
    """
    <section class="seo-hero">
        <div class="badge">💧 المصرية للفلاتر</div>
        <h1>فلاتر مياه وتركيب وصيانة في مصر</h1>
        <p>
            خدمات تركيب وصيانة فلاتر المياه وتغيير الشمعات وقطع الغيار
            في القاهرة والجيزة والقليوبية.
        </p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="seo-card">
        <h2>خدمات المصرية للفلاتر</h2>
        <p>
            تعرف على خدمات تركيب وصيانة فلاتر المياه، تغيير الشمعات،
            وقطع الغيار، واختر الصفحة المناسبة حسب المنطقة أو نوع الخدمة.
        </p>
        <h3>المناطق والخدمات</h3>
        <ul>
            <li>فلاتر مياه في القاهرة والجيزة والقليوبية.</li>
            <li>تركيب فلاتر المياه وضبط التوصيلات.</li>
            <li>صيانة الفلاتر وفحص التسريب وضعف التدفق.</li>
            <li>تغيير الشمعات وقطع الغيار المناسبة.</li>
        </ul>
    </section>
    """,
    unsafe_allow_html=True,
)

navigation_links()

st.markdown(
    '<div class="footer">المصرية للفلاتر — خدمات فلاتر المياه في مصر</div>',
    unsafe_allow_html=True,
)
