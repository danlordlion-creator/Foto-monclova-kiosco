# app.py - KIOSKO V16 NOMBRE EDITABLE - FOTO MONCLOVA - FIXED
import streamlit as st

st.set_page_config(page_title="KIOSKO FOTO", layout="wide")

DEFAULT_NOMBRE_PRINCIPAL = "FOTO"
DEFAULT_NOMBRE_SECUNDARIO = "MONCLOVA"
DEFAULT_SLOGAN = "RECUERDOS EN 15 SEG"

if "nombre_principal" not in st.session_state:
    st.session_state.nombre_principal = DEFAULT_NOMBRE_PRINCIPAL
if "nombre_secundario" not in st.session_state:
    st.session_state.nombre_secundario = DEFAULT_NOMBRE_SECUNDARIO
if "slogan" not in st.session_state:
    st.session_state.slogan = DEFAULT_SLOGAN
if "tap_count" not in st.session_state:
    st.session_state.tap_count = 0
if "show_editor" not in st.session_state:
    st.session_state.show_editor = False

st.markdown("""
<style>
.main-title { font-weight: 900; letter-spacing: 5px; text-align: center; }
.title1 { font-size: 4rem; }
.title2 { font-size: 4rem; font-weight: 300; }
.slogan { text-align: center; letter-spacing: 4px; font-size: 1rem; opacity: 0.7; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,6,1])
with col1:
    if st.button(" ", key="secret"):
        st.session_state.tap_count += 1
        if st.session_state.tap_count >= 5:
            st.session_state.show_editor = True
            st.session_state.tap_count = 0

st.markdown(f"""
<div class="main-title">
    <div class="title1">{st.session_state.nombre_principal}</div>
    <div class="title2">{st.session_state.nombre_secundario}</div>
</div>
<div class="slogan">{st.session_state.slogan}</div>
""", unsafe_allow_html=True)

st.markdown("---")

if st.session_state.show_editor:
    st.warning("MODO EDICION - NOMBRE DEL NEGOCIO")
    with st.form("edit_nombre"):
        nuevo_principal = st.text_input("NOMBRE PRINCIPAL", value=st.session_state.nombre_principal)
        nuevo_secundario = st.text_input("NOMBRE SECUNDARIO", value=st.session_state.nombre_secundario)
        nuevo_slogan = st.text_input("SLOGAN ABAJO", value=st.session_state.slogan)
        
        c1, c2 = st.columns(2)
        with c1:
            guardar = st.form_submit_button("GUARDAR")
        with c2:
            cerrar = st.form_submit_button("CERRAR")
        
        if guardar:
            st.session_state.nombre_principal = nuevo_principal.upper()
            st.session_state.nombre_secundario = nuevo_secundario.upper()
            st.session_state.slogan = nuevo_slogan.upper()
            st.session_state.show_editor = False
            st.rerun()
        if cerrar:
            st.session_state.show_editor = False
            st.rerun()

st.info("KIOSKO V16 - Sistema de Foto Listo")

if st.button("TOMAR FOTO", use_container_width=True, type="primary"):
    st.balloons()
    st.write("Foto tomada!")
