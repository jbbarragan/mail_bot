import fitz
import re
import pandas as pd

doc = fitz.open("proveedores.pdf")
data_list = []

for page in doc:
    text = page.get_text()

    # Buscar el bloque que inicia con la empresa y termina justo antes de Phone
    match = re.search(
        r'(?<=Address\s)(.*?)(?=Phone)',
        text,
        re.DOTALL
    )

    if match:
        block = match.group(1).strip()
        # Opcional: convertir saltos de línea a espacios o mantenerlos
        block = re.sub(r'\n+', ' ', block)  # Para una línea
        # block = match.group(1).strip()   # Si prefieres mantener saltos de línea
    else:
        block = ''

    data_list.append({'AddressBlock': block})

df = pd.DataFrame(data_list)
df.to_csv("bloques_address.csv", index=False, encoding="utf-8")

print("✅ ¡Bloque correcto extraído y guardado en 'bloques_address.csv'!")
