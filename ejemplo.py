paquetes = dict()
import random
for i in range(1,11):
    paquetes[i] = random.randint(1,5)
print(paquetes) 

poblacion = []
for i in range(3):
    indices    = list(paquetes.keys())
    random.shuffle(indices) 
    poblacion.append(indices)
print(poblacion)