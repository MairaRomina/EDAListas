import numpy as np
from math import trunc
from claseNodo import Nodo

class HashE:
    __arreglo = None
    __dimension = int

    def __init__ (self, claves):
        cant = trunc( claves / 4 )
        self.__dimension = self.primo( cant )
        print(self.__dimension)
        self.__arreglo = np.full( self.__dimension, None )
    
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
    
    def insertar(self, elemento):
        pos = elemento % self.__dimension
        if self.__arreglo[pos] == None:
            self.__arreglo[pos] = Nodo( elemento )
        else:
            aux = self.__arreglo[pos]
            ant = aux
            while aux != None:
                ant = aux
                aux = aux.getSig()
            if aux == None:
                ant.setSig( Nodo( elemento ) )
            else:
                print("error al insertar nodos")
    
    def buscar(self, elemento):
        pos = elemento % self.__dimension
        if self.__arreglo[pos] == None:
            print("error, nada cargado")
        else:
            if self.__arreglo[pos].getDato() == elemento:
                print("elemento encontrado", self.__arreglo[pos].getDato())
            else:
                aux = self.__arreglo[pos]
                bandera = True
                while bandera and aux != None:
                    if aux.getDato() == elemento:
                        bandera = False
                    else:
                        aux = aux.getSig()
                if bandera == False and aux != None:
                    print("elemento encontrado", aux.getDato())
                else:
                    print("no encontrado")

    def mostrar(self):
        for i in range(self.__dimension):
            aux=self.__arreglo[i]
            print(i,end="\t")
            while(aux!=None):
                print(aux.getDato(),end="\t")
                aux=aux.getSig()
            print("")

if __name__ == '__main__':
    tabla = HashE(20)
    tabla.insertar(50)
    tabla.insertar(95)
    tabla.insertar(80)
    tabla.insertar(56)
    tabla.insertar(78)
    tabla.mostrar()
    tabla.buscar(100)
