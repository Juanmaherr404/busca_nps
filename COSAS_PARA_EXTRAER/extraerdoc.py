import olefile

# Ruta al archivo .doc que contiene el archivo embebido
doc_file = 'vol2-C..doc_within_doc.doc'

# Abre el archivo .doc para examinar el contenido OLE
ole = olefile.OleFileIO(doc_file)

# Lista los elementos que tiene el archivo .doc
ole.listdir()

# Si encuentras algún objeto incrustado, puedes intentar extraerlo
# En este caso, supongamos que el objeto incrustado es un archivo
# en la carpeta "ObjectPool"
for entry in ole.listdir():
    print(entry)
    if entry == ['ObjectPool', 'File1']:
        with ole.openstream(entry) as file_stream:
            with open('extracted_file.doc', 'wb') as extracted_file:
                extracted_file.write(file_stream.read())

ole.close()
