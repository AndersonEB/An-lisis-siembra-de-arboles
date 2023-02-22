#- FILTRO2: Filtrar todos los datos de Caucasia e interpretar sus estadísticas
import pandas  as pd
data= pd.read_csv("./Siembras (5).csv")

#print(data)

filtro2 = data[data["Ciudad"]== "Caucasia"].describe()
print(filtro2)

archivoHTML=filtro2.to_html()
archivo=open("tablafiltro2.html","w", encoding="utf-8")
archivo.write(archivoHTML)
archivo.close()



#analisis
# Se puede analizar que el número promedio de árboles es de 12,040 en un área promedio de 28.63 hectáreas, con una desviación estándar muy alta de 41,371 árboles y 82.7 hectáreas. También se puede observar que la cantidad mínima de árboles es de 32, y la cantidad máxima 185823.