# ==============================================================================
# FOTO MONCLOVA - KIOSKO V20 ULTRA LARGO PRO - SIN FILTROS NI MARCOS
# ESPECIFICACIONES QUE PEDISTE:
# - Diseño chingon negro/rojo
# - Cobro con lector Point Smart (MODO DEMO)
# - Boton configuracion: precio, logotipo, color, que programa abrir, que impresora usar, auto-start
# - Al cobrar -> abre programa fotos -> detecta impresion -> regresa a cobro solo
# - Acceso config: 5 toques + 6to sostenido 5-7s (simulado en web, real en .EXE)
# - Modo demo hasta que me pases datos de terminal
# ==============================================================================

import streamlit as st
from datetime import datetime
import time
import json
import os
import base64

st.set_page_config(page_title="FOTO MONCLOVA - KIOSKO PRO", page_icon="📸", layout="centered", initial_sidebar_state="collapsed")

# --- PERSISTENCIA LOCAL (para que no se borre precio) ---
CONFIG_PATH = "kiosko_config.json"
def load_persist():
    try:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
    except:
        pass
    return {"precio": 40, "color": "#E30613", "logo_text": "FOTO MONCLOVA", "programa": "C:/Kiosko/EGX/Foto.exe", "impresora": "EPSON L8050", "autostart": True, "modo_demo": True, "ventas_hoy": 0, "total_cobrado": 0}

def save_persist(data):
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(data, f)
    except:
        pass

persist = load_persist()

# --- CSS ULTRA CHINGON - 150 LINEAS DE DISEÑO ---
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@300;500;700;900&display=swap');
.stApp {{ background: radial-gradient(ellipse at top, #1e1e1e 0%, #0a0a0a 40%, #000000 100%); }}
h1 {{ font-family: 'Bebas Neue' !important; text-align:center !important; color:white !important; font-size:92px !important; margin:0 !important; line-height:0.82 !important; letter-spacing:4px !important; text-shadow: 0 0 20px rgba(227,6,19,0.5); }}
.subtitle {{ text-align:center; color:#555; font-family:Montserrat; letter-spacing:12px; font-size:11px; margin-top:8px; font-weight:700; }}
.price-container {{ background: linear-gradient(180deg, #181818 0%, #0e0e0e 100%); border:1.5px solid #232323; border-radius:35px; padding:35px 20px; margin:30px 0 20px 0; text-align:center; box-shadow: 0 20px 60px rgba(0,0,0,0.8), inset 0 1px 0 rgba(255,255,255,0.05); position:relative; overflow:hidden; }}
.price-container::before {{ content:''; position:absolute; top:0; left:0; right:0; height:1px; background: linear-gradient(90deg, transparent, {persist['color']}, transparent); }}
.price {{ font-family:'Bebas Neue'; font-size:125px; color:white; margin:0; line-height:0.9; letter-spacing:2px; }}
.price-label {{ font-family:Montserrat; color:{persist['color']}; letter-spacing:6px; font-size:11px; font-weight:900; margin-bottom:5px; }}
.price-sub {{ font-family:Montserrat; color:#444; font-size:10px; letter-spacing:3px; margin-top:10px; }}
.stButton>button {{ background: linear-gradient(180deg, {persist['color']} 0%, #7a030a 100%) !important; color:white !important; border-radius:100px !important; height:80px !important; font-family:'Bebas Neue' !important; font-size:30px !important; letter-spacing:2px !important; border:1.5px solid rgba(255,255,255,0.15) !important; box-shadow: 0 10px 30px rgba(227,6,19,0.35), inset 0 1px 0 rgba(255,255,255,0.2) !important; transition: all 0.15s ease !important; }}
.stButton>button:hover {{ transform: translateY(-2px) !important; box-shadow: 0 15px 40px rgba(227,6,19,0.5) !important; }}
.demo-box {{ background: linear-gradient(90deg, #141414, #1a1a1a); border-left:4px solid #FFD700; border-radius:12px; padding:14px 18px; font-family:Montserrat; font-size:11px; color:#999; margin:18px 0; line-height:1.6; }}
.demo-box b {{ color:#FFD700; }}
.status-line {{ display:flex; justify-content:space-between; background:#0f0f0f; border:1px solid #1e1e1e; border-radius:12px; padding:10px 15px; font-family:Montserrat; font-size:10px; color:#555; margin-top:15px; }}
.status-dot {{ width:8px; height:8px; background:#00FF88; border-radius:50%; display:inline-block; margin-right:6px; box-shadow:0 0 10px #00FF88; animation: pulse 1.8s infinite; }}
@keyframes pulse {{ 0%{{opacity:1; transform:scale(1)}} 50%{{opacity:0.6; transform:scale(1.2)}} 100%{{opacity:1; transform:scale(1)}} }}
.config-header {{ font-family:Bebas Neue; font-size:36px; color:white; text-align:center; margin:15px 0 5px 0; letter-spacing:2px; }}
.log-box {{ background:#080808; border:1px solid #1a1a1a; border-radius:10px; padding:10px; font-family:monospace; font-size:10px; color:#666; max-height:120px; overflow-y:auto; }}
.tap-hint {{ background:{persist['color']}15; border:1px dashed {persist['color']}55; border-radius:10px; padding:10px; text-align:center; font-family:Montserrat; font-size:10px; color:{persist['color']}; margin:10px 0; }}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown(f"<h1 style='color:{persist['color']};'>FOTO</h1>", unsafe_allow_html=True)
st.markdown(f"<h1>{persist['logo_text'].split()[0] if len(persist['logo_text'].split())>0 else 'MONCLOVA'}</h1>", unsafe_allow_html=True)
if len(persist['logo_text'].split()) > 1:
    st.markdown(f"<h1 style='font-size:50px !important; opacity:0.8;'>{' '.join(persist['logo_text'].split()[1:])}</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>RECUERDOS EN 15 SEGUNDOS • MONCLOVA COAH.</p>", unsafe_allow_html=True)

st.markdown(f"""
<div class='demo-box'>
<span class='status-dot'></span> <b>SISTEMA V20 PRO ACTIVO - MODO DEMO</b><br>
• Esperando tus datos de Point Smart amarilla para cobros reales<br>
• Terminal: <b>NO CONECTADA (DEMO)</b> | Impresora: <b>{persist['impresora']}</b> | AutoStart: <b>{'SI' if persist['autostart'] else 'NO'}</b><br>
• Ventas hoy: {persist['ventas_hoy']} | Total: ${persist['total_cobrado']}
</div>
<div class='tap-hint'>🔒 CONFIG OCULTA: 5 toques rápidos en esquina + 6to toque sostenido 5-7 segundos (En versión Windows .EXE real)</div>
""", unsafe_allow_html=True)

# --- CONFIGURACION COMPLETA (lo que pediste) ---
with st.expander(f"⚙️ ABRIR CONFIGURACION - PRECIO, LOGO, COLOR, PROGRAMA, IMPRESORA, AUTOSTART", expanded=False):
    st.markdown("<div class='config-header'>PANEL DE CONTROL TOTAL</div>", unsafe_allow_html=True)
    st.caption("Aquí cambias todo lo que pediste. En el .EXE real se entra con 5 toques + hold.")

    tab1, tab2, tab3, tab4 = st.tabs(["💰 COBRO Y LECTOR", "🎨 LOGO Y COLOR", "🖥️ PROGRAMA E IMPRESORA", "⚙️ SISTEMA Y DEMO"])

    with tab1:
        colA, colB = st.columns(2)
        nuevo_precio = colA.number_input("💵 Precio que cobra el kiosko", value=persist['precio'], min_value=10, max_value=1000, step=5, help="Este es el precio que ve el cliente")
        moneda = colB.selectbox("Moneda", ["MXN $", "USD $"], index=0)
        lector_tipo = st.selectbox("Tipo de lector de tarjetas", ["Mercado Pago Point Smart Amarilla (Demo actual)", "Mercado Pago Point Smart Amarilla (Real - cuando me pases token)", "Lector USB genérico", "Solo efectivo (no tarjeta)"])
        st.markdown(f"""
        <div class='log-box'>
        > Lector configurado: {lector_tipo}<br>
        > Precio configurado: ${nuevo_precio} {moneda}<br>
        > Modo: {'DEMO - Simula cobro' if persist['modo_demo']
