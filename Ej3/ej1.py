from claseNodo import Nodo

class Pila:
    __comienzo = None
    __tope = 0

    def __init__(self):
        self.__comienzo = None

    def vacia (self):
        return self.__tope == -1
    
    def insertar (self, elemento):
        nodo = Nodo(elemento)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__tope += 1
    
    def convertir (self, num):
        valor = num
        while valor > 0:
            #print(valor)
            self.insertar(valor)
            valor -= 1

    def suprimir (self):
        aux = self.__comienzo
        sig = aux.getSiguiente()
        del self.__comienzo
        self.__comienzo = sig
        
    def mostrar (self):
        total = 1
        if self.vacia() == False:
            aux = self.__comienzo
            while aux != None:
                total *= aux.getDato()
                print(aux.getDato())
                aux = aux.getSiguiente()
                self.suprimir()
            print("el total fue ", total)