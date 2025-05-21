import pandas as pd
import re

# Cargar los archivos
bloques_df = pd.read_csv("bloques_address.csv")
emails_df = pd.read_csv("proveedores_extraidos.csv")

# Verificación básica
if len(bloques_df) != len(emails_df):
    raise ValueError("Los archivos no tienen la misma cantidad de filas.")

# Extraer datos del bloque de texto
proveedores = []
telefonos = []
emails = emails_df["Email"].tolist()  # Lista de emails

for i, row in bloques_df.iterrows():
    texto = row["AddressBlock"]

    # Extraer proveedor entre 'A/P Acct' y el siguiente número que inicia con 0
    proveedor_match = re.search(r'A/P Acct\s+(.*?)\s+0\d+', texto)
    proveedor = proveedor_match.group(1).strip() if proveedor_match else ''

    # Extraer texto después de 'Pay Type'
    telefono_match = re.search(r'Pay Type\s+(.*)', texto)
    telefono = telefono_match.group(1).strip() if telefono_match else ''

    proveedores.append(proveedor)
    telefonos.append(telefono)

# Crear nuevo DataFrame
df_final = pd.DataFrame({
    "Proveedor": proveedores,
    "Teléfono": telefonos,
    "Email": emails
})

# Guardar a CSV
df_final.to_csv("proveedores_final.csv", index=False, encoding="utf-8")
print("✅ Archivo 'proveedores_final.csv' generado correctamente.")
