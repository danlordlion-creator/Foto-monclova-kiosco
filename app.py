import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
from datetime import datetime

st.set_page_config(page_title="FOTO MONCLOVA", page_icon="📸", layout="centered")

# --- ESTILOS PREMIUM ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@300&display=swap');
.main { background-color: #0a0a0a; }
h1 { font-family: 'Bebas Neue', sans-serif; font-size: 72px !important; text-align: center; color: white !important; letter-spacing: 5px; margin: 0; }
.subtitle { font-family: 'Montserrat', sans-serif; text-align: center; color: #888; letter-spacing: 8px; font-size: 14px; }
.stButton>button { background-color: #E30613 !important; color: white !important; border: none; border-radius: 50px !important; height: 60px; font-family: 'Bebas Neue'; font-size: 22px !important; letter-spacing: 2px; width: 100%; }
.countdown { text-align: center; font-size: 80px; font-family: 'Bebas Neue'; color: #E30613; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>FOTO</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='margin-top:-30px;'>MONCLOVA</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>RECUERDOS EN 15 SEGUNDOS</p>", unsafe_allow_html=True)
st.divider()

col1, col2 = st.columns(2)
filtro = col1.selectbox("Filtro", ["Original", "Blanco y Negro", "Vintage Monclova"])
marco = col2.selectbox("Marco", ["Sin Marco", "Rojo Monclova", "Polaroid"])

img_file = st.camera_input("", label_visibility="collapsed")

if img_file:
    img = Image.open(img_file)
    
    # APLICAR FILTROS
    if filtro == "Blanco y Negro":
        img = img.convert("L").convert("RGB")
    elif filtro == "Vintage Monclova":
        img = img.convert("RGB")
    
    # APLICAR MARCO
    if marco == "Rojo Monclova":
        draw = ImageDraw.Draw(img)
        w, h = img.size
        border = int(w*0.04)
        draw.rectangle([(0,0),(w,h)], outline="#E30613", width=border)
    elif marco == "Polaroid":
        new_h = int(img.height * 1.25)
        polaroid = Image.new("RGB", (img.width, new_h), "white")
        polaroid.paste(img, (0,0))
        draw = ImageDraw.Draw(polaroid)
        try:
            draw.text((20, img.height+10), "Monclova, Coah. - " + datetime.now().strftime("%d/%m/%Y"), fill="black")
        except:
            pass
        img = polaroid

    st.image(img, use_container_width=True)
    st.success("¡Foto lista para imprimir!")
    
    # BOTONES DE ACCION
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    c1, c2 = st.columns(2)
    c1.download_button("📥 GUARDAR", buf.getvalue(), file_name=f"FotoMonclova_{datetime.now().strftime('%H%M%S')}.jpg", mime="image/jpeg", use_container_width=True)
    c2.button("🖨️ IMPRIMIR (Ctrl+P)", use_container_width=True)
    st.balloons()
else:
    st.info("👆 Presiona 'Take photo' para iniciar. Tienes 15 segundos para posar.")

st.markdown("<br><p style='text-align:center; color:#444; font-size:10px;'>KIOSKO V17 PREMIUM • MONCLOVA, COAH</p>", unsafe_allow_html=True)
