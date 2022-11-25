import numpy as np

class GrafoS:
    __vertices = []
    __matriz = None

    def __init__ (self, lista):
        self.__vertices = lista
        cant = len(lista)
        self.__matriz = np.full( (cant,cant), 0 )
        print(self.__matriz)
        print(self.__vertices)
    
    def buscar (self, dato):
        i = 0
        bandera = True
        while bandera and i < len(self.__vertices):
            if self.__vertices[i] == dato:
                bandera = False
            else:
                i += 1
        if self.__vertices[i] == dato:
            return i
        else:
            return None

    def insertar (self, A, B):
        i = self.buscar( A )
        j = self.buscar( B )
        if i != None and j != None:
            self.__matriz[i][j] = 1
            self.__matriz[j][i] = 1
            print(self.__matriz)
        else:
            print("no se pudo insertar")


if __name__ == '__main__':
    grafo = GrafoS([1,2,3,4])
    grafo.insertar( 1, 3 )


