import streamlit as st

SITE_URL = "https://egyptfilters.streamlit.app"
WHATSAPP = "201009490527"
PHONE = "01024246876"
WHATSAPP_DISPLAY = "01009490527"


def inject_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    *{font-family:Cairo,Tahoma,Arial,sans-serif;direction:rtl} html,body,.stApp,[data-testid='stAppViewContainer'],[data-testid='stMain'],[data-testid='stSidebar']{direction:rtl}
    .stApp{background:#f5fbff;direction:rtl}
    .block-container{max-width:1150px;padding-top:22px}
    .seo-hero{padding:38px 32px;border-radius:28px;background:linear-gradient(135deg,#f8fdff,#e3f6ff);border:1px solid #d9edf6;margin-bottom:26px}
    .seo-hero .badge{color:#0879c9;font-weight:800;font-size:16px}
    .seo-hero h1{font-size:40px;line-height:1.35;color:#063b67;margin:8px 0 12px}
    .seo-hero p{color:#55748a;font-size:18px;line-height:2;margin:0}
    .seo-card{background:#fff;border:1px solid #e5f0f5;border-radius:20px;padding:24px 28px;margin:18px 0;box-shadow:0 10px 30px #063b6710}
    .seo-card h2{color:#063b67;font-size:27px;margin:0 0 10px}
    .seo-card h3{color:#063b67;font-size:21px;margin:14px 0 6px}
    .seo-card p,.seo-card li{color:#55748a;line-height:2;font-size:16px}
    .seo-card ul{padding-right:22px}
    .cta{background:linear-gradient(135deg,#063b67,#0879c9);color:#fff;border-radius:24px;padding:28px;margin:24px 0}
    .cta h2{color:#fff;margin-top:0}.cta p{color:#d9efff;line-height:1.9}
    .footer{text-align:center;color:#688296;padding:28px 0 10px}
    </style>
    """, unsafe_allow_html=True)


def page_header(title, description, badge="💧 المصرية للفلاتر"):
    st.markdown(
        f'''<section class="seo-hero">
        <div class="badge">{badge}</div>
        <h1>{title}</h1>
        <p>{description}</p>
        </section>''',
        unsafe_allow_html=True,
    )


def contact_cta(service="الخدمة المطلوبة"):
    st.markdown(
        f'''<section class="cta">
        <h2>📞 اطلب {service} الآن</h2>
        <p>تواصل مع المصرية للفلاتر لتحديد احتياجك وموعد الخدمة في القاهرة أو الجيزة أو القليوبية.</p>
        <p><b>الهاتف:</b> {PHONE} &nbsp; | &nbsp; <b>واتساب:</b> {WHATSAPP_DISPLAY}</p>
        </section>''',
        unsafe_allow_html=True,
    )
    st.link_button("💬 التواصل عبر واتساب", f"https://wa.me/{WHATSAPP}", use_container_width=True)


def navigation_links():
    st.markdown("### صفحات وخدمات مهمة")

    page_map = st.session_state.get("_navigation_pages", {})

    links = [
        ("🏠 الرئيسية", "home"),
        ("📍 فلاتر مياه في القاهرة", "cairo"),
        ("📍 فلاتر مياه في الجيزة", "giza"),
        ("📍 فلاتر مياه في القليوبية", "qalyubia"),
        ("🔧 تركيب فلاتر المياه", "installation"),
        ("🛠️ صيانة فلاتر المياه", "maintenance"),
        ("💧 تغيير الشمعات", "cartridges"),
        ("🔩 قطع غيار الفلاتر", "spare_parts"),
    ]

    cols = st.columns(3)

    for i, (label, key) in enumerate(links):
        page = page_map.get(key)
        if page is not None:
            with cols[i % 3]:
                st.page_link(page, label=label)

def render_service_page(
    *,
    page_title,
    title,
    description,
    badge,
    card_title,
    intro,
    section_title,
    bullets,
    cta_text,
    footer_text,
    icon="💧",
):
    st.set_page_config(
        page_title=page_title,
        page_icon=icon,
        layout="wide",
    )

    inject_styles()
    page_header(title, description, badge)

    items_html = "".join(f"<li>{item}</li>" for item in bullets)

    st.markdown(
        f'''<section class="seo-card">
        <h2>{card_title}</h2>
        <p>{intro}</p>
        <h3>{section_title}</h3>
        <ul>{items_html}</ul>
        </section>''',
        unsafe_allow_html=True,
    )

    contact_cta(cta_text)
    navigation_links()
    st.markdown(
        f'<div class="footer">{footer_text}</div>',
        unsafe_allow_html=True,
    )

