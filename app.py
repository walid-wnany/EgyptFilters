import streamlit as st

st.set_page_config(
    page_title="المصرية للفلاتر | تركيب وصيانة فلاتر المياه في مصر",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# تطبيق اتجاه RTL على التطبيق بالكامل، بما في ذلك الشريط الجانبي وكل الصفحات.
st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], .stApp {
        direction: rtl !important;
    }

    [data-testid="stSidebar"] {
        direction: rtl !important;
    }

    [data-testid="stSidebar"] * {
        text-align: right;
    }

    [data-testid="stMain"] {
        direction: rtl !important;
    }

    .stHorizontalBlock {
        direction: rtl !important;
    }

    .stMarkdown, .stText, .stCaption,
    .stSelectbox, .stMultiSelect, .stTextInput,
    .stNumberInput, .stTextArea {
        direction: rtl !important;
    }

    /* الحفاظ على محاذاة الأيقونات والأزرار بشكل مريح في RTL */
    button, [role="button"] {
        direction: rtl;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# تعريف الصفحات مرة واحدة كـ st.Page objects
home = st.Page(
    "home.py",
    title="المصرية للفلاتر",
    icon="🏠",
    default=True,
)

cairo = st.Page(
    "pages/01_فلاتر_مياه_القاهرة.py",
    title="فلاتر مياه في القاهرة",
    icon="📍",
    url_path="water-filters-cairo",
)

giza = st.Page(
    "pages/02_فلاتر_مياه_الجيزة.py",
    title="فلاتر مياه في الجيزة",
    icon="📍",
    url_path="water-filters-giza",
)

qalyubia = st.Page(
    "pages/03_فلاتر_مياه_القليوبية.py",
    title="فلاتر مياه في القليوبية",
    icon="📍",
    url_path="water-filters-qalyubia",
)

installation = st.Page(
    "pages/04_تركيب_فلاتر_المياه.py",
    title="تركيب فلاتر المياه",
    icon="🔧",
    url_path="water-filter-installation",
)

maintenance = st.Page(
    "pages/05_صيانة_فلاتر_المياه.py",
    title="صيانة فلاتر المياه",
    icon="🛠️",
    url_path="water-filter-maintenance",
)

cartridges = st.Page(
    "pages/06_تغيير_شمعات_فلاتر_المياه.py",
    title="تغيير شمعات الفلاتر",
    icon="💧",
    url_path="filter-cartridge-change",
)

spare_parts = st.Page(
    "pages/07_قطع_غيار_فلاتر_المياه.py",
    title="قطع غيار فلاتر المياه",
    icon="🔩",
    url_path="filter-spare-parts",
)

pages = {
    "الرئيسية": [home],
    "المناطق": [cairo, giza, qalyubia],
    "الخدمات": [
        installation,
        maintenance,
        cartridges,
        spare_parts,
    ],
}

# حفظ نفس Page objects لاستخدامها في الروابط الداخلية.
st.session_state["_navigation_pages"] = {
    "home": home,
    "cairo": cairo,
    "giza": giza,
    "qalyubia": qalyubia,
    "installation": installation,
    "maintenance": maintenance,
    "cartridges": cartridges,
    "spare_parts": spare_parts,
}

pg = st.navigation(pages, position="sidebar")
pg.run()
