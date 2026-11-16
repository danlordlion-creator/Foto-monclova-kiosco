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

st.markdown("<style>.stApp{background:#0a0a0a;} .tap{opacity:0.08; font-size:10px;}</style>", unsafe_allow_html=True)

# ZONA SECRETA DE TOQUES - INVISIBLE ARRIBA
c1, c2, c3 = st.columns([1,5,1])
with c1:
    if st.button("·", key="tap_secret"):
        st.session_state.toques += 1
        if st.session_state.toques >= 5:
            st.session_state.mostrar_config = True
            st.session_state.toques = 0
            st.toast("Acceso configuracion desbloqueado - 5 toques detectados", icon="🔓")
        else:
            st.toast(f"Toque {st.session_state.toques}/5", icon="👆")

st.title("FOTO MONCLOVA")
st.caption(f"RECUERDOS EN 15 SEGUNDOS - {st.session_state.logo}")

if not st.session_state.mostrar_config:
    st.info("MODO DEMO - Impresora " + st.session_state.impresora)
else:
    st.warning("🔓 CONFIG DESBLOQUEADA - 5 toques detectados")
    st.markdown("### En Windows .EXE real sera 5 toques rapidos + 6to sostenido 5-7 segundos")
    p = st.number_input("Precio", value=st.session_state.precio, min_value=10, max_value=500, step=5)
    l = st.text_input("Logo texto", value=st.session_state.logo)
    prog = st.text_input("Programa fotos a abrir al cobrar", value=st.session_state.programa)
    imp = st.selectbox("Impresora a usar", ["EPSON L8050","EPSON L805","Canon Selphy","Default Windows"])
    auto = st.checkbox("Auto Start Windows", value=True)
    if st.button("GUARDAR Y OCULTAR", type="primary", use_container_width=True):
        st.session_state.precio = p
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.session_state.mostrar_config = False
        st.success("Guardado y oculto")
        time.sleep(0.5)
        st.rerun()
    if st.button("OCULTAR CONFIG"):
        st.session_state.mostrar_config = False
        st.rerun()
    st.divider()

if not st.session_state.mostrar_config:
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
        c1, c2 = st.columns(2)
        if c1.button("FOTO TOMADA", use_container_width=True):
            st.session_state.estado = "ESPERANDO_IMP"
            st.rerun()
        if c2.button("CANCELAR", use_container_width=True):
            st.session_state.estado = "ESPERA"
            st.rerun()
    elif st.session_state.estado == "
