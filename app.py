import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="FOTO MONCLOVA", page_icon="📸", layout="centered")

if "precio" not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = "FOTO MONCLOVA"
    st.session_state.programa = "C:/Kiosko/EGX/Foto.exe"
    st.session_state.impresora = "EPSON L8050"
    st.session_state.ventas = 0
    st.session_state.estado = "ESPERA"
    st.session_state.mostrar_config = False

# DISENO SUPER CHINGON - TODO CON CLASES, SIN COMILLAS DOBLES DENTRO
st.markdown('<style>@import url(https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@700;900&display=swap); .stApp{background:radial-gradient(ellipse at top,#1a1a1a 0%,#050505 100%);} .main1{font-family:Bebas Neue;font-size:90px;color:#E306
