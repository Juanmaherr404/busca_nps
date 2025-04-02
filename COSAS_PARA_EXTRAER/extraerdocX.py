import zipfile
import os

# Ruta al archivo .docx que contiene otro .docx
docx_file = 'vol2-C..docx_within_docx.docx'

# Crear una carpeta para extraer el contenido
output_folder = 'extracted_content'
os.makedirs(output_folder, exist_ok=True)

# Abrir el archivo .docx principal
with zipfile.ZipFile(docx_file, 'r') as docx_zip:
    # Lista los archivos dentro del .docx
    docx_zip.printdir()

    # Extraer todo el contenido del .docx en la carpeta
    docx_zip.extractall(output_folder)

# Verifica los archivos extraídos
print(f"Contenido extraído a: {output_folder}")
