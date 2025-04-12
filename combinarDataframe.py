#combina dataframes
import pandas as pd
DF1 = pd.DataFrame({'AUTOS':['Nissan','Ford','Audi'],
            'COLOR':['Blanco','Axul','Rojo']})

DF2 = pd.DataFrame({'AUTOS':['Toyota','Ford','Audi'],
            'MODELO':['2018','2020','2022']})

#Combinar dataframe
DF = pd.merge(DF1,DF2, on='AUTOS', how='outer')
print(DF)