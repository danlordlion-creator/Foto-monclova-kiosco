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
    st.session_state.estado = "ESPERA"
    st.session_state.mostrar_config = False

p1 = "<style>"
p2 = ".stApp{background:#050505;}"
p3 = ".t1{font-size:70px;color:#E30613;text-align:center;font-weight:900;}"
p4 = ".t2{font-size:70px;color:white;text-align:center;font-weight:900;}"
p5 = ".card{background:#141414;border-radius:24px;padding:25px;text-align:center;margin:20px 0;}"
p6 = ".price{font-size:90px;color:white;font-weight:900;text-align:center;}"
p7 = "</style>"
st.markdown(p1 + p2 + p3 + p4 + p5 + p6 + p7, unsafe_allow_html=True)

# HTML SIN TRIPLES
h1 = "<div id=zona style=width:100%;height:45px;background:#111;border-radius:10px;display:flex;align-items:center;justify-content:center;>"
h2 = "<span style=color:#333;font-size:10px;>ZONA SECRETA - 5 TOQUES + HOLD 5-6s</span></div>"
h3 = "<div id=status style=color:#555;font-size:11px;margin-top:6px;text-align:center;>Toques: 0/5</div>"
h4 = "<div id=bar style=width:0%;height:4px;background:#E30613;margin-top:4px;></div>"
h5 = "<script>"
h6 = "let t=0,last=0,ht=null,hs=0,hold=false;"
h7 = "const z=document.getElementById('zona'),s=document.getElementById('status'),b=document.getElementById('bar');"
h8 = "z.addEventListener('touchstart',go);z.addEventListener('mousedown',go);"
h9 = "function go(e){e.preventDefault();let n=Date.now();if(n-last>3000)t=0;last=n;"
h10 = "if(t<5){t++;s.innerText='Toques: '+t+'/5';if(t==5){s.innerText='5 TOQUES! Ahora deja oprimido 5-6s';}return;}"
h11 = "if(t>=5&&!hold){hold=true;hs=Date.now();ht=setInterval(()=>{let el=(Date.now()-hs)/1000;"
h12 = "b.style.width=Math.min(el/5*100,100)+'%';s.innerText='SOSTENIDO '+el.toFixed(1)+'s / 5s';"
h13 = "if(el>=5){clearInterval(ht);s.innerText='DESBLOQUEADO - Dale al boton abajo';}},100);}}"
h14 = "function up(){if(hold){clearInterval(ht);hold=false;}}"
h15 = "z.addEventListener('touchend',up);z.addEventListener('mouseup',up);"
h16 = "</script>"

html_final = h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10 + h11 + h12 + h13 + h14 + h15 + h16

components.html(html_final, height=120)

st.markdown('<div class=t1>FOTO</div>', unsafe_allow_html=True)
st.markdown('<div class=t2>' + st.session_state.logo + '</div>', unsafe_allow_html=True)

demo_txt = "DEMO | " + st.session_state.impresora + " | Ventas " + str(st.session_state.ventas)
st.caption(demo_txt)

if st.button("ABRIR CONFIG TRAS 5 TOQUES + HOLD"):
    st.session_state.mostrar_config = True
    st.rerun()

if st.session_state.mostrar_config:
    st.warning
