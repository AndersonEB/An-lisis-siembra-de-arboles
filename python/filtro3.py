import pandas as pd

data=pd.read_csv("Siembras.csv")
print(data)


filtro3=data[(data['Vereda'] == "La Salazar")|(data["Vereda"] == 'Rio Arriba')]
print(filtro3)

archivoHtml=filtro3.to_html()
with open("./tablaFiltro3.html","wb") as f:
    f.write(bytes(archivoHtml, encoding='utf-8'))