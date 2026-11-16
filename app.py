import streamlit as st
import time

st.set_page_config(page_title="FOTO MONCLOVA", page_icon="📸", layout="centered")

if "precio" not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = "FOTO MONCLOVA"
    st.session_state.programa = "C:/Kiosko/EGX/Foto.exe"
    st.session_state.impresora = "EPSON L8050"
    st.session_state.ventas = 0
    st.session_state.estado = "ESPERA"

# DISENO SUPER CHINGON SIN COMILLAS QUE ROMPAN EL CODIGO
st.markdown("<style> @import url(https://fonts.googleapis.com/css2?family=Bebas+Neue); .stApp{background:#080808;} .bigprice{font-family:Bebas Neue;font-size:120px;color:white;text-align:center;line-height:1;} .label{font-family:Montserrat;color:#E30613;letter-spacing:6px;font-size:12px;text-align:center;font-weight:900;} .card{background:#141414;border:1px solid #222;border-radius:30px;padding:30px;margin:20px 0;} </style>", unsafe_allow_html=True)

st.markdown("<h1 style=color:#E30613;text-align:center;font-family:B
