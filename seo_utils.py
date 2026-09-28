import base64
from pathlib import Path
import streamlit as st

SITE_URL = "https://flatermasr.com"
WHATSAPP = "201009490527"
PHONE = "01024246876"
WHATSAPP_DISPLAY = "01009490527"
LOGO_PATH = Path(__file__).parent / "assets" / "logo.png"
LOGO = "assets/logo.png"


def _logo_data_uri():
    try:
        encoded = base64.b64encode(LOGO_PATH.read_bytes()).decode("ascii")
        return f"data:image/png;base64,{encoded}"
    except Exception:
        return ""


def inject_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&display=swap');
        html, body, .stApp, [data-testid='stAppViewContainer'], [data-testid='stMain'], [data-testid='stSidebar'], [data-testid='stHeader'] {
            direction:rtl !important;
            font-family:Cairo,Tahoma,Arial,sans-serif !important;
        }
        * { box-sizing:border-box; }
        .stApp { background:#f5fbff; }
        .block-container { max-width:1150px; padding-top:22px; padding-bottom:40px; }
        .seo-hero { padding:34px 30px; border-radius:28px; background:linear-gradient(135deg,#f8fdff,#e3f6ff); border:1px solid #d9edf6; margin-bottom:26px; text-align:right; }
        .hero-logo { width:105px; max-width:30vw; border-radius:50%; box-shadow:0 10px 30px rgba(6,59,103,.15); margin-bottom:12px; }
        .seo-hero .badge { color:#0879c9; font-weight:800; font-size:16px; }
        .seo-hero h1 { font-size:40px; line-height:1.35; color:#063b67; margin:8px 0 12px; }
        .seo-hero p { color:#55748a; font-size:18px; line-height:2; margin:0; }
        .seo-card { background:#fff; border:1px solid #e5f0f5; border-radius:20px; padding:24px 28px; margin:18px 0; box-shadow:0 10px 30px rgba(6,59,103,.06); text-align:right; }
        .seo-card h2,.seo-card h3 { color:#063b67; }
        .seo-card h2 { font-size:27px; margin:0 0 10px; }
        .seo-card h3 { font-size:21px; margin:14px 0 6px; }
        .seo-card p,.seo-card li { color:#55748a; line-height:2; font-size:16px; }
        .seo-card ul { padding-right:22px; padding-left:0; }
        .cta { background:linear-gradient(135deg,#063b67,#0879c9); color:#fff; border-radius:24px; padding:28px; margin:24px 0; text-align:right; }
        .cta h2 { color:#fff; margin-top:0; }
        .cta p { color:#d9efff; line-height:1.9; }
        .footer { text-align:center; color:#688296; padding:28px 0 10px; }
        .contact-pill { display:inline-block; margin:5px 4px; padding:8px 14px; border-radius:999px; background:#e8f7ff; color:#063b67; font-weight:700; }
        [data-testid='stSidebar'] { border-left:1px solid #dceef7; border-right:0; }
        [data-testid='stSidebar'] * { text-align:right !important; }
        [data-testid='stSidebarNav'], [data-testid='stSidebarNav'] ul, [data-testid='stSidebarNav'] a { direction:rtl !important; }
        [data-testid='stSidebarNav'] ul { padding-right:0 !important; }
        [data-testid='column'], .stHorizontalBlock { direction:rtl !important; }
        button, [role='button'], input, textarea, select { direction:rtl !important; }
        input, textarea { text-align:right !important; }
        .area-card { background:#f8fdff; border:1px solid #dceef7; border-radius:18px; padding:18px; margin:8px 0; min-height:120px; }
        .area-card h3 { color:#063b67; margin:0 0 8px; font-size:20px; }
        .area-card ul { margin:0; padding-right:20px; }
        .area-card li { color:#55748a; line-height:1.9; }
        .brand-box { text-align:center; padding:8px 4px 18px; border-bottom:1px solid #dceef7; margin-bottom:14px; }
        .brand-box img { width:150px; max-width:80%; border-radius:50%; display:block; margin:0 auto 8px; box-shadow:0 8px 24px rgba(3,77,125,.15); }
        .brand-title { color:#063b67; font-weight:800; font-size:18px; }
        .brand-subtitle { color:#0879c9; font-size:12px; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    logo_uri = _logo_data_uri()
    if logo_uri:
        st.sidebar.markdown(
            f'''<div class="brand-box">
                <img src="{logo_uri}" alt="المصرية للفلاتر">
                <div class="brand-title">المصرية للفلاتر</div>
                <div class="brand-subtitle">مياه نقية.. لحياة أفضل</div>
            </div>''',
            unsafe_allow_html=True,
        )


def page_header(title, description, badge="💧 المصرية للفلاتر"):
    logo_uri = _logo_data_uri()
    logo_html = f'<img class="hero-logo" src="{logo_uri}" alt="المصرية للفلاتر">' if logo_uri else ""
    st.markdown(
        f'''<section class="seo-hero">
        {logo_html}
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
        <p><span class="contact-pill">الهاتف: {PHONE}</span><span class="contact-pill">واتساب: {WHATSAPP_DISPLAY}</span></p>
        </section>''',
        unsafe_allow_html=True,
    )
    st.link_button("💬 التواصل عبر واتساب", f"https://wa.me/{WHATSAPP}", use_container_width=True)


def navigation_links():
    st.markdown("### صفحات وخدمات مهمة")
    page_map = st.session_state.get("_navigation_pages", {})
    links = [
        ("🏠 الرئيسية", "home"),
        ("🗺️ المناطق المخدومة", "areas"),
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


def render_service_page(*, page_title, title, description, badge, card_title, intro, section_title, bullets, cta_text, footer_text, icon="💧"):
    st.set_page_config(page_title=page_title, page_icon=LOGO, layout="wide")
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
    st.markdown(f'<div class="footer">{footer_text}</div>', unsafe_allow_html=True)
