import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title='FOTO MONCLOVA', layout='centered')

# LEER SI VIENE DESBLOQUEADO POR GESTO SECRETO
params = st.query_params
if params.get('unlock') == '1':
    st.session_state.mostrar_config = True

if 'precio' not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = 'MONCLOVA'
    st.session_state.programa = 'C:/Kiosko/EGX/Foto.exe'
    st.session_state.impresora = 'EPSON L8050'
    st.session_state.ventas = 0
    st.session_state.ganancia = 0
    st.session_state.estado = 'ESPERA'
    st.session_state.mostrar_config = False

# CSS - 48px PARA QUE NO SE ROMPA LA A
c01 = '<style>'
c02 = '.stApp{background:#050505;}'
c03 = '.t1{font-size:48px;color:#E30613;'
c04 = 'text-align:center;font-weight:900;margin:0;}'
c05 = '.t2{font-size:48px;color:white;'
c06 = 'text-align:center;font-weight:900;margin:0;}'
c07 = '.sub{font-size:9px;letter-spacing:4px;'
c08 = 'color:#333;text-align:center;margin-top:6px;}'
c09 = '.card{background:#121212;border:1px solid #222;'
c10 = 'border-radius:24px;padding:28px;'
c11 = 'text-align:center;margin:16px 0;}'
c12 = '.price{font-size:90px;color:white;'
c13 = 'font-weight:900;text-align:center;}'
c14 = '</style>'
st.markdown(c01+c02+c03+c04+c05+c06+c07+c08+c09+c10+c11+c12+c13+c14, unsafe_allow_html=True)

# ZONA SECRETA INVISIBLE - SIN TEXTO - 5 TOQUES + 6TO SOSTENIDO 5-6s
h01 = '<div id=z style=width:100%;height:35px;'
h02 = 'background:#050505;border-radius:0;'
h03 = 'display:block;></div>'
h04 = '<div id=s style=display:none;></div>'
h05 = '<div id=b style=width:0%;height:2px;'
h06 = 'background:#111;margin-top:0;></div>'
h07 = '<script>let t=0,l=0,h=null,hs=0,hd=false;'
h08 = 'const z=document.getElementById("z");'
h09 = 'const s=document.getElementById("s");'
h10 = 'const b=document.getElementById("b");'
h11 = 'z.addEventListener("touchstart",g);'
h12 = 'z.addEventListener("mousedown",g);'
h13 = 'function g(e){e.preventDefault();'
h14 = 'let n=Date.now();if(n-l>2500)t=0;l=n;'
h15 = 'if(t<5){t++;'
h16 = 'if(t==5){b.style.background="gold";'
h17 = 'b.style.width="30%";}return;}'
h18 = 'if(t>=5&&!hd){hd=true;hs=Date.now();'
h19 = 'h=setInterval(()=>{let el=(Date.now()-hs)/1000;'
h20 = 'b.style.background="#E30613";'
h21 = 'b.style.width=Math.min(el/5*100,100)+"%";'
h22 = 'if(el>=5&&el<=7){clearInterval(h);'
h23 = 'window.parent.location.href='
h24 = 'window.parent.location.pathname+"?unlock=1";'
h25 = '}},80);}}'
h26 = 'function u(){if(hd){clearInterval(h);hd=false;'
h27 = 'let el=(Date.now()-hs)/1000;'
h28 = 'if(el<5){t=0;b.style.width="0%";'
h29 = 'b.style.background="#111";}}}'
h30 = 'z.addEventListener("touchend",u);'
h31 = 'z.addEventListener("mouseup",u);</script>'

html = h01+h02+h03+h04+h05+h06+h07+h08+h09+h10
html = html+h11+h12+h13+h14+h15+h16+h17+h18+h19+h20
html = html+h21+h22+h23+h24+h25+h26+h27+h28+h29+h30+h31

components.html(html, height=40)

st.markdown('<div class=t1>FOTO</div>', unsafe_allow_html=True)
st.markdown('<div class=t2>'+st.session_state.logo+'</div>', unsafe_allow_html=True)
st.markdown('<div class=sub>RECUERDOS EN 15 SEGUNDOS</div>', unsafe_allow_html=True)

# SOLO SI ESTA DESBLOQUEADO POR GESTO SECRETO
if st.session_state.mostrar_config:
    st.success('CONFIG - Gesto 5 + 6to hold 5-6s OK')
    p = st.number_input('Precio', value=st.session_state.precio, min_value=10, max_value=500, step=5)
    l = st.text_input('Logo 2da linea', value=st.session_state.logo)
    prog = st.text_input('Programa EGX', value=st.session_state.programa)
    imp = st.selectbox('Impresora', ['EPSON L8050','EPSON L805','Canon Selphy'])
    if st.button('GUARDAR Y OCULTAR', type='primary', use_container_width=True):
        st.session_state.precio = p
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.query_params.clear()
        st.session_state.mostrar_config = False
        st.rerun()
    if st.button('SALIR CONFIG', use_container_width=True):
        st.query_params.clear()
        st.session_state.mostrar_config = False
        st.rerun()
else:
    # KIOSCO NORMAL SIN NINGUNA INSTRUCCION DE CONFIG
    st.markdown('<div class=card><div class=price>$'+str(st.session_state.precio)+'</div></div>', unsafe_allow_html=True)
    est = st.session_state.estado
    if est == 'ESPERA':
        txt = 'PAGAR $'+str(st.session_state.precio)+' CON TARJETA'
        if st.button(txt, use_container_width=True, type='primary'):
            st.session_state.estado = 'COBRANDO'
            st.rerun()
    if est == 'COBRANDO':
        with st.spinner('Point Smart...'):
            time.sleep(1)
        st.session_state.estado = 'APROBADO'
        st.rerun()
    if est == 'APROBADO':
        st.session_state.ventas += 1
        st.session_state.ganancia += st.session_state.precio
        st.success('APROBADO $'+str(st.session_state.precio))
        st.info(st.session_state.programa)
        if st.button('FOTO TOMADA', use_container_width=True, type='primary'):
            st.session_state.estado = 'IMPRIMIENDO'
            st.rerun()
    if est == 'IMPRIMIENDO':
        st.warning(st.session_state.impresora)
        if st.button('ENTREGADA', type='primary', use_container_width=True):
            st.session_state.estado = 'ESPERA'
            st.rerun()

st.caption('V39 SECRETO - 5 toques + 6to hold 5-6s - sin instrucciones visibles')
