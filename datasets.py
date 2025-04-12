#Data sets pandas
import pandas as pd

#Cargar el dataset
dataset = pd.read_csv('E:/Programacion/Python/PythonDataScience/Pandas/datasets/all_pokemon_data.csv')
#print(dataset)

#ver primeras filas del dataset
print(dataset.head())

#buscar nombre y caracteristicas de Pokemon
print(dataset['Name'])

#utilizar rangos - buscar los pokemones con ataque mayor a 50
print(dataset['Attack']>50)

#usando un filtro
filtrar = (dataset['Speed']>60)
print(dataset[filtrar])
