import pandas as pd
tabla = pd.read_csv("./Siembras.csv")
filtro4= tabla[(tabla["Vereda"]=="Quitasol")]
print (filtro4)

archivoHTML=filtro4.to_html()
archivo=open("tablafiltro4.html","w", encoding="utf-8")
archivo.write(archivoHTML)
archivo.close()