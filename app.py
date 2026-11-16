import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title="FOTO MONCLOVA", layout="centered")

if "precio" not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = "FOTO MONCLOVA"
    st.session_state.programa = "C:/Kiosko/EGX/Foto.exe"
    st.session_state.impresora = "EPSON L8050"
    st.session_state.ventas = 0
    st.session_state.ganancia = 0
    st.session_state.estado = "ESPERA"
    st.session_state.mostrar_config = False
    st.session_state.auto_start = True

# CSS SEGURO EN PARTES CORTAS
a1 = "<style>"
a2 = ".stApp{background:#080808;}"
a3 = ".t1{font-size:68px;color:#E30613;text-align:center;font-weight:900;margin:0;line-height:0.9;}"
a4 = ".t2{font-size:68px;color:white;text-align:center;font-weight:900;margin:0;line-height:0.9;}"
a5 = ".sub{font-size:10px;letter-spacing:5px;color:#666;text-align:center;margin-top:5px;}"
a6 = ".card{background:#121212;border:1px solid #222;border-radius:28px;padding:30px;text-align:center;margin:20px 0;}"
a7 = ".price{font-size:100px;color:white;font-weight:900;text-align:center;line-height:1;}"
a8 = ".lbl{color:#E30613;font-size:10px;letter-spacing:4px;text-align:center;font-weight:900;}"
a9 = ".box{background:#151515;border-left:4px solid gold;border-radius:10px;padding:10px;font-size:11px;color:#888;}"
a10 = "</style>"

st.markdown(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10, unsafe_allow_html=True)

# GESTO SECRETO 5 TOQUES + HOLD 5-6s - SIN TRIPLE COMILLAS
h1 = '<div id=zona style=width:100%;height:48px;background:#111;border:1px dashed #222;border-radius:12px;display:flex;align-items:center;justify-content:center;>'
h2 = '<span style=color:#333;font-size:10px;>ZONA SECRETA - 5 TOQUES RAPIDOS + HOLD 5-6s</span></div>'
h3 = '<div id=status style=color:#555;font-size:12px;margin-top:8px;text-align:center;>Toques: 0/5</div>'
h4 = '<div id=bar style=width:0%;height:5px;background:#E30613;margin-top:5px;border-radius:3px;></div>'
h5 = '<script>'
h6 = 'let t=0,last=0,ht=null,hs=0,hold=false;'
h7 = 'const z=document.getElementById("zona"),s=document.getElementById("status"),b=document.getElementById("bar");'
h8 = 'z.addEventListener("touchstart",go);z.addEventListener("mousedown",go);'
h9 = 'function go(e){e.preventDefault();let n=Date.now();if(n-last>3000)t=0;last=n;'
h10 = 'if(t<5){t++;s.innerText="Toques: "+t+"/5";if(t==5){s.innerText="5 TOQUES! Ahora manten oprimido 5-6 seg";s.style.color="gold";}return;}'
h11 = 'if(t>=5&&!hold){hold=true;hs=Date.now();ht=setInterval(()=>{let el=(Date.now()-hs)/1000;'
h12 = 'b.style.width=Math.min(el/5*100,100)+"%";s.innerText="SOSTENIDO "+el.toFixed(1)+"s / 5s";'
h13 = 'if(el>=5){clearInterval(ht);s.innerText="DESBLOQUEADO - Presiona boton abajo";s.style.color="#0f8";}},100);}}'
h14 = 'function up(){if(hold){clearInterval(ht);hold=false;let el=(Date.now()-hs)/1000;'
h15 = 'if(el<5){s.innerText="Falto "+el.toFixed(1)+"s - Debe 5-6s";setTimeout(()=>{t=0;s.innerText="Toques: 0/5";b.style.width="0%";s.style.color="#555";},1500);}}}'
h16 = 'z.addEventListener("touchend",up);z.addEventListener("mouseup",up);'
h17 = '</script>'

html_full = h1+h2+h3+h4+h5+h6+h7+h8+h9+h10+h11+h12+h13+h14+h15+h16+h17

components.html(html_full, height=130)

# TITULO
st.markdown('<div class=t1>FOTO</div>', unsafe_allow_html=True)
st.markdown('<div class=t2>' + st.session_state.logo + '</div>', unsafe_allow_html=True)
st.markdown('<div class=sub>RECUERDOS EN 15 SEGUNDOS - MONCLOVA COAHUILA</div>', unsafe_allow_html=True)

# INFO DEMO
info_txt = "DEMO | " + st.session_state.impresora + " | " + st.session_state.programa + " | Ventas " + str(st.session_state.ventas) + " | $" + str(st.session_state.ganancia)
st.markdown('<div class=box>' + info_txt + '</div>', unsafe_allow_html=True)

# BOTON CONFIRMACION HOLD
if st.button("YA HICE 5 TOQUES + HOLD 5-6s - ABRIR CONFIG"):
    st.session_state.mostrar_config = True
    st.rerun()

# CONFIGURACION COMPLETA
if st.session_state.mostrar_config:
    st.error("CONFIGURACION DESBLOQUEADA - 5 toques + hold 5-6s")
    tab1, tab2, tab3 = st.tabs(["COBRO Y POINT", "DISENO E IMPRESION", "SISTEMA KIOSCO"])
    with tab1:
        p = st.number_input("Precio recuerdo MXN", value=st.session_state.precio, min_value=10, max_value=500, step=5)
        st.caption("Lector: Point Smart amarilla - Se conecta via API MercadoPago")
        st.checkbox("Cobro con tarjeta activado", value=True)
    with tab2:
        l = st.text_input("Texto logo kiosco", value=st.session_state.logo)
        imp = st.selectbox("Impresora", ["EPSON L8050","EPSON L805","Canon Selphy CP1500","Default Windows"])
        st.caption("Impresion automatica al tomar foto - Regresa a cobro al terminar")
    with tab3:
        prog = st.text_input("Ruta programa fotos .EXE que abre al cobrar", value=st.session_state.programa)
        auto = st.checkbox("Auto Start con Windows (kiosco)", value=st.session_state.auto_start)
        st.caption("
