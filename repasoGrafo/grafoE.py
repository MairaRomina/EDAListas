import numpy as np
from claseNodo import Nodo

class GrafoE:
    __arreglo = None
     
    def __init__ (self, lista):
        self.__arreglo = np.empty(len(lista), dtype=Nodo)
        for i in range(len(self.__arreglo)):
            self.__arreglo[i] = Nodo( lista[i] )
    
    def insertar (self, nodoA, nodoB): #1 , 4
        if nodoA <= len(self.__arreglo) and nodoB <= len(self.__arreglo) and nodoA != nodoB:
            if self.__arreglo[nodoA-1].getSig() == None:
                self.__arreglo[nodoA-1].setSig( Nodo( nodoB ))
                self.__arreglo[nodoB-1].setSig( Nodo( nodoA ))
            else:
                aux = self.__arreglo[nodoA-1]
                ant = aux
                while aux != None:
                    ant = aux
                    aux = aux.getSig()
                if aux == None:
                    ant.setSig( Nodo(nodoB) )
                else:
                    print("error al insertar")

                aux = self.__arreglo[nodoB-1]
                ant = aux
                while aux != None:
                    ant = aux
                    aux = aux.getSig()
                if aux == None:
                    ant.setSig( Nodo(nodoA) )
                else:
                    print("error al insertar")
        else:
            print("vertice no existente")

    def mostrar (self):
        for i in range(4):
            print("arreglo")
            print(self.__arreglo[i].getDato())
            aux = self.__arreglo[i].getSig()
            while aux != None:
                print("lista")
                print(aux.getDato())
                aux = aux.getSig()

if __name__ == '__main__':
    grafo = GrafoE([1,2,3,4])
    
    grafo.insertar( 1,4 )
    
    grafo.mostrar()
    