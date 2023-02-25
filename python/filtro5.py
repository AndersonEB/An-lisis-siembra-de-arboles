import pandas as pd

#Encontrar todos los datos de caramanta donde se tengan siembras de + de 100 arboles
data=pd.read_csv("../Siembras.csv")

filtro5=data[(data["Ciudad"]=="Caramanta") & (data["Arboles"]>100)]
print(filtro5)

archivoHTML=filtro5.to_html()
archivoGenerado=open("../tablas/tabla5.html", "w", encoding="utf-8")
archivoGenerado.write(archivoHTML)
archivoGenerado.close()









