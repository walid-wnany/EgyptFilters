import streamlit as st

SITE_URL = "https://egyptfilters.streamlit.app"
WHATSAPP = "201009490527"
PHONE = "01024246876"
WHATSAPP_DISPLAY = "01009490527"


def inject_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
    *{font-family:Cairo,Tahoma,Arial,sans-serif}
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
    cols = st.columns(3)
    links = [
        ("🏠 الرئيسية", "app.py"),
        ("📍 فلاتر مياه في القاهرة", "pages/01_فلاتر_مياه_القاهرة.py"),
        ("📍 فلاتر مياه في الجيزة", "pages/02_فلاتر_مياه_الجيزة.py"),
        ("📍 فلاتر مياه في القليوبية", "pages/03_فلاتر_مياه_القليوبية.py"),
        ("🔧 تركيب فلاتر المياه", "pages/04_تركيب_فلاتر_المياه.py"),
        ("🛠️ صيانة فلاتر المياه", "pages/05_صيانة_فلاتر_المياه.py"),
        ("💧 تغيير الشمعات", "pages/06_تغيير_شمعات_فلاتر_المياه.py"),
        ("🔩 قطع غيار الفلاتر", "pages/07_قطع_غيار_فلاتر_المياه.py"),
    ]
    for i, (label, path) in enumerate(links):
        with cols[i % 3]:
            st.page_link(path, label=label)
