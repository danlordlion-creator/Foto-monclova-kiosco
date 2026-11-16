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

st.markdown("<style>.stApp{background:#0a0a0a;} h1{color:white; text-align:center;} .stMetric{background:#151515; border-radius:20px; padding:20px;}</style>", unsafe_allow_html=True)

st.title("FOTO MONCLOVA")
st.markdown("### RECUERDOS EN 15 SEGUNDOS - MONCLOVA COAH")
st.info("MODO DEMO - Impresora " + st.session_state.impresora + " - Programa " + st.session_state.programa)

with st.expander("CONFIGURACION"):
    p = st.number_input("Precio", value=st.session_state.precio, min_value=10, max_value=500, step=5)
    l = st.text_input("Logo texto", value=st.session_state.logo)
    prog = st.text_input("Programa fotos a abrir", value=st.session_state.programa)
    imp = st.selectbox("Impresora", ["EPSON L8050","EPSON L805","Canon Selphy"])
    if st.button("GUARDAR TODO", type="primary", use_container_width=True):
        st.session_state.precio = p
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.success("Guardado")
        time.sleep(0.5)
        st.rerun()

st.divider()
st.metric(label="PRECIO HOY", value=f"${st.session_state.precio} MXN")
st.caption("TOCA PARA PAGAR CON TARJETA - POINT SMART")

if st.session_state.estado == "ESPERA":
    if st.button(f"PAGAR ${st.session_state.precio} CON TARJETA", use_container_width=True, type="primary"):
        st.session_state.estado = "COBRANDO"
        st.rerun()

elif st.session_state.estado == "COBRANDO":
    with st.spinner("Conectando Point Smart..."):
        time.sleep(1.2)
    st.session_state.estado = "APROBADO"
    st.rerun()

elif st.session_state.estado == "APROBADO":
    st.session_state.ventas += 1
    st.success(f"PAGO APROBADO ${st.session_state.precio}")
    st.info(f"ABRIENDO {st.session_state.programa}")
    col1, col2 = st.columns(2)
    if col1.button("FOTO TOMADA", use_container_width=True):
        st.session_state.estado = "ESPERANDO_IMP"
        st.rerun()
    if col2.button("CANCELAR", use_container_width=True):
        st.session_state.estado = "ESPERA"
        st.rerun()

elif st.session_state.estado == "ESPERANDO_IMP":
    st.warning(f"ESPERANDO IMPRESION EN {st.session_state.impresora}")
    if st.button("IMPRESION TERMINADA - REGRESAR A COBRO", type="primary", use_container_width=True):
        st.session_state.estado = "ESPERA"
        st.rerun()

st.caption("V26 SAFE - Monclova")
