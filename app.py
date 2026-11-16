import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="FOTO MONCLOVA", page_icon="📸", layout="centered")

# CONFIG
if "precio" not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = "FOTO MONCLOVA"
    st.session_state.programa = "C:/Kiosko/EGX/Foto.exe"
    st.session_state.impresora = "EPSON L8050"
    st.session_state.autostart = True
    st.session_state.ventas = 0
    st.session_state.estado = "ESPERA"

st.title("FOTO MONCLOVA")
st.subheader("RECUERDOS EN 15 SEGUNDOS - COAH")
st.info("MODO DEMO - Esperando Point Smart amarilla | Impresora: " + st.session_state.impresora + " | Programa: " + st.session_state.programa + " | Ventas: " + str(st.session_state.ventas))

# CONFIGURACION
with st.expander("CONFIGURACION - 5 toques + hold 5-7s en Windows .EXE"):
    st.markdown("### PANEL COMPLETO")
    tab1, tab2, tab3 = st.tabs(["COBRO", "DISENO", "SISTEMA"])
    with tab1:
        p = st.number_input("Precio", value=st.session_state.precio, min_value=10, max_value=500, step=5)
        lector = st.selectbox("Lector", ["Point Smart Demo", "Point Smart Real"])
    with tab2:
        c = st.color_picker("Color principal", "#E30613")
        l = st.text_input("Logo texto", value=st.session_state.logo)
        logo_file = st.file_uploader("Subir logo PNG", type=["png","jpg"])
        if logo_file:
            st.image(logo_file, width=150)
    with tab3:
        prog = st.text_input("Programa fotos a abrir al cobrar", value=st.session_state.programa)
        imp = st.selectbox("Impresora a usar", ["EPSON L8050", "EPSON L805", "Canon Selphy", "Default Windows"])
        auto = st.checkbox("Auto Start Windows", value=st.session_state.autostart)
        demo = st.checkbox("Modo Demo", value=True)
    if st.button("GUARDAR TODO", use_container_width=True, type="primary"):
        st.session_state.precio = p
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.session_state.autostart = auto
        st.success("Guardado")
        time.sleep(0.5)
        st.rerun()

st.divider()
st.metric(label="PRECIO HOY", value=f"${st.session_state.precio} MXN")
st.caption("TOCA PARA PAGAR CON TARJETA")

# FLUJO
if st.session_state.estado == "ESPERA":
    if st.button(f"PAGAR ${st.session_state.precio} CON TARJETA", use_container_width=True):
        st.session_state.estado = "COBRANDO"
        st.rerun()

elif st.session_state.estado == "COBRANDO":
    with st.spinner("Conectando lector..."):
        time.sleep(1.5)
    st.warning(f"ACERQUE TARJETA - ${st.session_state.precio} MODO DEMO")
    time.sleep(1)
    st.session_state.estado = "APROBADO"
    st.rerun()

elif st.session_state.estado == "APROBADO":
    st.session_state.ventas += 1
    st.success(f"PAGO ${st.session_state.precio} APROBADO")
    st.info(f"ABRIENDO: {st.session_state.programa}")
    st.info(f"Impresora: {st.session_state.impresora} - Al terminar regresa solo")
    c1, c2 = st.columns(2)
    if c1.button("FOTO TOMADA", use_container_width=True):
        st.session_state.estado = "ESPERANDO_IMP"
        st.rerun()
    if c2.button("CANCELAR", use_container_width=True):
        st.session_state.estado = "ESPERA"
        st.rerun()

elif st.session_state.estado == "ESPERANDO_IMP":
    st.warning(f"ESPERANDO IMPRESION EN {st.session_state.impresora}")
    if st.button("IMPRESION TERMINADA - REGRESAR A COBRO", use_container_width=True, type="primary"):
        st.session_state.estado = "ESPERA"
        st.toast("Regresando a cobro")
        time.sleep(1)
        st.rerun()

st.caption("V22 FIX - Sin filtros ni marcos - 5 toques + hold para config en .EXE")
