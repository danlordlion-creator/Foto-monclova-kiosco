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
    st.session_state.toques = 0
    st.session_state.mostrar_config = False

st.title("FOTO MONCLOVA")
st.caption("RECUERDOS EN 15 SEGUNDOS - MONCLOVA COAH")

# TOQUE SECRETO
col_tap, col_empty = st.columns([1,5])
with col_tap:
    if st.button(".", key="tap"):
        st.session_state.toques = st.session_state.toques + 1
        if st.session_state.toques >= 5:
            st.session_state.mostrar_config = True
            st.session_state.toques = 0
            st.toast("Config desbloqueada")
        st.rerun()

if st.session_state.mostrar_config == True:
    st.warning("CONFIG DESBLOQUEADA - 5 toques")
    p = st.number_input("Precio", value=st.session_state.precio, min_value=10, max_value=500, step=5)
    l = st.text_input("Logo", value=st.session_state.logo)
    prog = st.text_input("Programa", value=st.session_state.programa)
    imp = st.selectbox("Impresora", ["EPSON L8050","EPSON L805","Canon Selphy"])
    if st.button("GUARDAR Y OCULTAR", type="primary", use_container_width=True):
        st.session_state.precio = p
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.session_state.mostrar_config = False
        st.rerun()
    if st.button("OCULTAR"):
        st.session_state.mostrar_config = False
        st.rerun()
else:
    st.info("MODO DEMO - Impresora " + st.session_state.impresora)
    precio_txt = "$" + str(st.session_state.precio) + " MXN"
    st.metric(label="PRECIO HOY", value=precio_txt)
    
    estado_actual = st.session_state.estado
    
    if estado_actual == "ESPERA":
        texto_boton = "PAGAR $" + str(st.session_state.precio) + " CON TARJETA"
        if st.button(texto_boton, use_container_width=True, type="primary"):
            st.session_state.estado = "COBRANDO"
            st.rerun()
    
    if estado_actual == "COBRANDO":
        with st.spinner("Conectando..."):
            time.sleep(1)
        st.session_state.estado = "APROBADO"
        st.rerun()
    
    if estado_actual == "APROBADO":
        st.session_state.ventas = st.session_state.ventas + 1
        msg_ok = "PAGO APROBADO $" + str(st.session_state.precio)
        st.success(msg_ok)
        st.info("ABRIENDO " + st.session_state.programa)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("FOTO TOMADA", use_container_width=True):
                st.session_state.estado = "ESPERANDO_IMP"
                st.rerun()
        with c2:
            if st.button("CANCELAR", use_container_width=True):
                st.session_state.estado = "ESPERA"
                st.rerun()
    
    if estado_actual == "ESPERANDO_IMP":
        msg_imp = "ESPERANDO IMPRESION EN " + st.session_state.impresora
        st.warning(msg_imp)
        if st.button("IMPRESION TERMINADA", type="primary", use_container_width=True):
            st.session_state.estado = "ESPERA"
            st.rerun()

st.caption("V28 - Toques secretos - Toca 5 veces el punto arriba")
