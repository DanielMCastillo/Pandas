#series con pandas
import pandas as pd
numeros = pd.Series([1,2,3,4,5])
print(numeros)

#funcion suma en series
print(numeros.sum())
#valor maximo en serie
print(numeros.max())
#valor minimo en serie
print(numeros.min())
#valor promedio en serie
print(numeros.mean())
#valor mediana en serie
print(numeros.median())
#valor varianza en serie
print(numeros.var())
#valor desviacion estandar en serie
print(numeros.std())


#ejempplo series
serie = pd.Series({'Matematicas': 90, 'Historia': 85, 'Ciencias': 95})
#filtar valores
print(serie[serie > 85])
#ordenar elementos de serie
print(serie.sort_values(ascending=False))

#crear una serie usando valor escalar
#se crea una serie con 10 elementos con el valor 5
serie = pd.Series(5, index=range(10))
print(serie)

# pasando indice usando arrays
data_list = ['Messi', 'Cristiano', 'Neymar']
indice = ['Barcelona','Real Madrid','PSG']
seriefutbol = pd.Series(data_list, index=indice)
print(seriefutbol)



