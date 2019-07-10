from genetico import Genetico
import random
import collections
K    = 10   #TAMAÑO DEL ARREGLO 
NMAX = 5   # PESO MAXIMO DE UN PAQUETE 
M    = 20  # TAMAÑO DEL BUFFER 
TMAX = 8  # NUMERO DE INDIVIDUOS, POBLACION MAXIMA
T0   = 5   # POBLACIÓN INICIAL
CDPO = 50  # % PARA DETENER EL CICLO

paquetes = dict()

#generar paquetes
for i in range(K):
    paquetes[i] = random.randint(1,NMAX)
print("Paquetes: ",paquetes)

poblacion = []

#generar poblacion inicial
for i in range(T0):
    indices    = list(paquetes.keys()) # generar un arreglo con el tamaño K
    random.shuffle(indices)  # hacer un random con las posiciones
    poblacion.append(indices) # generar la población

print("Poblacion inicial:",poblacion)

#cruza
for i in range(T0):
    for j in range(i+1,T0):
        poblacion.append(poblacion[i][0:int(K/2)]+poblacion[j][int(K/2):K])
        poblacion.append(poblacion[j][0:int(K/2)]+poblacion[i][int(K/2):K])

for i in range(len(poblacion)):
    print(poblacion[i],": ",i)


'''for x in range(len(lista[0])):
    if(lista[0].count(lista[0][x]) > 1):
        index1 = lista[0].index(lista[0][x])
        valor1 = lista[0][x]
    if(lista[1].count(lista[1][x]) > 1):
        index2 = lista[1].index(lista[1][x])
        valor2 = lista[1][x]
    lista[0][index1] = valor2
    lista[1][index2] = valor1

print(lista)
valores = [1,2,3,4,5,6,7,8,9,10]
print(len([x for x, y in collections.Counter(valores).items() if y > 1]))'''

print(collections.Counter(poblacion[5]).items()) 
        


    
    
    









