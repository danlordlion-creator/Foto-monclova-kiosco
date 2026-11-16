import streamlit as st
import streamlit.components.v1 as components
import time

st.set_page_config(page_title='FOTO MONCLOVA', layout='centered')

if 'precio' not in st.session_state:
    st.session_state.precio = 40
    st.session_state.logo = 'FOTO MONCLOVA'
    st.session_state.programa = 'C:/Kiosko/EGX/Foto.exe'
    st.session_state.impresora = 'EPSON L8050'
    st.session_state.ventas = 0
    st.session_state.ganancia = 0
    st.session_state.estado = 'ESPERA'
    st.session_state.mostrar_config = False
    st.session_state.auto_start = True

# CSS LARGO CHINGON PERO EN CACHITOS CORTOS
c01 = '<style>'
c02 = '.stApp{background:#050505;}'
c03 = '.t1{font-size:72px;color:#E30613;'
c04 = 'text-align:center;font-weight:900;'
c05 = 'margin:0;line-height:0.85;}'
c06 = '.t2{font-size:72px;color:white;'
c07 = 'text-align:center;font-weight:900;'
c08 = 'margin:0;line-height:0.85;}'
c09 = '.sub{font-size:10px;letter-spacing:5px;'
c10 = 'color:#666;text-align:center;}'
c11 = '.card{background:radial-gradient(#1a1a1a,#0a0a0a);'
c12 = 'border:1px solid #222;border-radius:28px;'
c13 = 'padding:32px;text-align:center;margin:18px 0;}'
c14 = '.price{font-size:110px;color:white;'
c15 = 'font-weight:900;text-align:center;line-height:1;}'
c16 = '.lbl{color:#E30613;font-size:10px;'
c17 = 'letter-spacing:4px;text-align:center;font-weight:900;}'
c18 = '.info{background:#111;border-left:4px solid gold;'
c19 = 'border-radius:8px;padding:10px;color:#888;font-size:11px;}'
c20 = '</style>'

css = c01+c02+c03+c04+c05+c06+c07+c08+c09+c10
css = css+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20
st.markdown(css, unsafe_allow_html=True)

# GESTO 5 TOQUES + HOLD 5-6s EN CACHITOS
h01 = '<div id=z style=width:100%;height:48px;'
h02 = 'background:#111;border-radius:12px;'
h03 = 'display:flex;align-items:center;'
h04 = 'justify-content:center;>'
h05 = '<span style=color:#444;font-size:10px;>'
h06 = 'ZONA SECRETA - 5 TOQUES + HOLD 5s</span></div>'
h07 = '<div id=s style=color:#666;font-size:12px;'
h08 = 'text-align:center;margin-top:6px;>'
h09 = 'Toques: 0/5</div>'
h10 = '<div id=b style=width:0%;height:5px;'
h11 = 'background:#E30613;margin-top:5px;></div>'
h12 = '<script>let t=0,l=0,h=null,hs=0,hd=false;'
h13 = 'const z=document.getElementById("z");'
h14 = 'const s=document.getElementById("s");'
h15 = 'const b=document.getElementById("b");'
h16 = 'z.addEventListener("touchstart",g);'
h17 = 'z.addEventListener("mousedown",g);'
h18 = 'function g(e){e.preventDefault();'
h19 = 'let n=Date.now();if(n-l>3000)t=0;l=n;'
h20 = 'if(t<5){t++;s.innerText="Toques: "+t+"/5";'
h21 = 'if(t==5){s.innerText="5 OK - ahora manten 5s";'
h22 = 's.style.color="gold";}return;}'
h23 = 'if(t>=5&&!hd){hd=true;hs=Date.now();'
h24 = 'h=setInterval(()=>{let el=(Date.now()-hs)/1000;'
h25 = 'b.style.width=Math.min(el/5*100,100)+"%";'
h26 = 's.innerText="Hold "+el.toFixed(1)+"s /5s";'
h27 = 'if(el>=5){clearInterval(h);'
h28 = 's.innerText="DESBLOQUEADO - boton abajo";'
h29 = 's.style.color="#0f8";}},100);}}'
h30 = 'function u(){if(hd){clearInterval(h);hd=false;'
h31 = 'let el=(Date.now()-hs)/1000;'
h32 = 'if(el<5){s.innerText="Falto "+el.toFixed(1)+"s";'
h33 = 'setTimeout(()=>{t=0;s.innerText="Toques: 0/5";'
h34 = 'b.style.width="0%";},1500);}}}'
h35 = 'z.addEventListener("touchend",u);'
h36 = 'z.addEventListener("mouseup",u);</script>'

html = h01+h02+h03+h04+h05+h06+h07+h08+h09+h10
html = html+h11+h12+h13+h14+h15+h16+h17+h18+h19+h20
html = html+h21+h22+h23+h24+h25+h26+h27+h28+h29+h30
html = html+h31+h32+h33+h34+h35+h36

components.html(html, height=135)

# TITULOS
st.markdown('<div class=t1>FOTO</div>', unsafe_allow_html=True)
st.markdown('<div class=t2>'+st.session_state.logo+'</div>', unsafe_allow_html=True)
st.markdown('<div class=sub>RECUERDOS EN 15 SEGUNDOS - MONCLOVA COAHUILA</div>', unsafe_allow_html=True)

inf = 'DEMO | '+st.session_state.impresora+' | '
inf = inf+st.session_state.programa+' | Ventas '
inf = inf+str(st.session_state.ventas)+' | $'+str(st.session_state.ganancia)
st.markdown('<div class=info>'+inf+'</div>', unsafe_allow_html=True)

if st.button('YA HICE 5 TOQUES + HOLD 5s - ABRIR CONFIG'):
    st.session_state.mostrar_config = True
    st.rerun()

# CONFIG COMPLETA LARGA
if st.session_state.mostrar_config:
    st.error('CONFIG DESBLOQUEADA - 5 toques + hold OK')
    tab1, tab2, tab3 = st.tabs(['COBRO', 'DISENO', 'SISTEMA'])
    with tab1:
        p = st.number_input('Precio MXN', value=st.session_state.precio, min_value=10, max_value=500, step=5)
        st.caption('Point Smart amarilla - API MercadoPago')
    with tab2:
        l = st.text_input('Texto logo', value=st.session_state.logo)
        imp = st.selectbox('Impresora', ['EPSON L8050','EPSON L805','Canon Selphy'])
    with tab3:
        prog = st.text_input('Ruta programa EGX .EXE', value=st.session_state.programa)
        auto = st.checkbox('Auto Start Windows', value=st.session_state.auto_start)
    if st.button('GUARDAR TODO Y OCULTAR', type='primary', use_container_width=True):
        st.session_state.precio = p
        st.session_state.logo = l
        st.session_state.programa = prog
        st.session_state.impresora = imp
        st.session_state.auto_start = auto
        st.session_state.mostrar_config = False
        st.rerun()
    if st.button('REINICIAR VENTAS DIA', use_container_width=True):
        st.session_state.ventas = 0
        st.session_state.ganancia = 0
        st.rerun()

# KIOSCO FULL LARGO
if st.session_state.mostrar_config == False:
    st.markdown('<div class=card><div class=lbl>PRECIO HOY</div><div class=price>$'+str(st.session_state.precio)+'</div><div class=lbl>POINT SMART AMARILLA</div></div>', unsafe_allow_html=True)
    est = st.session_state.estado
    if est == 'ESPERA':
        txt = 'PAGAR $'+str(st.session_state.precio)+' CON TARJETA - TOCAR'
        if st.button(txt, use_container_width=True, type='primary'):
            st.session_state.estado = 'COBRANDO'
            st.rerun()
    if est == 'COBRANDO':
        with st.spinner('Conectando Point Smart...'):
            time.sleep(1.2)
        st.session_state.estado = 'APROBADO'
        st.rerun()
    if est == 'APROBADO':
        st.session_state.ventas = st.session_state.ventas + 1
        st.session_state.ganancia = st.session_state.ganancia + st.session_state.precio
        st.success('PAGO APROBADO $'+str(st.session_state.precio))
        st.info('ABRIENDO: '+st.session_state.programa)
        st.warning('Cliente: Tomese foto - 15 seg')
        if st.button('FOTO TOMADA - IMPRIMIR', use_container_width=True, type='primary'):
            st.session_state.estado = 'IMPRIMIENDO'
            st.rerun()
        if st.button('CANCELAR VENTA', use_container_width=True):
            st.session_state.estado = 'ESPERA'
            st.rerun()
    if est == 'IMPRIMIENDO':
        st.warning('IMPRIMIENDO EN '+st.session_state.impresora)
        with st.spinner('Imprimiendo...'):
            time.sleep(1.5)
        st.success('IMPRESION TERMINADA')
        if st.button('ENTREGADA - REGRESAR A COBRO', type='primary', use_container_width=True):
            st.session_state.estado = 'ESPERA'
            st.rerun()

st.caption('V37 FULL LARGO - Point + EGX + EPSON + Kiosco + 5 toques hold 5-6s')
