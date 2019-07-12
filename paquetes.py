import random
from  random import sample
import collections
import matplotlib.pyplot as plt
import numpy as np
K    = 10   #TAMAÑO DEL ARREGLO 
NMAX = 5   # PESO MAXIMO DE UN PAQUETE 
M    = 20  # TAMAÑO DEL BUFFER 
TMAX = 8  # NUMERO DE INDIVIDUOS, POBLACION MAXIMA
T0   = 2   # POBLACIÓN INICIAL
CDPO = 50  # % PARA DETENER EL CICLO
CRUZA = 1

PORCENTA = int(( TMAX * CDPO ) / 100)
print(PORCENTA)
paquetes = dict()
maximos = []
minimos = []
promedios = []

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
PARAR = False
parar = 0 
while PARAR != True :
#cruza
    for i in range(T0):
        for j in range(i+1,T0):
              
            poblacion.append(poblacion[i][0:int(K/2)]+poblacion[j][int(K/2):K])
            poblacion.append(poblacion[j][0:int(K/2)]+poblacion[i][int(K/2):K])
    i = T0
    iAux = T0+1
    valores = []
    continuar = False
    while i < len(poblacion):
        for j in range(K):
            if poblacion[i].count(poblacion[i][j]) > 1:
                valores.append(poblacion[i][j])
                jAux = 0
                while jAux < K:
                    print("here aqui")
                    if poblacion[iAux].count(poblacion[iAux][jAux]) > 1:
                        valores.append(poblacion[iAux][jAux])
                        poblacion[i][j] = valores[1]
                        poblacion[iAux][jAux] = valores[0]
                        valores = []
                        continuar = True
                        break
                    jAux+=1
        if continuar == True:
            i+=1
        if iAux+1 < len(poblacion):
            iAux+=1
        print("here")
    

    pos = []
    valores = []
    num_intercambios = random.randint(0,int(K/2))
    for i in range(len(poblacion)):
        for j in range(num_intercambios):
            lista_random = sample(range(0,K-1),2)
            valores.append(poblacion[i][lista_random[0]])
            valores.append(poblacion[i][lista_random[1]])
            poblacion[i][lista_random[0]] = valores[1]
            poblacion[i][lista_random[1]] = valores[0]
            valores = []

    totales = []
    ganancias = []
    ganancias_count = 0
    for i in range(len(poblacion)):
        aux_total_paquete = 0
        for j in range(K):
            if (aux_total_paquete + paquetes[poblacion[i][j]]) <= M:
                aux_total_paquete += paquetes[poblacion[i][j]]
                ganancias_count +=1
            else:
                break
        poblacion[i].append(aux_total_paquete)
        poblacion[i].append(ganancias_count+aux_total_paquete)
        aux_total_paquete = 0
        ganancias_count = 0

    poblacion.sort(key=lambda poblacion: poblacion[K+1])

    for i in range(len(poblacion)):
        print(poblacion[i])

    mini = min(poblacion, key=lambda poblacion: poblacion[K+1])
    maxi = max(poblacion, key=lambda poblacion: poblacion[K+1])
    promedio = 0
    for i in range(len(poblacion)):
        promedio += poblacion[i][K+1]
    promedio /=len(poblacion)

    promedios.append(promedio)
    maximos.append(maxi[K+1])
    minimos.append(mini[K+1])
    
    
    print(maximos.pop())
    if poblacion[0].count(maxi[K+1]) >= PORCENTA:
        PARAR = True

    for i in range(len(poblacion)):
        poblacion[i].pop()
        poblacion[i].pop()

    #poda
    print("Valor de pablacion: ",len(poblacion))
    for i in range(0,(len(poblacion)-TMAX)):
        print("Quitar: ",i)
        poblacion.pop(i)

    T0 = len(poblacion)
    print("T0: ",T0)
    parar +=1


################ 


plt.plot(minimos, marker='x', linestyle=':', color='b', label = "Minimos")
plt.plot(promedios, marker='*', linestyle='-', color='g', label = "Promedios")
plt.plot(maximos, marker='o', linestyle='--', color='r', label = "Maximos")
plt.legend(loc="upper left")
plt.show()



    




        
            
    
    


                    





    
    
    









