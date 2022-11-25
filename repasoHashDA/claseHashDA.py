import numpy as np
import math

class Hash:
    __arreglo = None  #direccionamiento abierto
    __dimension = int

    def __init__ (self, claves):
        cant = claves / 0.7 
        self.__dimension = self.primo( math.trunc(cant) )
        self.__arreglo = np.full( self.__dimension, None )
    
    def es_primo(self,num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

    def primo(self,num):
        band=True
        while band:
            if( self.es_primo(num) ):
                band=False
            else:
                num+=1
        return num
    
    def insertar (self, elemento):
        pos = elemento % self.__dimension #metodo division para calcular la posicion
        if self.__arreglo[ pos ] == None:
            self.__arreglo[ pos ] = elemento
        else:
            aux = pos
            while self.__arreglo[ aux ] != None and aux != pos:
                aux = (aux + 1) % self.__dimension
            if aux != pos and self.__arreglo[ aux ] == None:
                self.__arreglo[ aux ] = elemento
            else:
                print("error al insertar")
    
    def mostrar (self):
        for variable in self.__arreglo:
            print(variable)
    
    # def insertar(self, elemento):
    #     num = int(elemento[2] + elemento[3]) #metodo extraccion
    #     pos = num % self.__dimension
    #     if self.__arreglo[ pos ] == None:
    #         self.__arreglo[ pos ] = elemento
    #     else:
    #         aux = pos
    #         while self.__arreglo[ aux ] != None and aux != pos:
    #             aux = (aux + 1) % self.__dimension
    #         if aux != pos and self.__arreglo[ aux ] == None:
    #             self.__arreglo[ aux ] = elemento
    #         else:
    #             print("error al insertar")

    # def insertar(self, elemento):
    #     num = int(elemento[0] + elemento[1]) + int(elemento[2] + elemento[3]) #metodo plegado
    #     pos = num % self.__dimension
    #     if self.__arreglo[ pos ] == None:
    #         self.__arreglo[ pos ] = elemento
    #     else:
    #         aux = pos
    #         while self.__arreglo[ aux ] != None and aux != pos:
    #             aux = (aux + 1) % self.__dimension
    #         if aux != pos and self.__arreglo[ aux ] == None:
    #             self.__arreglo[ aux ] = elemento
    #         else:
    #             print("error al insertar")
    
    def buscar(self,elemento):
        pos = elemento % self.__dimension
        if self.__arreglo[pos] == elemento:
            retorna = self.__arreglo[pos]
        else:
            aux1 = pos 
            while(self.__arreglo[aux1] != None and pos != aux1):
                    aux1 = (aux1 + 1) % self.__dimension
            if pos != aux1:
                retorna = self.__arreglo[aux1]
            else:
                retorna = None
                print("elemento no encontrado")
        return retorna

#metodo cuadrado medio 1551 --> 55 --> 5+5 = 10 = pos
if __name__ == '__main__':
    arreglo = Hash( 10 )
    arreglo.insertar( 1551 )
    arreglo.insertar( 2552 )
    arreglo.insertar( 3553)
    arreglo.insertar( 4554 )
    arreglo.insertar( 5555 )
    arreglo.mostrar()
    print("buscar ", arreglo.buscar(2552))