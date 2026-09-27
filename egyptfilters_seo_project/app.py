import streamlit as st

st.set_page_config(
    page_title="المصرية للفلاتر | تركيب وصيانة فلاتر المياه في مصر",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = {
    "الرئيسية": [
        st.Page("home.py", title="المصرية للفلاتر", icon="🏠", default=True),
    ],
    "المناطق": [
        st.Page("pages/01_فلاتر_مياه_القاهرة.py", title="فلاتر مياه في القاهرة", icon="📍", url_path="water-filters-cairo"),
        st.Page("pages/02_فلاتر_مياه_الجيزة.py", title="فلاتر مياه في الجيزة", icon="📍", url_path="water-filters-giza"),
        st.Page("pages/03_فلاتر_مياه_القليوبية.py", title="فلاتر مياه في القليوبية", icon="📍", url_path="water-filters-qalyubia"),
    ],
    "الخدمات": [
        st.Page("pages/04_تركيب_فلاتر_المياه.py", title="تركيب فلاتر المياه", icon="🔧", url_path="water-filter-installation"),
        st.Page("pages/05_صيانة_فلاتر_المياه.py", title="صيانة فلاتر المياه", icon="🛠️", url_path="water-filter-maintenance"),
        st.Page("pages/06_تغيير_شمعات_فلاتر_المياه.py", title="تغيير شمعات الفلاتر", icon="💧", url_path="filter-cartridge-change"),
        st.Page("pages/07_قطع_غيار_فلاتر_المياه.py", title="قطع غيار فلاتر المياه", icon="🔩", url_path="filter-spare-parts"),
    ],
}

pg = st.navigation(pages, position="sidebar")
pg.run()
