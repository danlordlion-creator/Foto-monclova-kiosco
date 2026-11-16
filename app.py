import streamlit as st
from PIL import Image, ImageDraw
import io
from datetime import datetime

st.set_page_config(page_title="FOTO MONCLOVA KIOSKO", page_icon="📸", layout="centered")

# --- ESTILO CHINGON ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@300;600&display=swap');
.stApp { background-color: #050505; }
h1 { font-family: 'Bebas Neue'; font-size: 75px !important; text-align:center; color:white !important; margin:0; line-height:0.9; }
.subtitle { font-family: 'Montserrat'; text-align:center; color:#888; letter-spacing:8px; font-size:13px; margin-bottom:20px; }
.stButton>button { background:#E30613 !important; color:white !important; border-radius:50px !important; height:65px; font-family:'Bebas Neue'; font-size:26px !important; letter-spacing:2px; border:none; }
.price-tag { text-align:center; font-family:'Bebas Neue'; font-size:90px; color:white; margin:10px 0; }
.demo-badge { text-align:center; background:#1a1a1a; color:#FFD700; padding:8px; border-radius:20px; font-family:Montserrat; font-size:11px; letter-spacing:2px; }
.config-box { background:#111; border:1px solid #222; border-radius:15px; padding:15px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='color:#E30613;'>FOTO</h1>", unsafe_allow_html=True)
st.markdown("<h1>MONCLOVA</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>RECUERDOS EN 15 SEGUNDOS</p>", unsafe_allow_html=True)
st.markdown("<div class='demo-badge'>MODO DEMO • EN ESPERA DE TERMINAL POINT SMART</div>", unsafe_allow_html=True)

# --- CONFIGURACION OCULTA (SIMULACION DE LOS 5 TOQUES) ---
with st.expander("⚙️ CONFIGURACION (5 toques + hold 5s en version Windows)"):
    c1, c2 = st.columns(2)
    precio = c1.number_input("Precio", value=40, min_value=10, max_value=200)
    color = c2.color_picker("Color Principal", "#E30613")
    logo = st.text_input("Texto Logo", "FOTO MONCLOVA")
    programa = st.text_input("Programa de fotos que debe abrir", "C:/Kiosko/EGX/Fotos.exe")
    impresora = st.selectbox("Impresora a usar", ["EPSON L805", "Canon Selphy", "Default Windows", "Otra..."])
    autostart = st.checkbox("Auto Start con Windows (version .EXE)")
    st.info(f"Guardado: Abrirá {programa} en {impresora} y cobrará ${precio}. AutoStart: {autostart}")

st.divider()
st.markdown(f"<div class='price-tag'>${precio}</div>", unsafe_allow_html=True)

col_filtro, col_marco = st.columns(2)
filtro = col_filtro.selectbox("Filtro", ["Original", "Blanco y Negro", "Vintage Monclova", "Rojo Pasión"])
marco = col_marco.selectbox("Marco", ["Sin Marco", "Rojo Monclova", "Polaroid 2026", "Negro Premium"])

# --- FLUJO COBRO ---
if 'pagado' not in st.session_state:
    st.session_state.pagado = False

if not st.session_state.pagado:
    if st.button(f"PAGAR ${precio} CON TARJETA 💳", use_container_width=True):
        with st.spinner("Conectando a lector... (MODO DEMO)"):
            import time
            time.sleep(2)
        st.session_state.pagado = True
        st.rerun()
else:
    st.success(f"✅ PAGO ${precio} APROBADO (DEMO) - ABRIENDO {programa}")
    st.markdown("#### 📸 SONRIE - TIENES 15 SEGUNDOS")
    
    img_file = st.camera_input("TOMAR FOTO", label_visibility="collapsed")
    
    if img_file:
        img = Image.open(img_file)
        
        # FILTROS
        if filtro == "Blanco y Negro":
            img = img.convert("L").convert("RGB")
        elif filtro == "Vintage Monclova":
            img = img.convert("RGB")
            # sepia simple
            pixels
