#Data sets pandas
import pandas as pd

#Cargar el dataset
dataset = pd.read_csv('E:/Programacion/Python/PythonDataScience/Pandas/datasets/alumnos.csv', sep=';')
#print(dataset)
print(dataset.head())

#convercion de archivo csv
#convert_file = pd.read_excel('E:/Programacion/Python/PythonDataScience/Pandas/datasets/alumnos.xlsx')
#print(convert_file.head())
#convert_file.to_csv('E:/Programacion/Python/PythonDataScience/Pandas/datasets/alumnos.csv', index=False)

#print(convert_file.head())
print(dataset.iloc[1:3])
print(dataset.iloc[2:3])

#acceder a elementos por nombre
print(dataset.loc[1,'CARRERA'])

#LIMPIAR COLUMNAS EN CASO DE TENER NOMBRES CON ESPACIO O SALTO DE LÍNEA
dataset.columns = dataset.columns.str.strip()
print(dataset.loc[1,'NOMBRE'])
#acceder a elementos por nombre y rango
print(dataset.loc[:3, ['NOMBRE', 'CARRERA']])

#AÑADIR COLUMNAS AL DATAFRAME
dataset['TURNO'] = pd.Series(['Tarde','Noche','Mañana'])
print(dataset)

#ELIMINAR COLUMNAS
GENERO = dataset.pop('GENERO')
print(dataset)

#AÑADIR FILAS
#crear nueva fila como un dataframe
nueva_fila = pd.DataFrame([{
    'NOMBRE': 'Carlos',
    'EDAD': 24,
    'CARRERA': 'Software',
    'SEMESTRE': 8,
    'TURNO': 'Mañana'
}])

#concater la fila
dataset = pd.concat([dataset, nueva_fila], ignore_index=True)
print(dataset)

#Eliminar filas de un dataframe
print(dataset.drop([7]))

#filtrar filas de un dataframe
#busacar que sean mayores a 22 años y que sean de software
print(dataset[(dataset['EDAD']>22) & (dataset['CARRERA']=='Software')])

#Ordenar un dataframe por carrera
print(dataset.sort_values('CARRERA'))

# ordenar por edades
print(dataset.sort_values('EDAD'))

#Omitir los nullos
print(dataset.dropna())