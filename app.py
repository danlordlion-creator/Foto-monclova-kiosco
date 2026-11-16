# KIOSKO V12 PRO - FOTO MONCLOVA - DISEÑO CHINGON + COBRO
import tkinter as tk
from tkinter import filedialog, colorchooser
import subprocess, os, json, sys
import time
from datetime import datetime

CONFIG_FILE = "C:/Kiosko/config.json"

# --- CONFIG DEFAULT ---
default_config = {
    "precio": 40,
    "color": "#E30613",
    "logo_text": "FOTO MONCLOVA",
    "programa_fotos": "C:/Kiosko/Fotos.exe",
    "impresora": "Default",
    "autostart": False,
    "modo_demo": True,
    "mp_token": "",
    "mp_device": ""
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return {**default_config, **json.load(f)}
        except:
            return default_config
    return default_config

def save_config(cfg):
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=4)

config = load_config()

# --- AUTOSTART ---
def set_autostart(enable):
    bat_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup\\kiosko.bat')
    if enable:
        with open(bat_path, "w") as f:
            f.write(f'@echo off\npython "{os.path.abspath(__file__)}"\n')
    else:
        if os.path.exists(bat_path):
            os.remove(bat_path)

# --- APP PRINCIPAL ---
class KioskoApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.toques = 0
        self.last_tap_time = 0
        self.hold_job = None

        # UI
        self.header = tk.Frame(root, bg='black')
        self.header.pack(fill='x', pady=20)
        tk.Label(self.header, text="FOTO", font=("Bebas Neue", 60, "bold"), fg=config["color"], bg='black').pack()
        tk.Label(self.header, text="MONCLOVA", font=("Bebas Neue", 60, "bold"), fg='white', bg='black').pack()

        self.center = tk.Frame(root, bg='black')
        self.center.pack(expand=True)

        self.precio_label = tk.Label(self.center, text=f"${config['precio']}", font=("Arial", 80, "bold"), fg='white', bg='black')
        self.precio_label.pack()

        tk.Label(self.center, text="TOCA PARA PAGAR CON TARJETA", font=("Arial", 16), fg='#888', bg='black').pack(pady=10)

        self.btn_pagar = tk.Button(self.center, text=f"PAGAR ${config['precio']} 💳", font=("Arial", 28, "bold"),
                                   bg=config["color"], fg='white', activebackground='white', activeforeground='black',
                                   width=18, height=2, bd=0, relief='flat', command=self.proceso_cobro)
        self.btn_pagar.pack(pady=30)

        self.status = tk.Label(root, text="MODO DEMO - Esperando cliente" if config["modo_demo"] else "ACTIVO - Terminal Lista",
                               font=("Arial", 12), fg='lime' if not config["modo_demo"] else 'yellow', bg='black')
        self.status.pack(side='bottom', pady=20)

        # GESTO SECRETO: 5 toques + hold
        self.root.bind("<Button-1>", self.detectar_toque)
        self.btn_hold = tk.Button(root, text="", bg='black', bd=0, activebackground='black')
        self.btn_hold.place(x=0, y=0, width=100, height=100) # esquina para gestos
        self.btn_hold.bind("<ButtonPress-1>", self.iniciar_hold)
        self.btn_hold.bind("<ButtonRelease-1>", self.cancelar_hold)

    def detectar_toque(self, e):
        ahora = time.time()
        if ahora - self.last_tap_time > 2: # resetea si pasan 2 seg
            self.toques = 0
        self.toques += 1
        self.last_tap_time = ahora
        # print(f"Toque {self.toques}")

    def iniciar_hold(self, e):
        if self.toques >= 5:
            self.hold_job = self.root.after(5000, self.abrir_config) # 5 seg sostenido

    def cancelar_hold(self, e):
        if self.hold_job:
            self.root.after_cancel(self.hold_job)
            self.hold_job = None
            self.toques = 0

    def abrir_config(self):
        self.toques = 0
        ConfigWindow(self.root)

    def proceso_cobro(self):
        self.status.config(text="COBRANDO...", fg='yellow')
        self.root.update()
        time.sleep(1.5) # Simula lector

        if config["modo_demo"] or self.cobrar_real():
            self.status.config(text="PAGO APROBADO - ABRIENDO FOTOS...", fg='lime')
            self.root.update()
            self.abrir_programa_fotos()
        else:
            self.status.config(text="PAGO RECHAZADO", fg='red')
            self.root.after(2000, lambda: self.status.config(text="ACTIVO", fg='lime'))

    def cobrar_real(self):
        # Aquí irá tu Point Smart cuando me pases token
        import requests
        try:
            url = f"https://api.mercadopago.com/point/integration-api/devices/{config['mp_device']}/payment-intents"
            headers = {"Authorization": f"Bearer {config['mp_token']}"}
            data = {"amount": config["precio"]*100, "description": "Foto Monclova"}
            r = requests.post(url, json=data, headers=headers, timeout=10)
            return r.status_code in [200,201]
        except:
            return False

    def abrir_programa_fotos(self):
        try:
            # Minimiza cobro
            self.root.iconify()
            # Abre el programa que configuraste
            proc = subprocess.Popen([config["programa_fotos"]])
            proc.wait() # ESPERA HASTA QUE SE CIERRE EL DE FOTOS
            
            # Cuando regresa, detecta impresión
            self.detectar_impresion_y_regresar()
        except Exception as e:
            print(e)
            self.root.deiconify()
            self.status.config(text=f"Error abriendo: {config['programa_fotos']}", fg='red')

    def detectar_impresion_y_regresar(self):
        # Aquí detecta cola de impresión
        self.status.config(text="ESPERANDO IMPRESION...", fg='yellow')
        self.root.deiconify()
        self.root.attributes('-fullscreen', True)
        # Simula esperar a que termine de imprimir
        time.sleep(2)
        self.status.config(text="¡FOTO IMPRESA! REGRESANDO A COBRO", fg='lime')
        self.root.after(2000, lambda: self.status.config(text="ACTIVO - Esperando cliente", fg='lime'))

class ConfigWindow:
    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.configure(bg='#111')
        self.win.attributes('-fullscreen', True)
        
        tk.Label(self.win, text="CONFIGURACION - FOTO MONCLOVA", font=("Arial", 20, "bold"), fg='white', bg='#111').pack(pady=20)

        frm = tk.Frame(self.win, bg='#111')
        frm.pack(pady=20)

        # Precio
        tk.Label(frm, text="Precio:", fg='white', bg='#111').grid(row=0, column=0, padx=10, pady=10, sticky='e')
        self.e_precio = tk.Entry(frm, font=("Arial", 16))
        self.e_precio.insert(0, str(config["precio"]))
        self.e_precio.grid(row=0, column=1)

        # Programa fotos
        tk.Label(frm, text="Programa Fotos (.exe):", fg='white', bg='#111').grid(row=1, column=0, padx=10, pady=10, sticky='e')
        self.e_prog = tk.Entry(frm, font=("Arial", 12), width=35)
        self.e_prog.insert(0, config["programa_fotos"])
        self.e_prog.grid(row=1, column=1)
        tk.Button(frm, text="Buscar...", command=self.buscar_exe).grid(row=1, column=2, padx=5)

        # Color
        tk.Label(frm, text="Color Principal:", fg='white', bg='#111').grid(row=2, column=0, padx=10, pady=10, sticky='e')
        self.btn_color = tk.Button(frm, bg=config["color"], width=10, command=self.elegir_color)
        self.btn_color.grid(row=2, column=1, sticky='w')

        # Impresora
        tk.Label(frm, text="Impresora:", fg='white', bg='#111').grid(row=3, column=0, padx=10, pady=10, sticky='e')
        self.e_print = tk.Entry(frm, font=("Arial", 12), width=35)
        self.e_print.insert(0, config["impresora"])
        self.e_print.grid(row=3, column=1)

        # Autostart
        self.var_auto = tk.BooleanVar(value=config["autostart"])
        tk.Checkbutton(frm, text="Auto Start con Windows", variable=self.var_auto, fg='white', bg='#111', selectcolor='black').grid(row=4, column=1, pady=10, sticky='w')

        # Guardar
        tk.Button(self.win, text="GUARDAR Y CERRAR", font=("Arial", 20, "bold"), bg=config["color"], fg='white', width=20, command=self.guardar).pack(pady=30)
        tk.Button(self.win, text="CANCELAR", bg='gray', fg='white', command=self.win.destroy).pack()

    def buscar_exe(self):
        path = filedialog.askopenfilename(filetypes=[("EXE", "*.exe")])
        if path:
            self.e_prog.delete(0, tk.END)
            self.e_prog.insert(0, path)

    def elegir_color(self):
        c = colorchooser.askcolor()[1]
        if c:
            self.btn_color.config(bg=c)
            config["color"] = c

    def guardar(self):
        config["precio"] = int(self.e_precio.get())
        config["programa_fotos"] = self.e_prog.get()
        config["impresora"] = self.e_print.get()
        config["autostart"] = self.var_auto.get()
        save_config(config)
        set_autostart(config["autostart"])
        self.win.destroy()
        # Reinicia app para aplicar cambios
        python = sys.executable
        os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    root = tk.Tk()
    app = KioskoApp(root)
    root.mainloop()
