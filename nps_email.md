# NPS_EMAIL

## Abrimos Autopsy

```bash
sudo autopsy
```

## Como acceder a una imagen de un disco

1. Creamos un caso

2. Creamos un host para el caso

3. Añadimos la imagen que queremos analizar

4. Analizamos la imagen en este caso fat16

5. Entramos en Analizar de archivos

## Empezamos a buscar email

1. EMAIL en c:/document1.txt

```plaintext
plain_text@textedit.com
```

2. EMAIL en document2.pdf -> Exportar

```plaintext
plain_text_pdf@textedit.com
```

3. EMAIL en document3.pdf -> Exportar

```plaintext
plain_utf16_pdf@textedit.com
```

4. EMAIL en testfilex.pdf -> Exportar

```plaintext
This is a test --- user_docx_pdf@microsoftword.com
```

5. EMAIL en document2.rtf

```plaintext en 
rtf_text@textedit.com
```

6. EMAIL en docx_within_docx.docx, he ejecutado extraerdoc.py -> docx que esta en extracted_content/word/embeddings

```plaintext en 
docx_within_docx@document.com
```

7. EMAIL en myfile.zip -> exportar y descomprimir con unzip

```plaintext
email_in_zip@zipfile1.com
```

8. EMAIL en myfile22.zip -> exportar y descomprimir con unzip y volver a descomprimir

```plaintext
email_in_zip_zip@zipfile2.com
```

9. EMAIL en iwork_09.pages -> exportamos y convertimos en un zip -> descomprimimos -> ver el .pdf que genera

```bash
unzip iwork_09.zip -d iwork_extracted
evince iwork_extracted/QuickLook/Preview.pdf
```

```plaintext
pages@iwork09.com
```

10. EMAIL en myfilegzip.txt.gz -> descomprimimos el archivo -> abrimos el .txt

```bash
gunzip -c ./vol2-C..myfilegzip.txt.gz 
```
```plaintext
email_in_gzip@gzipfile.com                         
```

11. EMAIL en workbook1.xls -> abrimos en una aplicacion online que soporte .xls

```plaintext
xls_cell@microsoft_excel.com
```

12. EMAIL en workbook2.xlsx > abrimos en una aplicacion online que soporte .xlsx

```plaintext
xlsx_cell@microsoft_excel.com
```