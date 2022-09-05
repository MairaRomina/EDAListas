from claseNodo import Nodo

class Medio:
    __comienzo = None
    __tope = 0

    def __init__(self):
        self.__comienzo = None

    def insertar (self, elemento): #por contenido se carga ordenada por elemento
        aux = self.__comienzo
        bandera = True
        if self.vacia(): #si la lista esta vacia inserta el nodo 
            nodo = Nodo(elemento)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__tope += 1
        elif elemento <= aux.getDato(): #si el dato es menor a lo que tiene la cabeza lo inserta primero
            nodo = Nodo( elemento )
            nodo.setSiguiente( self.__comienzo )
            self.__comienzo = nodo
            self.__tope += 1
        else:
            ant = aux
            aux = aux.getSiguiente()
            while aux != None and bandera:
                if elemento <= aux.getDato():
                    bandera = not bandera
                else:
                    ant = aux
                    aux = aux.getSiguiente()
            #hace el enlace entre medio o al final
            nodo = Nodo( elemento ) 
            nodo.setSiguiente( aux )
            ant.setSiguiente( nodo )
            
    def suprimir (self, posicion):
        aux = self.__comienzo
        bandera = True
        cont = 0
        if posicion == cont:
            bandera == False
            self.__comienzo = aux.getSiguiente()
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
            while aux != None and bandera:
                if cont == posicion:
                    bandera = not bandera
                else:
                    cont += 1
                    ant = aux
                    aux = aux = aux.getSiguiente()
            if cont == posicion:
                ant.setSiguiente( aux.getSiguiente() )
                del aux
            else:
                return -1
        
    def recuperar (self, posicion):
        aux = self.__comienzo
        bandera = True
        cont = 0
        while aux != None and bandera:
            if posicion == cont:
                bandera = not bandera
            else:
                cont += 1
                aux = aux.getSiguiente()
        if posicion == cont:
            return aux.getDato()

        else:
            return -1

    def buscar (self, elemento):
        aux = self.__comienzo
        bandera = True
        while aux != None and bandera:
            if elemento == aux.getDato():
                bandera = False
            else:
                aux = aux.getSiguiente()
        if elemento == aux.getDato():
            return aux
        else:
            return -1
    
    def primer_elemento (self):
        aux = self.__comienzo
        valor = -1
        if not self.vacia():
            valor = aux.getDato()
        return valor

    def ultimo_elemento (self):
        aux = self.__comienzo
        ant = aux
        while aux != None:
            ant = aux
            aux = aux.getSiguiente()
        return ant.getDato()
    
    def siguiente (self, posicion):
        aux = self.__comienzo
        cont = 0
        while aux != None:
            if cont != posicion:
                cont+= 1
            aux = aux.getSiguiente()
        return aux.getSiguiente()#.getDato()

    def anterior (self, posicion):
        cont = 0
        aux = self.__comienzo
        ant = aux
        while aux != None:
            if cont != posicion:
                cont += 1
            ant = aux
            aux = aux.getSiguiente()
        return ant

    def recorrer (self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()
        
    def crear (self):
        self.__comienzo = None
    
    def vacia (self):
        return self.__tope == 0