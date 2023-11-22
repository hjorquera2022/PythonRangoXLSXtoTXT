import pandas as pd

# Nombre del archivo Excel
archivo_excel = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\01 PARCIALIDADES\\0002-01 PAVIMENTACION AREA AVIONES\\CONTROL DOCUMENTOS ING DEF P0002-01.xlsx'
archivo_txt   = 'C:\\Users\\hjorquera\\Desktop\\Minuta explicativa planimetria de repositorio\\01 PARCIALIDADES\\0002-01 PAVIMENTACION AREA AVIONES\\SALIDA.ACTUALIZA EDITABLE DOC VIG.TXT'
# Nombre de la hoja que deseas leer
nombre_hoja = 'ACTUALIZA EDITABLE DOC VIG'  

# Filas y columnas que deseas extraer (por ejemplo, de la A1 a la A100)
rango = 'A1:A10'

# Lee el archivo Excel en un DataFrame
df = pd.read_excel(archivo_excel, sheet_name=nombre_hoja)

with open(archivo_txt, 'w') as archivo_texto:
    for valor in df['RUTA']:
        archivo_texto.write(str(valor) + '\n')
        print(valor)


print(f'Se ha creado el archivo "salida.txt" con el rango.')



