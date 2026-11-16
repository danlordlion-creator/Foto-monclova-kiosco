import streamlit as st
import time

st.set_page_config(page_title='FOTO MONCLOVA', layout='centered')

if 'precio' not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = 'MONCLOVA'
    st.session_state.programa = 'C:/Kiosko/EGX/Foto.exe'
    st.session_state.impresora = 'EPSON L8050'
    st.session_state.ventas = 0
    st.session_state.ganancia = 0
    st.session_state.estado = 'ESPERA'
    st.session_state.pin = '1234'
    st.session_state.mostrar_pin = False
    st.session_state.mostrar_config = False

# CSS
c01 = '<style>'
c02 = '.stApp{background:#050505;}'
c03 = '.t1{font-size:48px;color:#E30613;text-align:center;font-weight:900;margin:0;}'
c04 = '.t2{font-size:48px;color:white;text-align:center;font-weight:900;margin:0;}'
c05 = '.sub{font-size:9px;letter-spacing:4px;color:#333;text-align:center;margin-top:6px;}'
c06 = '.card{background:#121212;border:1px solid #222;border-radius:24px;padding:28px;text-align:center;margin:16px 0;}'
c07 = '.price{font-size:90px;color:white;font-weight:900;text-align:center;}'
c08 = '</style>'
st.markdown(c01+c02+c03+c04+c05+c06+c07+c08, unsafe_allow_html=True)

st.markdown('<div class=t1>FOTO</div>', unsafe_allow_html=True)
st.markdown('<div class=t2>'+st.session_state.logo+'</div>', unsafe_allow_html=True)
st.markdown('<div class=sub>RECUERDOS EN 15 SEGUNDOS</div>', unsafe_allow_html=True)

# BOTON INVISIBLE PARA PIN - ABAJO DERECHA
col_a, col_b = st.columns([9,1])
with col_b:
    if st.button('.', key='dot'):
        st.session_state.mostrar_pin = True
        st.rerun()

# ENTRADA PIN
if st.session_state.mostrar_pin and not st.session_state.mostrar_config:
    st.warning('INGRESA PIN PARA CONFIG')
    pin_in = st.text_input('PIN', type='password', max_chars=6)
    c1, c2 = st.columns(2)
    with c1:
        if st.button('ENTRAR', type='primary', use_container_width=True):
            if pin_in == st.session_state.pin:
                st.session_state.mostrar_config = True
                st.session_state.mostrar_pin = False
                st.rerun()
            else:
                st.error('PIN INCORRECTO')
    with c2:
        if st.button('CANCELAR', use_container_width=True):
            st.session_state.mostrar_pin = False
            st.rerun()

# CONFIG CON CAMBIO DE PIN
if st.session_state.mostrar_config:
    st.success('CONFIG DESBLOQUEADA - PIN '+st.session_state.pin)
    tab1, tab2, tab3 = st.tabs(['COBRO', 'DISENO', 'PIN Y SISTEMA'])
    with tab1:
        p = st.number_input('Precio MXN', value=st.session_state.precio, min_value=10, max_value=500, step=5)
    with tab2:
        l = st.text_input('Logo 2da linea', value=st.session_state.logo)
        imp = st.selectbox('Impresora', ['EPSON L8050','EPSON L805','Canon Selphy'])
    with tab3:
        prog = st.text_input('Programa EGX .EXE', value=st.session_state.programa)
        nuevo_pin = st.text_input('Cambiar PIN - actual '+st.session_state.pin, value=st.session_state.pin, max_chars=6)
        st.caption('PIN por defecto 1234 - Cambialo aqui')
    if st.button('GUARDAR TODO Y OCULTAR', type='primary', use_container_width=True):
        st.session_state.precio = p
