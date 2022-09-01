import numpy as np

class Cola:
    __arreglo = None
    __maximo = int
    __primero = int
    __ultimo = int
    __cantidad = int

    def __init__(self, max): #maximo = 7
        self.__arreglo = np.empty(max, dtype = int)
        self.__primero = 0 #3 - 4
        self.__ultimo = 0 #4 - 5 - 6 - 0
        self.__cantidad = 0 #1 - 2 - 1 - 2 - 3
        self.__maximo = max

    def insertar (self, elemento):
        if self.__cantidad < self.__maximo:
            self.__arreglo[ self.__ultimo ] = elemento
            self.__ultimo = (self.__ultimo + 1) % self.__maximo
            self.__cantidad += 1
            return elemento
        else:
            return 0

    def suprimir (self):
        x = 0
        if not self.vacia():
            x = self.__arreglo[ self.__primero ] #3
            self.__primero = (self.__primero + 1) % self.__maximo #apunta al siguiente elemento
            self.__cantidad -= 1 #1
            return x
        else:
            print("Pila vacia")
            return 0

    def recorrer (self):
        i = 0
        j = 0
        if not self.vacia():
            i = self.__primero
            j = 0
            for j in range(0, self.__cantidad, 1):
                print("elemento ", (j + 1) , " es ",self.__arreglo[i])
                i = (i + 1) % self.__maximo

    def vacia (self):
        return self.__cantidad == 0