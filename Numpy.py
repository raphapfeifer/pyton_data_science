import numpy as np

km = np.loadtxt(fname = "C:/Users/rapha/alura/Python_Data_Science/Numpy/data/carros-km.txt")

#print(km)

anos = np.loadtxt(fname ="C:/Users/rapha/alura/Python_Data_Science/Numpy/data/carros-anos.txt", dtype = int)

valor = np.loadtxt(fname ="C:/Users/rapha/alura/Python_Data_Science/Numpy/data/carros-valor.txt")

#print(valor)


dataset = np.column_stack((anos,km,valor))
#print(dataset)

#print(dataset.shape)

print(np.mean(dataset[:]))

print(np.mean(dataset))

#print(np.std(dataset[:,2]))

#print(dataset.sum(axis = 0))

#print(dataset[:,2].sum())


#km_media = km / (2019 - anos)

#print('resultado: {}'.format(km_media))

#print(type(km_media))