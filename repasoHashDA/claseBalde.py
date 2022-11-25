import numpy as np
from claseNodo import Nodo
from math import trunc

class Registro:
    __arreglo = None
    __dimension = int
    __indice = int

    def __init__ (self):
        self.__dimension = 4
        self.__arreglo = np.full(self.__dimension, None)
        self.__indice = 0
    
    def getDato(self, indice):
        return self.__arreglo[indice]
    
    def agregar (self, dato):
        self.__arreglo[self.__indice] = dato
        self.__indice += 1
    
    def getIndice (self):
        return self.__indice
    
    def lleno (self):
        return self.__dimension < self.__indice
    
    def getRegistro (self):
        return self.__arreglo

class HashBalde:
    __arreglo = None
    __dimension = int
    __overflow = int

    def __init__ (self, clave):
        cant = trunc(clave / 4)
        self.__dimension = self.primo( cant )
        self.__arreglo = np.full( self.__dimension, None )
        
    

