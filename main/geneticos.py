import random
from  random import sample
import matplotlib.pyplot as plt
import numpy as np
class Geneticos:

    def __init__(self,k,n_max,m,t_max,t_inicial,porcentaje,cruzar):
        self.porcentaje = int((t_max*porcentaje)/100)
        self.k         = k
        self.n_max     = n_max
        self.t_inicial = t_inicial
        self.cruzar     = cruzar
        self.paquetes  = dict()
        self.minimos   = []
        self.maximos   = []
        self.promedios = []
        self.poblacion_inicial = []
        self.m = m
        self.terminar = False
        self.t_max = t_max
    
    def start(self):
        self.generar_paquetes()
        self.generar_poblacion_incial()
        while self.terminar !=  True:
            self.cruza()
            self.quitarRepetidos()
            self.mutacion()
            self.calcular_totales()
            self.ordenar_poblacion()
            self.maximos_minimos()
            self.promedio()
            self.poda()
            self.terminar = self.condicionParo()
            
            
        print("--------------------------------")
        for i in range(len(self.poblacion_inicial)):
            print(self.poblacion_inicial[i])
        
        print(self.promedios)
        print(self.maximos)
        print(self.minimos)
        

        plt.plot(self.maximos, marker='o', linestyle='--', color='r', label = "Maximos")
        
        plt.plot(self.promedios, marker='*', linestyle='-', color='g', label = "Promedios")

        plt.plot(self.minimos, marker='x', linestyle=':', color='b', label = "Minimos")
        
        plt.legend(loc="upper left")
        plt.ylabel("Ganancias")
        plt.xlabel("Iteraciones")
        plt.show()

    def generar_paquetes(self):
        for i in range(self.k):
            self.paquetes[i] = random.randint(1,self.n_max)

    def generar_poblacion_incial(self):
        for i in range(self.t_inicial):
            indices = list(self.paquetes.keys())
            random.shuffle(indices)
            self.poblacion_inicial.append(indices)

    def condicionParo(self):
        mayorElemento = self.poblacion_inicial[0][self.k+1]
        count = 0
        for i in range(len(self.poblacion_inicial)):
            if mayorElemento == self.poblacion_inicial[i][self.k+1]:
                count=count+1
        if count >= self.porcentaje:
            return True
        return False
    
    def cruza(self):
        for i in range(self.t_inicial):
            for j in range(i+1, self.t_inicial):    
                self.poblacion_inicial.append(self.poblacion_inicial[i][:self.k//2]+self.poblacion_inicial[j][self.k//2:self.k])
                self.poblacion_inicial.append(self.poblacion_inicial[j][:self.k//2]+self.poblacion_inicial[i][self.k//2:self.k])
    
    def mutacion(self):
        self.numero_intercambios = random.randint(0,int(self.k/2))
        for i in range (len(self.poblacion_inicial)):
            for j in range(self.numero_intercambios):
                self.posiciones_random = sample(range(0,self.k-1),2)
                self.valorAux = self.poblacion_inicial[i][self.posiciones_random[0]]
                self.poblacion_inicial[i][self.posiciones_random[0]] = self.poblacion_inicial[i][self.posiciones_random[1]]
                self.poblacion_inicial[i][self.posiciones_random[1]] = self.valorAux
    
    def calcular_totales(self):
        for i in range(len(self.poblacion_inicial)):
            self.total_peso = 0
            self.ganancias   = 0
            for j in range(self.k):
                if (self.total_peso + self.paquetes[self.poblacion_inicial[i][j]]) <= self.m :
                    self.total_peso += self.paquetes[self.poblacion_inicial[i][j]]
                    self.ganancias=self.ganancias+1
                else:
                    break
            self.poblacion_inicial[i].append(self.total_peso)
            self.poblacion_inicial[i].append(self.total_peso+self.ganancias)
    
    def maximos_minimos(self):
        minimo = min(self.poblacion_inicial, key=lambda poblacion: poblacion[self.k+1])
        maximo = max(self.poblacion_inicial, key=lambda poblacion: poblacion[self.k+1])

        self.minimos.append(minimo[self.k+1])
        self.maximos.append(maximo[self.k+1])
    
    def promedio(self):
        self.suma_promedio = 0
        for i in range(len(self.poblacion_inicial)):
            self.suma_promedio += self.poblacion_inicial[i][self.k+1]
        self.prom = self.suma_promedio / len(self.poblacion_inicial)
        self.promedios.append(self.prom)
    
    def ordenar_poblacion(self):
        self.poblacion_inicial.sort(key=lambda poblacion_inicial:poblacion_inicial[self.k+1], reverse = True)
    
    def poda(self):
        if len(self.poblacion_inicial) > self.t_max:
            for i in range(len(self.poblacion_inicial)-1,self.t_max-1,-1):
                self.poblacion_inicial.pop()
    
    def quitarRepetidos(self):
        i = self.t_inicial
        while i < len(self.poblacion_inicial):
            for j in range(self.k):
                if self.hayRepetido(i,j) == True:
                    jAux = self.hayRepetidoSiguiente(i+1)
                    if jAux != False:
                        self.valorAux = self.poblacion_inicial[i][j]
                        self.poblacion_inicial[i][j] = self.poblacion_inicial[i+1][jAux]
                        self.poblacion_inicial[i+1][jAux] = self.valorAux
            i+=1
            if  i+1 == len(self.poblacion_inicial):
                break

    def hayRepetidoSiguiente(self,i):
        if i < len(self.poblacion_inicial): 
            for j in range(self.k):
                if self.hayRepetido(i,j) == True:
                    return j
        return False
    
    def hayRepetido(self,i,j):
        if self.poblacion_inicial[i].count(self.poblacion_inicial[i][j]) > 1:
            return True
        return False

                    

        
