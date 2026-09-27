import streamlit as st
import urllib.parse
import hashlib
import qrcode
from io import BytesIO

st.set_page_config(page_title="المصرية للفلاتر", page_icon="💧", layout="wide")

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
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><div class="brand">💧 المصرية للفلاتر <span>— نقاء يستحق الثقة</span></div></div>', unsafe_allow_html=True)

left, right = st.columns([1.15,.85], gap="large")
with left:
    st.markdown("""<div class="hero"><div class="badge">💧 متخصصون في فلاتر المياه</div>
    <h1>مياه أنقى…<br><span>وحياة أفضل</span></h1>
    <p>تركيب وصيانة فلاتر المياه، تغيير الشمعات وقطع الغيار بخدمة احترافية واهتمام بكل التفاصيل.</p></div>""", unsafe_allow_html=True)
with right:
    st.image("water_logo.png", use_container_width=True)

st.markdown('<div class="title">خدماتنا</div><div class="subtitle">كل ما يحتاجه فلتر المياه في مكان واحد</div>', unsafe_allow_html=True)
services=[("🔧","تركيب فلاتر المياه","تركيب احترافي وضبط التوصيلات والتأكد من التشغيل بشكل سليم."),
("🛠️","صيانة وإصلاح","فحص الأعطال وتسريب المياه وضعف الضغط واستبدال القطع اللازمة."),
("💧","تغيير الشمعات","تغيير الشمعات ومتابعة مراحل الفلترة للحفاظ على كفاءة الفلتر.")]
cols=st.columns(3)
for col,(icon,title,text) in zip(cols,services):
    with col:
        st.markdown(f'<div class="card"><div class="icon">{icon}</div><h3>{title}</h3><p>{text}</p></div>',unsafe_allow_html=True)

st.markdown('<div class="title">ليه تختار المصرية للفلاتر؟</div><div class="subtitle">نهتم بالتفاصيل من أول مكالمة لحد انتهاء الخدمة.</div>',unsafe_allow_html=True)
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

st.markdown('<div class="footer">© 2026 المصرية للفلاتر — تركيب وصيانة فلاتر المياه</div>',unsafe_allow_html=True)
