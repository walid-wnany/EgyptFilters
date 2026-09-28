import streamlit as st
from seo_utils import inject_styles, page_header, contact_cta, navigation_links, LOGO

st.set_page_config(page_title="مناطق خدمة فلاتر المياه | المصرية للفلاتر", page_icon=LOGO, layout="wide")
inject_styles()

page_header(
    "مناطق خدمة المصرية للفلاتر",
    "اختر منطقتك للوصول إلى خدمات فلاتر المياه والتركيب والصيانة وتغيير الشمعات وقطع الغيار.",
    "📍 مناطق الخدمة",
)

regions = [
    {"title": "القاهرة", "icon": "🏙️", "areas": [
        ("15 مايو", ["50 فدان", "120 فدان", "290 فدان"]),
        ("القاهرة الجديدة", ["القاهرة الجديدة"]),
    ]},
    {"title": "الجيزة", "icon": "📍", "areas": [
        ("6 أكتوبر", ["مدينة 6 أكتوبر", "كمباوندات 6 أكتوبر"]),
    ]},
    {"title": "القليوبية ومناطق الخدمة", "icon": "📌", "areas": [
        ("العبور", ["مدينة العبور"]),
        ("العاشر من رمضان", ["العاشر من رمضان"]),
        ("الرحاب", ["مدينة الرحاب"]),
        ("مدينتي", ["مدينتي"]),
        ("الشروق", ["مدينة الشروق"]),
    ]},
]

for region in regions:
    st.markdown(f'<section class="seo-card"><h2>{region["icon"]} {region["title"]}</h2>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, (area, subareas) in enumerate(region["areas"]):
        with cols[i % 2]:
            sub_html = "".join(f"<li>{x}</li>" for x in subareas)
            st.markdown(f"""
                <div class="area-card">
                    <h3>📍 {area}</h3>
                    <ul>{sub_html}</ul>
                </div>
            """, unsafe_allow_html=True)
    st.markdown("</section>", unsafe_allow_html=True)

st.markdown("""
<section class="seo-card">
<h2>💧 جميع خدماتنا متاحة حسب المنطقة</h2>
<p>تركيب فلاتر المياه، صيانة الفلاتر، تغيير الشمعات، وقطع الغيار. اختر المنطقة الأقرب لك ثم تواصل معنا لتحديد الخدمة والموعد.</p>
</section>
""", unsafe_allow_html=True)

contact_cta("الخدمة في منطقتك")
navigation_links()
st.markdown('<div class="footer">المصرية للفلاتر — خدمة فلاتر المياه حسب المناطق — flatermasr.com</div>', unsafe_allow_html=True)
