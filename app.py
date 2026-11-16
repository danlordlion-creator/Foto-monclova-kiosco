import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="FOTO MONCLOVA KIOSKO", page_icon="📸", layout="centered")

# --- CONFIG DEFAULT ---
if 'precio' not in st.session_state:
    st.session_state.precio = 40
if 'color' not in st.session_state:
    st.session_state.color = "#E30613"
if 'logo' not in st.session_state:
    st.session_state.logo = "FOTO MONCLOVA"
if 'programa' not in st.session_state:
    st.session_state.programa = "C:/Kiosko/EGX/Foto.exe"
if 'impresora' not in st.session_state:
    st.session_state.impresora = "EPSON L8050"
if 'autostart' not in st.session_state:
    st.session_state.autostart = True
if 'ventas' not in st.session_state:
    st.session_state.ventas = 0
if 'estado' not in st.session_state:
    st.session_state.estado = "ESPERA"

# CSS SIN F-STRING PARA QUE NO TRUENE
css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@700&display=swap');
.stApp { background-color: #050505; }
h1 { font-family: Bebas Neue; text-align:center; color:white !important; font-size:80px !important; margin:0; line-height:0.9; }
.subtitle { text-align:center; color:#666; font-family:Montserrat; letter-spacing:10px; font-size:11px; }
.price-box { background: #111; border: 1px solid #222; border-radius: 30px; padding: 30px; margin: 25px 0; text-align:center; }
.price { font-family: Bebas Neue; font-size: 110px; color: white; }
.price-label { font-family: Montserrat; color: #E30613; letter-spacing: 5px; font-size: 11px; font-weight: 900; }
.stButton>button { background: #E30613 !important; color: white !important; border-radius: 100px !important; height: 75px !important; font-family: Bebas Neue !important; font-size: 26px !important; }
.demo-box { background: #141414; border-left: 4px solid gold; border-radius: 12px; padding: 12px; font-family: Montserrat; font-size: 11px; color: #999; }
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# HEADER
st.markdown("<h1 style='color:#E30613;'>FOTO</h1>", unsafe_allow_html=True)
st.markdown("<h1>" + st.session_state.logo + "</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>RECUERDOS EN 15 SEGUNDOS - MONCLOVA COAH</p>", unsafe_allow_html=True)

st.markdown("<div class='demo-box'><b>MODO DEMO</b> - Esperando datos Point Smart amarilla<br>Impresora: " + st.session_state.impresora + " | Programa: " + st.session_state.programa + " | Ventas hoy: " + str(st.session_state.ventas) + "</div>", unsafe_allow_html=True)

# CONFIGURACION COMPLETA
with st.expander("CONFIGURACION - 5 toques + hold 5-7s en Windows .EXE"):
    st.write("### PANEL DE CONTROL TOTAL")
    t1, t2, t3 = st.tabs(["COBRO", "DISENO", "SISTEMA"])
    with t1:
        p = st.number_input("Precio", value=st.session_state.precio, min_value=10, max_value=500, step=5)
        lector = st.selectbox("Lector", ["Point Smart Amarilla Demo", "Point Smart Real (cuando me pases datos)", "USB Generico"])
    with t2:
        c = st.color_picker("Color principal", st.session_state.color)
        l = st.text_input("Texto Logo", value=st.session_state.logo)
        logo_file = st.file_uploader("Subir logotipo PNG", type=["png","jpg"])
        if logo_file:
            st.image(logo_file, width=150)
    with t3:
        prog = st.text_input("Programa fotos a abrir al cobrar", value=st.session_state.programa)
        imp = st.selectbox("Impresora", ["EPSON L8050", "EPSON L805", "Canon Selphy", "Default Windows", "Otra manual"])
        if imp == "Otra manual":
            imp = st.text_input("Nombre impresora manual")
        auto = st.checkbox("Auto Start con Windows", value=st.session_state.autostart)
        demo = st.checkbox("Modo Demo", value=True)
    
    if st.button("GUARDAR TODO", use_container_width=True, type="primary"):
        st.session_state.precio = p
        st.session_state.color = c
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.session_state.autostart = auto
        st.success("Guardado")
        time.sleep(0.8)
        st.rerun()

st.divider()

st.markdown("<div class='price-box'><div class='
