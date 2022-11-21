import numpy as np
from math import trunc

class HashBuckets:
    __matriz = None
    __contador = None #arreglo banderas
    __overflow = int
    __dimension = int

    def __init__ (self, claves):
        cant = trunc(claves / 4)
        print("cant",cant)
        self.__overflow = cant #marco la zona de comienzo de overflow
        cant+=(10*cant)/100
        print("overflow", self.__overflow)
        self.__dimension = self.primo(  trunc(cant)  )
        print("dimension",self.__dimension)
        self.__matriz = np.full((self.__dimension,4), None)
        self.__contador = np.full(self.__dimension,0)

                
    def Insertar(self,elemento):
        posicion = elemento % self.__dimension
        if self.__contador[posicion] < 4:
            self.__matriz[posicion][self.__contador[posicion]]=elemento
            self.__contador[posicion]+=1
        else:
            aux=self.__overflow
            band=True
            while aux<self.__dimension and band:
                if self.__contador[aux] < 4:
                    self.__matriz[aux][self.__contador[aux]]=elemento
                    self.__contador[aux]+=1
                    band=False
                else:
                    aux+=1

    def Buscar(self, elemento):
        posicion = elemento % self.__dimension
        aux = 0
        while aux < 4 and self.__matriz[posicion][aux] != elemento:
            aux += 1 
        if aux < 4 and self.__matriz[posicion][aux] == elemento:
            print("elemento encontrado en la matriz")
        else:
            aux = self.__overflow
            band = True
            j = 0
            while band and aux < self.__dimension:
                while band and j < 4:
                    if self.__matriz[aux][j] == elemento:
                        band = False
                    else:
                        j += 1
                aux += 1
            if band == False:
                print("elemento encontrado")
            else:
                print("no se encontro")
                    
    def es_primo(self,num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

    def primo(self,num):
        band=True
        while band:
            if( self.es_primo(num) ):
                band=False
            else:
                num+=1
        return num
    
    def mostrar (self):
        print(self.__matriz, end="\t")
        print(self.__contador)

if __name__ == '__main__':
    tabla = HashBuckets(40)
    tabla.Insertar(5)
    tabla.Insertar(3)
    tabla.Insertar(4)
    tabla.Insertar(5)
    tabla.Insertar(5)
    tabla.Insertar(5)
    tabla.Insertar(5)
    tabla.Insertar(16)
    tabla.mostrar()
    tabla.Buscar(16)
