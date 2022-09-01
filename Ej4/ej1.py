#from claseNodo import Nodo

class Pila:
    __lista = []
    __comienzo = None
    __a1 = None
    __a2 = None
    __tope1 = 0
    __tope2 = 0

    def __init__(self, cant):
        self.__lista = [None] * cant
        self.__comienzo = None
        self.__tope2 = cant - 1

    def vacia (self):
        return self.__tope == -1
    
    def insertar (self, elemento, donde):
        print("tope 1 ",self.__tope1 + 1)
        print("tope 2 ",self.__tope2)
        if self.__tope1 <= self.__tope2:
            if donde == 1:
                self.__lista[self.__tope1] = elemento
                self.__a1 = elemento
                self.__tope1 += 1
            else:
                self.__lista[self.__tope2] = elemento
                self.__a2 = elemento
                self.__tope2 -= 1
        else:
            print("no se puede insertar")

    def suprimir (self):
        if self.vacia():
            print("lista vacia")
        else:
            self.__lista.pop()
        
    def mostrar (self):
        #if self.vacia() == False:
            for elemento in self.__lista:
                print(elemento)
                #self.suprimir()