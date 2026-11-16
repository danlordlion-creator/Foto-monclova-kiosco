import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="FOTO MONCLOVA", page_icon="📸", layout="centered")

if "precio" not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = "FOTO MONCLOVA"
    st.session_state.programa = "C:/Kiosko/EGX/Foto.exe"
    st.session_state.impresora = "EPSON L8050"
    st.session_state.ventas = 0
    st.session_state.estado = "ESPERA"

st.markdown("<style>@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@700;900&display=swap'); .stApp{background:radial-gradient(ellipse at top,#1e1e1e 0%,#050505 100%);} .main-title{font-family:Bebas Neue;text-align:center;font-size:88px;color:#E30613;margin:0;text-shadow:0 0 30px rgba(227,6,19,0.6);line-height:0.85;} .main-title2{font-family:Bebas Neue;text-align:center;font-size:88px;color:white;margin:0;line-height:0.85;} .sub{text-align:center;color:#555;font-family:Montserrat;letter-spacing:12px;font-size:11px;margin-top:12px;font-weight:900;} .price-card{background:linear-gradient(180deg,#181818,#0a0a0a);border:1.5px solid #262626;border-radius:32px;padding:38px 20px;margin:28px 0;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.9);} .price-label{font-family:Montserrat;color:#E30613;letter-spacing:6px;font-size:11px;font-weight:900;} .price-value{font-family:Bebas Neue;font-size:130px;color:white;line-height:0.9;margin:10px 0;} .stButton>button{background:linear-gradient(180deg,#E30613,#8a040d) !important;color:white !important;border-radius:100px !important;height:84px !important;font-family:Bebas Neue !important;font-size:30px !important;letter-spacing:2px !important;box-shadow:0 12px 35px rgba(227,6,19,0.4) !important;} .demo{background:#141414;border-left:4px solid #FFD700;border-radius:14px;padding:14px 16px;font-family:Montserrat;font-size:11px;color:#888;line-height:1.7;}</style>", unsafe_allow_html=True)

st.markdown('<div class="main-title">FOTO</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title2">' + st.session_state.logo + '</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">RECUERDOS EN 15 SEGUNDOS - MONCLOVA COAH</div>', unsafe_allow_html=True)

st.markdown('<div class="demo"><b style="color:#FFD700;">SISTEMA V24 SUPER CHINGON - MODO DEMO</b><br>Lector: Point Smart amarilla (esperando datos) | Impresora: ' + st.session_state.impresora + '<br>Programa: ' + st.session_state.programa + ' | Ventas: ' + str(st.session_state.ventas) + '</div>', unsafe_allow_html=True)

with st.expander("CONFIGURACION - 5 toques + hold 5-7s en Windows .EXE"):
    t1, t2, t3 = st.tabs(["COBRO", "DISENO", "SISTEMA"])
    with t1:
        p = st.number_input("Precio", value=st.session_state.precio, min_value=10, max_value=500, step=5)
        lector = st.selectbox("Lector", ["Point Smart Amarilla Demo", "Point Smart Real"])
    with t2:
        l = st.text_input("Texto Logo", value=st.session_state.logo)
        logo_file = st.file_uploader("Subir logo PNG", type=["png","jpg"])
        if logo_file:
            st.image(logo_file, width=150)
    with t3:
        prog = st.text_input("Programa a abrir al cobrar", value=st.session_state.programa)
        imp = st.selectbox("Impresora", ["EPSON L8050", "EPSON L805", "Canon Selphy", "Default Windows"])
        auto = st.checkbox("Auto Start Windows", value=True)
    if st.button("GUARDAR TODO", use_container_width=True, type="primary"):
        st.session_state.precio = p
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.success("Guardado")
        time.sleep(0.6)
        st.rerun()

st.markdown('<div class="price-card"><div class="price-label">PRECIO HOY
