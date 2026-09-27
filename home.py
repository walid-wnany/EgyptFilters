import streamlit as st
import urllib.parse
import hashlib
import qrcode
from io import BytesIO

# ---------------- SEO CONFIG ----------------
SITE_URL = "https://egyptfilters.streamlit.app/"
SEO_TITLE = "المصرية للفلاتر | تركيب وصيانة فلاتر المياه في مصر"
SEO_DESCRIPTION = (
    "المصرية للفلاتر لخدمات تركيب وصيانة فلاتر المياه، تغيير الشمعات "
    "واستبدال قطع الغيار بخدمة احترافية وسرعة في الاستجابة."
)

# Streamlit Community Cloud indexes public apps. Keep the primary SEO
# description visible near the top because search engines can use visible
# headers/text as page context.
st.markdown(
    """
    <header class="seo-top" aria-label="المصرية للفلاتر">
      <h1>المصرية للفلاتر – تركيب وصيانة فلاتر المياه في مصر</h1>
      <p>
        تركيب وصيانة فلاتر المياه، تغيير الشمعات واستبدال قطع الغيار
        بخدمة احترافية وسرعة في الاستجابة.
      </p>
    </header>
    """,
    unsafe_allow_html=True,
)

# عدّل البيانات دي فقط
WHATSAPP = "201009490527"   # 01009490527 بصيغة واتساب الدولية بدون + أو مسافات
WHATSAPP_DISPLAY = "01009490527"
PHONE = "01024246876"



def make_customer_id(name, phone):
    raw = f"{name.strip()}|{phone.strip()}".encode("utf-8")
    return "MF-" + hashlib.sha256(raw).hexdigest()[:8].upper()

def make_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');
*{font-family:Cairo,Tahoma,Arial,sans-serif}
.stApp{background:#f5fbff;direction:rtl}
.block-container{max-width:1150px;padding-top:18px}
.header{background:#fff;padding:15px 22px;border-radius:18px;border:1px solid #e4f0f6;margin-bottom:22px}
.brand{font-size:27px;font-weight:800;color:#063b67}
.brand span{font-size:13px;color:#688296}
.hero{padding:48px 38px;border-radius:30px;background:linear-gradient(135deg,#f8fdff,#e3f6ff);border:1px solid #d9edf6}
.badge{color:#0879c9;font-weight:800;font-size:17px}
.hero h1{font-size:52px;line-height:1.25;color:#063b67;margin:8px 0}
.hero h1 span{color:#0879c9}.hero p{color:#55748a;font-size:18px;line-height:2}
.water-image img{border-radius:30px;box-shadow:0 18px 45px #063b6718}
.title{text-align:center;color:#063b67;font-size:32px;font-weight:800;margin-top:55px}
.subtitle{text-align:center;color:#688296;margin-bottom:28px}
.card{background:#fff;border:1px solid #e5f0f5;border-radius:20px;padding:25px;min-height:195px;box-shadow:0 12px 35px #063b6710}
.icon{font-size:32px}.card h3{color:#063b67}.card p{color:#617d8f;line-height:1.9}
.feature{background:#f0faff;border-radius:13px;padding:12px 16px;margin:9px 0;color:#34576e}
.stat{background:#effaff;border-radius:17px;padding:20px;text-align:center;margin-bottom:13px}
.stat strong{display:block;color:#0879c9;font-size:29px}
.contact{margin-top:50px;padding:35px;border-radius:28px;background:linear-gradient(135deg,#063b67,#0879c9);color:#fff}
.contact h2{color:#fff}.contact p{color:#d9efff}
.wa{display:inline-block;background:#16b75a;color:#fff!important;text-decoration:none;padding:11px 20px;border-radius:12px;font-weight:800}
.footer{text-align:center;color:#688296;padding:30px 0 10px}
.seo-top{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.seo-section{background:#fff;border:1px solid #e5f0f5;border-radius:20px;padding:24px 28px;margin:24px 0}
.seo-section h2,.faq h2{color:#063b67;font-size:27px;margin:0 0 10px}
.seo-section p{color:#55748a;line-height:2;font-size:16px;margin:0}
.faq{margin-top:48px;background:#fff;border:1px solid #e5f0f5;border-radius:22px;padding:28px}
.faq details{border-top:1px solid #e5f0f5;padding:16px 0}
.faq details:first-of-type{border-top:0}
.faq summary{cursor:pointer;color:#063b67;font-weight:800;font-size:17px}
.faq details p{color:#55748a;line-height:1.9;margin:10px 0 0}
</style>
""", unsafe_allow_html=True)

st.markdown('<header class="header"><div class="brand">💧 المصرية للفلاتر <span>— نقاء يستحق الثقة</span></div></header>', unsafe_allow_html=True)

left, right = st.columns([1.15,.85], gap="large")
with left:
    st.markdown("""<div class="hero"><div class="badge">💧 متخصصون في فلاتر المياه</div>
    <h1>مياه أنقى…<br><span>وحياة أفضل</span></h1>
    <p>تركيب وصيانة فلاتر المياه، تغيير الشمعات وقطع الغيار بخدمة احترافية واهتمام بكل التفاصيل.</p></div>""", unsafe_allow_html=True)
with right:
    st.image("water_logo.png", caption="المصرية للفلاتر - خدمات فلاتر المياه", use_container_width=True)

st.markdown(
    """
    <section class="seo-section" aria-labelledby="about-filters">
      <h2 id="about-filters">فلاتر المياه في مصر</h2>
      <p>
        إذا كنت تبحث عن تركيب فلتر مياه أو صيانة فلتر المياه أو تغيير الشمعات،
        تقدم المصرية للفلاتر خدمات الفحص والتركيب والصيانة واستبدال قطع الغيار.
        يمكنك إرسال طلب الخدمة مباشرة من خلال النموذج أو التواصل عبر الهاتف وواتساب.
      </p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h2 class="title">خدمات تركيب وصيانة فلاتر المياه</h2><div class="subtitle">كل ما يحتاجه فلتر المياه في مكان واحد</div>', unsafe_allow_html=True)
services=[("🔧","تركيب فلاتر المياه","تركيب احترافي وضبط التوصيلات والتأكد من التشغيل بشكل سليم."),
("🛠️","صيانة وإصلاح","فحص الأعطال وتسريب المياه وضعف الضغط واستبدال القطع اللازمة."),
("💧","تغيير الشمعات","تغيير الشمعات ومتابعة مراحل الفلترة للحفاظ على كفاءة الفلتر.")]
cols=st.columns(3)
for col,(icon,title,text) in zip(cols,services):
    with col:
        st.markdown(f'<div class="card"><div class="icon">{icon}</div><h3>{title}</h3><p>{text}</p></div>',unsafe_allow_html=True)

st.markdown('<h2 class="title">لماذا تختار المصرية للفلاتر؟</h2><div class="subtitle">نهتم بالتفاصيل من أول مكالمة لحد انتهاء الخدمة.</div>',unsafe_allow_html=True)
a,b=st.columns(2)
with a:
    for x in ["✓ فنيون متخصصون وخدمة احترافية","✓ مواعيد مرنة وسرعة في الاستجابة","✓ قطع غيار وشمعات مناسبة لنوع الفلتر","✓ متابعة بعد الخدمة عند الحاجة"]:
        st.markdown(f'<div class="feature">{x}</div>',unsafe_allow_html=True)
with b:
    x,y=st.columns(2)
    with x:
        st.markdown('<div class="stat"><strong>+500</strong>عميل مخدوم</div><div class="stat"><strong>7/7</strong>أيام خدمة</div>',unsafe_allow_html=True)
    with y:
        st.markdown('<div class="stat"><strong>+1000</strong>عملية صيانة وتركيب</div><div class="stat"><strong>100%</strong>اهتمام بالعميل</div>',unsafe_allow_html=True)

st.markdown(f'<div class="contact"><h2>📞 اطلب خدمة الآن</h2><p>املأ البيانات وسنتواصل معك لتأكيد موعد الخدمة.</p><p><b>الهاتف:</b> {PHONE} &nbsp; | &nbsp; <b>واتساب:</b> {WHATSAPP_DISPLAY}</p></div>',unsafe_allow_html=True)

with st.form("service_form"):
    st.subheader("📝 طلب خدمة")
    c1,c2=st.columns(2)
    with c1: name=st.text_input("الاسم *",placeholder="اكتب اسمك")
    with c2: phone=st.text_input("رقم الهاتف *",placeholder="01xxxxxxxxx")
    service=st.selectbox("نوع الخدمة",["تركيب فلتر مياه","صيانة فلتر","تغيير شمعات","استبدال قطع غيار","استفسار"])
    details=st.text_area("تفاصيل الطلب",placeholder="اكتب أي تفاصيل تساعدنا...")
    send=st.form_submit_button("💬 إرسال الطلب عبر واتساب",use_container_width=True)

if send:
    if not name.strip() or not phone.strip():
        st.error("من فضلك اكتب الاسم ورقم الهاتف.")
    else:
        message=f"""طلب خدمة - المصرية للفلاتر
الاسم: {name}
الهاتف: {phone}
الخدمة: {service}
التفاصيل: {details}"""
        url="https://wa.me/"+WHATSAPP+"?text="+urllib.parse.quote(message)
        st.success("تم تجهيز الطلب.")
        st.markdown(f'<a class="wa" href="{url}" target="_blank">💬 فتح واتساب</a>',unsafe_allow_html=True)

        customer_id = make_customer_id(name, phone)
        qr_data = f"""المصرية للفلاتر
رقم العميل: {customer_id}
الاسم: {name}
الهاتف: {phone}
الخدمة: {service}"""
        qr_image = make_qr(qr_data)

        st.markdown(
            f"""<div style="margin-top:25px;padding:25px;background:#f0faff;border-radius:20px;text-align:center;border:1px solid #d9edf6">
            <h3 style="color:#063b67;margin-bottom:5px">📱 باركود العميل</h3>
            <div style="font-size:24px;font-weight:800;color:#0879c9">{customer_id}</div>
            <p style="color:#688296">احتفظ بهذا الرقم والباركود لتمييز العميل في كل زيارة.</p>
            </div>""",
            unsafe_allow_html=True
        )
        st.image(qr_image, caption=f"QR العميل {customer_id}", width=240)
        st.download_button(
            "⬇️ تحميل باركود العميل",
            data=qr_image.getvalue(),
            file_name=f"{customer_id}.png",
            mime="image/png",
            use_container_width=True
        )


st.markdown("### 📍 المناطق والخدمات")
nav_cols = st.columns(3)
nav_items = [
    ("📍 فلاتر مياه في القاهرة", "pages/01_فلاتر_مياه_القاهرة.py"),
    ("📍 فلاتر مياه في الجيزة", "pages/02_فلاتر_مياه_الجيزة.py"),
    ("📍 فلاتر مياه في القليوبية", "pages/03_فلاتر_مياه_القليوبية.py"),
    ("🔧 تركيب فلاتر المياه", "pages/04_تركيب_فلاتر_المياه.py"),
    ("🛠️ صيانة فلاتر المياه", "pages/05_صيانة_فلاتر_المياه.py"),
    ("💧 تغيير الشمعات", "pages/06_تغيير_شمعات_فلاتر_المياه.py"),
    ("🔩 قطع غيار الفلاتر", "pages/07_قطع_غيار_فلاتر_المياه.py"),
]
for i, (label, path) in enumerate(nav_items):
    with nav_cols[i % 3]:
        st.page_link(path, label=label, use_container_width=True)

st.markdown(
    """
    <section class="faq" aria-labelledby="faq-title">
      <h2 id="faq-title">أسئلة شائعة عن فلاتر المياه</h2>

      <details>
        <summary>ما الخدمات التي تقدمها المصرية للفلاتر؟</summary>
        <p>تركيب فلاتر المياه، صيانة وإصلاح الأعطال، تغيير الشمعات واستبدال قطع الغيار.</p>
      </details>

      <details>
        <summary>هل يمكن طلب الخدمة عبر واتساب؟</summary>
        <p>نعم، يمكنك إرسال بيانات الطلب من النموذج وسيتم تجهيز رسالة واتساب للتواصل.</p>
      </details>

      <details>
        <summary>متى تحتاج شمعات الفلتر إلى التغيير؟</summary>
        <p>يعتمد ذلك على نوع الفلتر وجودة المياه ومعدل الاستخدام؛ يمكن فحص الفلتر وتحديد ما يحتاج إلى استبدال.</p>
      </details>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="footer">© 2026 المصرية للفلاتر — تركيب وصيانة فلاتر المياه</div>',unsafe_allow_html=True)
