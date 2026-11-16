import streamlit as st
import time
import json
import os
from datetime import datetime

st.set_page_config(page_title="FOTO MONCLOVA", layout="centered")

CONFIG_FILE = "config_monclova.json"

def cargar_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except:
            pass
    return {
        "precio": 40,
        "logo": "MONCLOVA",
        "programa": "C:/Kiosko/EGX/Foto.exe",
        "impresora": "EPSON L8050",
        "pin": "123",
        "ventas": 0,
        "ganancia": 0,
        "historial": [],
        "color_primary": "#E30613",
        "color_bg": "#070708",
        "color_card": "#141416",
        "tema": "Rojo"
    }

def guardar_config():
    data = {
        "precio": st.session_state.precio,
        "logo": st.session_state.logo,
        "programa": st.session_state.programa,
        "impresora": st.session_state.impresora,
        "pin": st.session_state.pin,
        "ventas": st.session_state.ventas,
        "ganancia": st.session_state.ganancia,
        "historial": st.session_state.historial,
        "color_primary": st.session_state.color_primary,
        "color_bg": st.session_state.color_bg,
        "color_card": st.session_state.color_card,
        "tema": st.session_state.tema
    }
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f)

if "precio" not in st.session_state:
    cfg = cargar_config()
    st.session_state.precio = cfg.get("precio", 40)
    st.session_state.logo = cfg.get("logo", "MONCLOVA")
    st.session_state.programa = cfg.get("programa", "C:/Kiosko/EGX/Foto.exe")
    st.session_state.impresora = cfg.get("impresora", "EPSON L8050")
    st.session_state.pin = cfg.get("pin", "123")
    st.session_state.ventas = cfg.get("ventas", 0)
    st.session_state.ganancia = cfg.get("ganancia", 0)
    st.session_state.historial = cfg.get("historial", [])
    st.session_state.color_primary = cfg.get("color_primary", "#E30613")
    st.session_state.color_bg = cfg.get("color_bg", "#070708")
    st.session_state.color_card = cfg.get("color_card", "#141416")
    st.session_state.tema = cfg.get("tema", "Rojo")
    st.session_state.estado = "ESPERA"
    st.session_state.mostrar_pin = False
    st.session_state.mostrar_config = False

temas_nombres = ["Rojo","Neon","Oro","Morado","Verde","Blanco"]
temas_primary = ["#E30613","#00E5FF","#FFC400","#9C27FF","#00E676","#FFFFFF"]
temas_bg = ["#070708","#060a14","#0c0a06","#0c0614","#05120a","#050505"]
temas_card = ["#141416","#101828","#1a160a","#1a1228","#0f1f14","#18181a"]

cp = st.session_state.color_primary
cb = st.session_state.color_bg
cc = st.session_state.color_card

# CSS SEGURO CON PARENTESIS
c01 = "<style>"
c02 = (".stApp{background:" + cb + ";}")
c03 = (".t1{font-size:48px;color:" + cp + ";text-align:center;font-weight:900;margin:0;}")
c04 = ".t2{font-size:48px;color:white;text-align:center;font-weight:900;margin:0;}"
c05 = ".sub{font-size:10px;letter-spacing:5px;color:#666;text-align:center;}"
c06 = (".card{background:" + cc + ";border:1px solid " + cp + "33;border-radius:28px;padding:32px;text-align:center;margin:18px 0;}")
c07 = ".price{font-size:100px;color:white;font-weight:900;text-align:center;}"
c08 = (".lbl{color:" + cp + ";font-size:11px;letter-spacing:4px;text-align:center;font-weight:900;}")
c09 = "</style>"

st.markdown(c01+c02+c03+c04+c05+c06+c07+c08+c09, unsafe_allow_html=True)

def guardar_venta():
    now = datetime.now()
    v = {"hora": now.strftime("%H:%M:%S"), "fecha": now.strftime("%d/%m/%Y"), "monto": st.session_state.precio}
    st.session_state.historial.append(v)
    st.session_state.ventas += 1
    st.session_state.ganancia += st.session_state.precio
    guardar_config()

def detectar_impresion_terminada():
    time.sleep(3)
    return True

st.markdown('<div class=t1>FOTO</div>', unsafe_allow_html=True)
st.markdown('<div class=t2>'+st.session_state.logo+'</div>', unsafe_allow_html=True)
st.markdown('<div class=sub>RECUERDOS EN 15 SEGUNDOS</div>', unsafe_allow_html=True)

if not st.session_state.mostrar_config and not st.session_state.mostrar_pin:
    c1, c2 = st.columns([10,1])
    with c2:
        if st.button(".", key="dot"):
            st.session_state.mostrar_pin = True
            st.rerun()

if st.session_state.mostrar_pin and not st.session_state.mostrar_config:
    st.warning("ACCESO ADMINISTRADOR")
    pin_in = st.text_input("PIN", type="password", max_chars=6)
    b1, b2 = st.columns(2)
    with b1:
        if st.button("ENTRAR", type="primary", use_container_width=True):
            if pin_in == st.session_state.pin:
                st.session_state.mostrar_config = True
                st.session_state.mostrar_pin = False
                st.rerun()
            else:
                st.error("PIN MAL")
    with b2:
        if st.button("CANCELAR", use_container_width=True):
            st.session_state.mostrar_pin = False
            st.rerun()

if st.session_state.mostrar_config:
    st.info("CONFIGURACION")
    t1, t2, t3, t4 = st.tabs(["COBRO","DISENO","ACCESO","VENTAS"])
    with t1:
        p = st.number_input("Precio $", value=st.session_state.precio, min_value=10, max_value=500, step=5)
        l = st.text_input("Logo", value=st.session_state.logo)
        prog = st.text_input("Programa EGX", value=st.session_state.programa)
        imp = st.selectbox("Impresora", ["EPSON L8050","EPSON L805","Canon Selphy"], index=0)
    with t2:
        st.write("Temas")
        cols = st.columns(3)
        for i in range(len(temas_nombres)):
            with cols[i % 3]:
                if st.button(temas_nombres[i], use_container_width=True, key="tema_"+str(i)):
                    st.session_state.color_primary = temas_primary[i]
                    st.session_state.color_bg = temas_bg[i]
                    st.session_state.color_card = temas_card[i]
                    st.session_state.tema = temas_nombres[i]
                    guardar_config()
                    st.rerun()
        st.divider()
        cp_new = st.color_picker("Principal", value=st.session_state.color_primary)
        bg_new = st.color_picker("Fondo", value=st.session_state.color_bg)
        card_new = st.color_picker("Tarjeta", value=st.session_state.color_card)
    with t3:
        nuevo_pin = st.text_input("PIN", value=st.session_state.pin, max_chars=6)
    with t4:
        st.metric("Hoy", str(st.session_state.ventas)+" fotos")
        st.metric("Total", "$"+str(st.session_state.ganancia))
        if st.button("Reiniciar dia"):
            st.session_state.ventas = 0
            st.session_state.ganancia = 0
            st.session_state.historial = []
            guardar_config()
            st.rerun()
    if st.button("GUARDAR Y SALIR", type="primary", use_container_width=True):
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
        st.rerun()

if not st.session_state.mostrar_pin and not st.session_state.mostrar_config:
    st.markdown('<div class=card><div class=lbl>PRECIO HOY</div><div class=price>$'+str(st.session_state.precio)+'</div></div>', unsafe_allow_html=True)
    est = st.session_state.estado
    if est == "ESPERA":
        if st.button("PAGAR $"+str(st.session_state.precio), type="primary", use_container_width=True):
            st.session_state.estado = "COBRANDO"
            st.rerun()
    if est == "COBRANDO":
        with st.spinner("Procesando..."):
            time.sleep(1.2)
        st.session_state.estado = "APROBADO"
        st.rerun()
    if est == "APROBADO":
        guardar_venta()
        st.success("APROBADO")
        st.session_state.estado = "IMPRIMIENDO"
        st.rerun()
    if est == "IMPRIMIENDO":
        with st.spinner("Imprimiendo..."):
            if detectar_impresion_terminada():
                time.sleep(0.8)
                st.session_state.estado = "ESPERA"
                st.rerun()
