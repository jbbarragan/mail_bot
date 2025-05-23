import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import filedialog, Tk
import time
import chardet

def escribir_lento(elemento, texto, campo=""):
    print(f"[~] Escribiendo en '{campo}':")
    for letra in texto:
        elemento.send_keys(letra)
        print(letra, end='', flush=True)
        time.sleep(0.05)
    print()

def leer_csv_con_codificacion(path, skiprows=0):
    try:
        return pd.read_csv(path, skiprows=skiprows)
    except UnicodeDecodeError:
        with open(path, 'rb') as f:
            result = chardet.detect(f.read(10000))
            encoding_detected = result['encoding']
            print(f"[i] Codificación detectada para '{path}': {encoding_detected}")
            return pd.read_csv(path, skiprows=skiprows, encoding=encoding_detected)

# --- Seleccionar archivos ---
Tk().withdraw()
archivo_vencidas = filedialog.askopenfilename(title="Selecciona el archivo de órdenes vencidas")
archivo_proveedores = filedialog.askopenfilename(title="Selecciona el archivo de proveedores")

# --- Leer archivos con manejo de codificación ---
df_vencidas = leer_csv_con_codificacion(archivo_vencidas, skiprows=4)
df_proveedores = leer_csv_con_codificacion(archivo_proveedores)

df_vencidas = df_vencidas[['num_orden_com', 'nombre_proveedor', 'desc_articulo']]
df_proveedores = df_proveedores[['Proveedor', 'Email']]

lista_correos = []

for _, row in df_vencidas.iterrows():
    orden = str(row['num_orden_com'])
    proveedor = str(row['nombre_proveedor']).strip()
    articulo = str(row['desc_articulo'])

    proveedor_info = df_proveedores[df_proveedores['Proveedor'].str.strip().str.lower() == proveedor.lower()]
    if proveedor_info.empty:
        continue

    email = proveedor_info.iloc[0]['Email']
    if pd.isna(email) or not isinstance(email, str) or "@" not in email:
        continue

    lista_correos.append({
        'orden': orden,
        'proveedor': proveedor,
        'articulo': articulo,
        'email': email.strip()
    })

if not lista_correos:
    print("[!] No se encontraron correos válidos para enviar.")
    exit()

print("\n[*] Correos que se enviarán:\n")
for item in lista_correos:
    print(f"- Orden {item['orden']} → {item['email']} (Proveedor: {item['proveedor']})")

input("\n[*] Presiona ENTER para continuar al envío de correos...")

# --- Configurar Selenium ---
servicio = Service()
opciones = webdriver.ChromeOptions()
opciones.add_argument("--start-maximized")
driver = webdriver.Chrome(service=servicio, options=opciones)
wait = WebDriverWait(driver, 20)

# --- Abrir Outlook e iniciar sesión ---
print("[*] Abriendo Outlook e ingresando el correo automáticamente...")
driver.get("https://outlook.office.com/mail/")

try:
    correo_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
    escribir_lento(correo_input, "becario.compras01@ibero.mx", "Correo")
    correo_input.send_keys(Keys.ENTER)
    print("[✓] Correo ingresado. Por favor continúa con la contraseña e inicio de sesión.")
except Exception as e:
    print(f"[!] No se pudo ingresar el correo automáticamente: {e}")

input("[*] Presiona ENTER cuando hayas iniciado sesión correctamente...")

# --- Enviar correos ---
for item in lista_correos:
    orden = item['orden']
    proveedor = item['proveedor']
    articulo = item['articulo']
    email = item['email']

    print(f"\n[+] Redactando correo a {email} por la orden {orden}...")

    driver.get("https://outlook.office.com/mail/deeplink/compose")
    try:
        time.sleep(5)

        para = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][aria-label='Para']")))
        escribir_lento(para, email, "Para")
        time.sleep(1)

        cc = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='textbox'][aria-label='CC']")))
        escribir_lento(cc, "veronica.ylescas@ibero.mx", "CC")
        time.sleep(1)

        asunto = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Agregar un asunto']")))
        asunto_texto = f"Orden {orden} vencida"
        escribir_lento(asunto, asunto_texto, "Asunto")

        cuerpo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Cuerpo del mensaje, presione Alt+F10 para salir']")))
        cuerpo.click()
        time.sleep(1)
        cuerpo_texto = f"""Estimado proveedor:

Por medio del presente correo, le informamos que la orden {orden} correspondiente a los siguientes artículos {articulo} se encuentra VENCIDA.
Es fundamental que la entrega se realice en tiempo y forma. Le recordamos que la Universidad Iberoamericana puede aplicar las sanciones correspondientes por retrasos en la entrega.

Permanecemos al pendiente de su respuesta.

A T E N T A M E N T E 

Adquisiciones
Universidad Iberoamericana
"""
        escribir_lento(cuerpo, cuerpo_texto, "Cuerpo")

        enviar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Enviar (Ctrl+Entrar)']")))
        enviar.click()

        print(f"[✓] Correo enviado a {email} por la orden {orden}")
        time.sleep(5)

    except Exception as e:
        print(f"[!] Error al enviar correo a {email}: {e}")
        continue

# --- Fin ---
print("\n[*] Todos los correos han sido procesados.")
driver.quit()
