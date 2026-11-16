import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="FOTO MONCLOVA", layout="centered")

if "precio" not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = "FOTO MONCLOVA"
    st.session_state.programa = "C:/Kiosko/EGX/Foto.exe"
    st.session_state.impresora = "EPSON L8050"
    st.session_state.ventas = 0
    st.session_state.estado = "ESPERA"
    st.session_state.mostrar_config = False

# CSS EN CACHITOS - SIN IMPORT URL PARA QUE NO TRUENE
p1 = "<style>"
p2 = ".stApp{background:#050505;}"
p3 = ".t1{font-size:70px;color:#E30613;text-align:center;font-weight:900;line-height:0.9;}"
p4 = ".t2{font-size:70px;color:white;text-align:center;font-weight:900;line-height:0.9;}"
p5 = ".card{background:#141414;border:1px solid #222;border-radius:24px;padding:25px;margin:20px 0;text-align:center;}"
p6 = ".price{font-size:90px;color:white;font-weight:900;text-align:center;}"
p7 = ".lbl{color:#E30613;letter-spacing:4px;font-size:10px;text-align:center;font-weight:900;}"
p8 = "</style>"

st.markdown(p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8, unsafe_allow_html=True)

# GESTO 5 TOQUES + HOLD 5-6s
components.html("""
<div id=zona style=width:100%;height:45px;background:#111;border-radius:10
