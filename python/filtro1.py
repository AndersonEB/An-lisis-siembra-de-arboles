import pandas as pd

bd = pd.read_csv('../Siembras.csv')

columns = bd.columns.values
print(columns)

print('\n')
print('FILTRO1: Encontrar todos los datos de santa fe de Antioquia donde se tengan siembras de + de 250 arboles')

mas250arboles = bd[(bd["Ciudad"] == "Santa Fe de Antioquia") & (bd["Arboles"]>250)]
print(mas250arboles)



archivoHTML = mas250arboles.to_html()
with open("../tablas/tabla1.html", 'wb') as f:
    f.write(bytes(archivoHTML, encoding= 'utf-8'))