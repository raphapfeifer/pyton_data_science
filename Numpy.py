import numpy as np

km = np.loadtxt("C:/Users/rapha/alura/Python_Data_Science/Numpy/data/carros-km.txt")

#print(km)

anos = np.loadtxt("C:/Users/rapha/alura/Python_Data_Science/Numpy/data/carros-anos.txt", dtype = int)

#print(anos)

km_media = km / (2019 - anos)

print('resultado: {}'.format(km_media))

print(type(km_media))