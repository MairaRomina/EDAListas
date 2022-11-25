import numpy as np

class Digrafo:
    __vertices = None
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
            print(self.__matriz)
        else:
            print("no se pudo insertar")
    
    # def sumidero (self):
    #     fila = 0
    #     col = 0
    #     nodos = []
    #     contf = 0
    #     contc = 0
    #     while fila < len(self.__vertices) and col < len(self.__vertices):
    #         contf = 0
    #         contc = 0
    #         for i in range(len(self.__matriz)):
    #             if self.__matriz[fila][i] == 0:
    #                 contf += 1
    #                 print("contf", contf)
            
    #         for j in range(len(self.__matriz[fila])):
    #             if self.__matriz[j][col] == 0:
    #                 contc += 1
    #                 print("contc", contc)
            
    #         if contf == len(self.__vertices) and contc != len(self.__vertices):
    #             print("nodo sumidero")
    #             print(self.__vertices[fila])
    #             nodos.append(self.__vertices[fila])

    #         fila += 1
    #         col += 1
    #     print(nodos)

    def gradoE (self, nodo):
        cont = 0
        j = self.buscar(nodo) #j fija 
        for i in range(4):
            if self.__matriz[i][j] != 0: #me muevo por columnas
                cont += 1
        if cont == 0:
            return cont
        else:
            return cont
    
    def gradoS (self, nodo):
        cont = 0
        i = self.buscar(nodo) #i fija
        for j in range(4):
            if self.__matriz[i][j] != 0: #me muevo por filas
                cont += 1
        if cont == 0:
            return cont
        else:
            return cont
    
    def fuente (self):
        for i in range(4):
            s = self.gradoS(self.__vertices[i])
            e = self.gradoE(self.__vertices[i])
            if e == 0 and s >= 1: #si el grado de entrada = 0 y grado de salida >= 1 es fuente
                print("nodo fuente")
                print("vertice ",self.__vertices[i])
    
    def sumidero (self):
        for i in range(4):
            s = self.gradoS(self.__vertices[i])
            e = self.gradoE(self.__vertices[i])
            if e >= 1 and s == 0: #si el grado de entrada >= 1 y grado de salida = 0 es sumidero
                
                print("nodo sumidero")
                print("vertice ",self.__vertices[i])
    
    def adyacentes (self, nodo):
        i = self.buscar(nodo)
        lista = []
        for j in range(4):
            if self.__matriz[i][j] == 1:
                lista.append( self.__vertices[j] )
        return lista
        
    def camino (self, nodoI, nodoF, recorrido = []):
        if nodoI == nodoF:
            return [nodoF]
        else:
            recorrido.append(nodoI)

            for nodo in self.adyacentes(nodoI):
                if nodo not in recorrido:
                    recorrido.append(nodo)
                    camino = self.camino(nodo, nodoF, recorrido)
                    if camino != None:
                        return [nodoI]+camino
            raise Exception("No hay camino")

if __name__ == '__main__':
    digrafo = Digrafo([1,2,3,4])
    digrafo.insertar(2,1)
    digrafo.insertar(2,4)
    digrafo.insertar(3,1)
    digrafo.insertar(3,4)
    digrafo.insertar(4,1)
    digrafo.insertar(4,2)
    #digrafo.sumidero()
    digrafo.gradoE(1)
    digrafo.gradoS(1)
    digrafo.fuente()
    digrafo.sumidero()
    print("adyacentes",digrafo.adyacentes(1))
    print(digrafo.camino(1,4,[]))
