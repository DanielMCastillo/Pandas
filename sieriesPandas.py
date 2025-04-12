#Series con Pandas
import pandas as pd

# Serie con indice y valores por defecto
colores = pd.Series(['rojo', 'verde', 'azul', 'amarillo',
'morado'], index=['a', 'b', 'c', 'd', 'e'])

print(colores)

#Creacion de Serie/diccionarios
materias = pd.Series({'matematicas': 10, 'historia': 8, 'ingles': 9, 'programacion': 10})
print(materias)

numeros = pd.Series([1,2,3,4,5,6,7,8,9,10])
# Uso de size
print(numeros.size)
#uso de index
print(numeros.index)
#uso de dtype
print(numeros.dtype)

# Acceso a una serie
print(colores[2])
#con rango
print(colores[2:4])