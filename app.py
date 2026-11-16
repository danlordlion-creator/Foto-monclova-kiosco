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

# CSS SUPER CHINGON - SIN F-STRING PARA QUE NO TRUENE
st.markdown('''
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@700;900&display=swap');
.stApp {
    background: radial-gradient(ellipse at top, #1e1e1e 0%, #050505 100%);
}
h1 {
    font-family: Bebas Neue !important;
    text-align: center !important;
    letter-spacing: 3px;
    line-height: 0.85;
}
.main-title {
    font-family: Bebas Neue;
    text-align: center;
    font-size: 88px;
    color: #E30613;
    margin: 0;
    text-shadow: 0 0 30px rgba(227,6,19,0.6);
    line-height: 0.85;
}
.main-title2 {
    font-family: Bebas Neue;
    text-align: center;
    font-size: 88px;
    color: white;
    margin: 0;
    line-height: 0.85;
}
.sub {
    text-align: center;
    color: #555;
    font-family: Montserrat;
    letter-spacing: 12px;
    font-size: 11px;
    margin-top: 12px;
    font-weight: 900;
}
.price-card {
    background: linear-gradient(180deg, #181818, #0a0a0a);
    border: 1.5px solid #262626;
    border-radius: 32px;
    padding: 38px 20px;
    margin: 28px 0;
    text-align: center;
    box-shadow: 0 20px 60px rgba(0,0,0,0.9);
    position: relative;
}
.price-card:before {
    content: "";
    position: absolute;
    top: 0;
    left: 20%;
    right: 20%;
    height: 1px;
    background: linear-gradient(90deg, transparent
