from claseNodo import Nodo

class Cola:
    __comienzo = None
    __tope = 0

    def __init__(self):
        self.__comienzo = None

    def vacia (self):
        return self.__tope == -1
    
    def insertar (self, elemento):
        if self.__comienzo == None:
            nodo = Nodo(elemento)
            nodo.setSiguiente(None)
            self.__comienzo = nodo
            self.__tope += 1
        else:
            aux = self.__comienzo
            anterior = aux
            while aux != None:
                anterior = aux
                aux = aux.getSiguiente()
            nodo = Nodo(elemento)
            nodo.setSiguiente(None)
            anterior.setSiguiente(nodo)
            self.__tope += 1

    def suprimir (self):
        aux = self.__comienzo
        sig = aux.getSiguiente()
        del self.__comienzo
        self.__comienzo = sig
        
    def mostrar (self):
        if self.vacia() == False:
            aux = self.__comienzo
            while aux != None:
                print(aux.getDato())
                aux = aux.getSiguiente()
                self.suprimir()