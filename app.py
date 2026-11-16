import streamlit as st
import time
import json
import os
from datetime import datetime

st.set_page_config(page_title='FOTO MONCLOVA', layout='centered')

CONFIG_FILE = 'config_monclova.json'

def cargar_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {
        'precio': 40,
        'logo': 'MONCLOVA',
        'programa': 'C:/Kiosko/EGX/Foto.exe',
        'impresora': 'EPSON L8050',
        'pin': '123',
        'ventas': 0,
        'ganancia': 0,
        'historial': [],
        'color_primary': '#E30613',
        'color_bg': '#050505',
        'color_card': '#121212',
        'fondo_tipo': 'color',
        'tema': 'Chingon Rojo'
    }

def guardar_config():
    data = {
        'precio': st.session_state.precio,
        'logo': st.session_state.logo,
        'programa': st.session_state.programa,
        'impresora': st.session_state.impresora,
        'pin': st.session_state.pin,
        'ventas': st.session_state.ventas,
        'ganancia': st.session_state.ganancia,
        'historial': st.session_state.historial,
        'color_primary': st.session_state.color_primary,
        'color_bg': st.session_state.color_bg,
        'color_card': st.session_state.color_card,
        'fondo_tipo': st.session_state.fondo_tipo,
        'tema': st.session_state.tema
    }
    with open(CONFIG_FILE, 'w') as f:
        json.dump(data, f)

if 'precio' not in st.session_state:
    cfg = cargar_config()
    st.session_state.precio = cfg.get('precio', 40)
    st.session_state.logo = cfg.get('logo', 'MONCLOVA')
    st.session_state.programa = cfg.get('programa', 'C:/Kiosko/EGX/Foto.exe')
    st.session_state.impresora = cfg.get('impresora', 'EPSON L8050')
    st.session_state.pin = cfg.get('pin', '123')
    st.session_state.ventas = cfg.get('ventas', 0)
    st.session_state.ganancia = cfg.get('ganancia', 0)
    st.session_state.historial = cfg.get('historial', [])
    st.session_state.color_primary = cfg.get('color_primary', '#E30613')
    st.session_state.color_bg = cfg.get('color_bg', '#050505')
    st.session_state.color_card = cfg.get('color_card', '#121212')
    st.session_state.fondo_tipo = cfg.get('fondo_tipo', 'color')
    st.session_state.tema = cfg.get('tema', 'Chingon Rojo')
    st.session_state.estado = 'ESPERA'
    st.session_state.mostrar_pin = False
    st.session_state.mostrar_config = False

# TEMAS CHINGONES PREDEFINIDOS
temas = {
    'Chingon Rojo': {'primary': '#E30613', 'bg': '#050505', 'card': '#121212'},
    'Neon Cyber': {'primary': '#00FFFF', 'bg': '#0a0a1a', 'card': '#111122'},
    'Oro Negro': {'primary': '#FFD700', 'bg': '#0a0a0a', 'card': '#1a1500'},
    'Morado Power': {'primary': '#8A2BE2', 'bg': '#0f0a1a', 'card': '#1a1222'},
    'Verde Matrix': {'primary': '#00FF41', 'bg': '#020a02', 'card': '#0a1a0a'}
}

# CSS DINAMICO CON COLORES EDITABLES
cp = st.session_state.color_primary
cb = st.session_state.color_bg
cc = st.session_state.color_card

c01 = '<style>'
c02 = '.stApp{background:'+cb+';}'
c03 = '.t1{font-size:52px;color:'+cp+';text-align:center;font-weight:900;margin:0;letter-spacing:4px;text-shadow:0 0 20px '+cp+'80;}'
c04 = '.t2{font-size:52px;color:white;text-align:center;font-weight:900;margin:0;letter-spacing:4px;}'
c05 = '.sub{font-size:9px;letter-spacing:5px;color:#555;text-align:center;}'
c06 = '.card{background:radial-gradient(circle at 50% 0%, '+cc+', #000000);border:1px solid '+cp+'33;border-radius:28px;padding:32px;text-align:center;margin:18px 0;box-shadow:0 0 40px '+cp+'22, inset 0 1px 0 rgba(255,255,255,0.1);}'
c07 = '.price{font-size:100px;color:white;font-weight:900;text-align:center;line-height:1;text-shadow:0 0 30px '+cp+'60;}'
c08 = '.lbl{color:'+cp+';font-size:10px;letter-spacing:5px;text-align:center;font-weight:900;}'
c09 = 'div[data-testid="stButton"] button[kind="primary"]{background:'+cp+';border:none;border-radius:16px;font-weight:900;letter-spacing:2px;box-shadow:0 0 20px '+cp+'60;}'
c10 = '</style>'

st.markdown(c01+c02+c03+c04+c05+c06+c07+c08+c09+c10, unsafe_allow_html=True)

def guardar_venta():
    now = datetime.now()
    v = {'hora': now.strftime('%H:%M:%S'), 'fecha': now.strftime('%d/%m/%Y'), 'monto': st.session_state.precio}
    st.session_state.historial.append(v)
    st.session_state.ventas += 1
    st.session_state.ganancia += st.session_state.precio
    guardar_config()

def detectar_impresion_terminada():
    time.sleep(3)
    return True

st.markdown('<div class=t1>FOTO</div>', unsafe_allow_html=True)
st.markdown('<div class=t2>'+st.session_state.logo+'</div>', unsafe_allow_html=True)
st.markdown('<div class=sub>RECUERDOS EN 15 SEGUNDOS - MONCLOVA</div>', unsafe_allow_html=True)

if not st.session_state.mostrar_config and not st.session_state.mostrar_pin:
    c1, c2 = st.columns([10,1])
    with c2:
        if st.button('.', key='dot'):
            st.session_state.mostrar_pin = True
            st.rerun()

if st.session_state.mostrar_pin and not st.session_state.mostrar_config:
    st.warning('PIN ADMIN')
    pin_in = st.text_input('PIN', type='password', max_chars=6)
    b1, b2 = st.columns(2)
    with b1:
        if st.button('ENTRAR', type='primary', use_container_width=True):
            if pin_in == st.session_state.pin:
                st.session_state.mostrar_config = True
                st.session_state.mostrar_pin = False
                st.rerun()
            else:
                st.error('PIN MAL')
    with b2:
        if st.button('CANCELAR', use_container_width=True):
            st.session_state.mostrar_pin = False
            st.rerun()

if st.session_state.mostrar_config:
    st.success('CONFIG - TEMA '+st.session_state.tema)
    t1, t2, t3, t4 = st.tabs(['COBRO Y FOTO', 'DISENO CHINGON', 'PIN', 'CAJA'])
    with t1:
        p = st.number_input('Precio MXN', value=st.session_state.precio, min_value=10, max_value=500, step=5)
        l = st.text_input('Logo 2da linea', value=st.session_state.logo)
        prog = st.text_input('Ruta EGX .EXE', value=st.session_state.programa)
        imp = st.selectbox('Impresora', ['EPSON L8050','EPSON L805','Canon Selphy'], index=0)
    with t2:
        st.subheader('DISENO CHINGON - FONDO Y COLORES')
        tema_sel = st.selectbox('Temas predefinidos chingones', list(temas.keys()), index=list(temas.keys()).index(st.session_state.tema) if st.session_state.tema in temas else 0)
        if st.button('APLICAR TEMA '+tema_sel):
            st.session_state.color_primary = temas[tema_sel]['primary']
            st.session_state.color_bg = temas[tema_sel]['bg']
            st.session_state.color_card = temas[tema_sel]['card']
            st.session_state.tema = tema_sel
            guardar_config()
            st.rerun()
        st.divider()
        st.write('Colores personalizados:')
        cp_new = st.color_picker('Color principal chingon', value=st.session_state.color_primary)
        bg_new = st.color_picker('Color fondo', value=st.session_state.color_bg)
        card_new = st.color_picker('Color tarjeta precio', value=st.session_state.color_card)
        st.caption('Fondo con imagen proximamente - por ahora colores solidos con glow')
    with t3:
        nuevo_pin = st.text_input('Cambiar PIN permanente', value=st.session_state.pin, max_chars=6)
        st.caption('Se guarda en '+CONFIG_FILE+' - no se borra al apagar')
    with t4:
        st.metric('Ventas hoy', st.session_state.ventas)
        st.metric('Ganancia', '$'+str(st.session_state.ganancia))
        if st.button('REINICIAR DIA'):
            st.session_state.ventas = 0
            st.session_state.ganancia = 0
            st.session_state.historial = []
            guardar_config()
            st.rerun()

    if st.button('GUARDAR TODO PERMANENTE CHINGON', type='primary', use_container_width=True):
        st.session_state.precio = p
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.session_state.pin = nuevo_pin
        st.session_state.color_primary = cp_new
        st.session_state.color_bg = bg_new
        st.session_state.color_card = card_new
        guardar_config()
        st.session_state.mostrar_config = False
        st.session_state.mostrar_pin = False
        st.success('GUARDADO - DISENO CHINGON ACTIVO')
        time.sleep(1)
        st.rerun()

if not st.session_state.mostrar_pin and not st.session_state.mostrar_config:
    st.markdown('<div class=card><div class=lbl>PRECIO</div><div class=price>$'+str(st.session_state.precio)+'</div><div class=lbl>TOCA PARA PAGAR</div></div>', unsafe_allow_html=True)
    est = st.session_state.estado
    if est == 'ESPERA':
        if st.button('PAGAR $'+str(st.session_state.precio)+' CON TARJETA', use_container_width=True, type='primary'):
            st.session_state.estado = 'COBRANDO'
            st.rerun()
    if est == 'COBRANDO':
        with st.spinner('Point Smart...'):
            time.sleep(1.2)
        st.session_state.estado = 'APROBADO'
        st.rerun()
    if est == 'APROBADO':
        guardar_venta()
       
