# paquetes = dict()
# import random
# for i in range(1,11):
#     paquetes[i] = random.randint(1,5)
# print(paquetes) 

# poblacion = []
# for i in range(3):
#     indices    = list(paquetes.keys())
#     random.shuffle(indices) 
#     poblacion.append(indices)
# print(poblacion)


import matplotlib.pyplot as plt 
import  numpy as np
import pandas as pd

# lista = [ [5,2,1,5], [5,5,4,1], [2,5,2,5], [5,4,1,5],[5,4,1,5],[5,4,1,5] ]
# col = {1:4, 2:5, 3:2, 4:1}
# # df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# # df2.plot.bar()
# # print(lista)
# df2 = pd.DataFrame(lista, columns=col)

# # df2.plot.bar()

# df2.plot.barh(stacked=True)
# plt.show()


# plt.axes((0.2,0.1,0.7,0.8))  # Creamos los ejes en la posición que queremos
# plt.title(u'Evolución para hoy de los tipos de nubosidad')  # Ponemos un título al gráfico
# plt.broken_barh([(0,10),(3,3), (10,5), (21,3)], (9500, 1000))  # Dibujamos los momentos en que ha habido nubes altas
# plt.broken_barh([(0,24)], (4500, 1000))  # Dibujamos los momentos en que ha habido nubes medias
# plt.broken_barh([(0,9), (12,5), (20,2)], (1500, 1000))  # Dibujamos los momentos en que ha habido nubes bajas
# plt.xlim(-1,25)  # Limitamos el rango de valores del eje x
# plt.yticks([2000, 5000, 10000], ['nubes bajas', 'nubes medias','nubes altas'])  # Colocamos etiquetas en el eje y
# plt.xlabel('t(h)')  # Y finalmente ponemos un título al eje x, el eje de tiempos
# plt.show()


df=pd.DataFrame({'Users': [ 'Bob', 'Jim', 'Ted', 'Jesus', 'James'],
                 'Score': [10,2,5,6,7],})

df = df.set_index('Users')
df.plot(kind='bar',  title='Scores')

plt.show()