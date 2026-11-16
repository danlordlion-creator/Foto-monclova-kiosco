# FOTO MONCLOVA V20 ULTRA LARGO - FIX SyntaxError - SIN FILTROS NI MARCOS
import streamlit as st
from datetime import datetime
import time
import json
import os

st.set_page_config(page_title="FOTO MONCLOVA KIOSKO", page_icon="📸", layout="centered")

CONFIG_PATH = "kiosko_config.json"
def load_persist():
    try:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, "r") as f:
                return json.load(f)
    except:
        pass
    return {"precio": 40, "color": "#E30613", "logo_text": "FOTO MONCLOVA", "programa": "C:/Kiosko/EGX/Foto.exe", "impresora": "EPSON L8050", "autostart": True, "modo_demo": True, "ventas_hoy": 0}

def save_persist(data):
    try:
        with open(CONFIG_PATH, "w") as f:
            json.dump(data, f)
    except:
        pass

persist = load_persist()
color_main = persist['color']

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Montserrat:wght@400;700&display=swap');
.stApp {{ background: radial-gradient(circle at top, #1e1e1e 0%, #000 100%); }}
h1 {{ font-family: 'Bebas Neue' !important; text-align:center !important; color:white !important; font-size:85px !important; margin:0 !important; line-height:0.85 !important; }}
.subtitle {{ text-align:center; color:#666; font-family:Montserrat; letter-spacing:10px; font-size:11px; }}
.price-container {{ background: linear-gradient(180deg, #181818, #0e0e0e); border:1.5px solid #232323; border-radius:35px; padding:35px 20px; margin:25px 0; text-align:center; }}
.price {{ font-family:'Bebas Neue'; font-size:110px;
