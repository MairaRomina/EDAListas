class Nodo:
    __elemento = int
    __izq = None
    __der = None

    def __init__(self, elemento):
        self.__elemento = elemento
        self.__der = None
        self.__izq = None

    def getIzq(self):
        return self.__izq

    def getDer(self):
        return self.__der

    def getElemento(self):
        return self.__elemento

    def setDer(self,nodo):
        self.__der = nodo

    def setIzq(self,nodo):
        self.__izq = nodo