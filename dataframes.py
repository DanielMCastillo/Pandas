#Usando dataframes
import pandas as pd
import numpy as np

data = {'NOMBRE': ['Juan', 'Ana', 'Pedro', 'Maria'], 
        'EDAD': [23, 45, 34, 29],
        'CARRERA': ['Ingenieria', 'Medicina', 'Derecho', 'Arquitectura']}
dataframeAlumnos =pd.DataFrame(data)
print(dataframeAlumnos)

#dataframe a partir de una Lista
datos = [['Juan', 23, 'Ingenieria'], ['Ana', 45, 'Medicina'], ['Pedro', 34, 'Derecho'], ['Maria', 29, 'Arquitectura']]
dataframeEstudiantes = pd.DataFrame(data, columns=['NOMBRE', 'EDAD', 'CARRERA'])
print(dataframeEstudiantes)

# dataframe usando arrays y numpy
d = pd.DataFrame(np.random.randn(4,3), columns=['NOMBRE', 'EDAD', 'CARRERA'])
print(d)

