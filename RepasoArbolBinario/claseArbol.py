from claseNodo import Nodo

class Arbol:
    __raiz = None

    def __init__ (self):
        self.__raiz = None
    
    def getRaiz (self):
        return self.__raiz
    
    def Insertar(self,nodo,elemento):
        if nodo != None: #pregunto si el arbol no esta vacio
                if elemento < nodo.getElemento(): #pregunto si es mas chico y si puedo asignarlo a la izq
                    if nodo.getIzq() == None:
                        nodo.setIzq(Nodo(elemento))
                    else:
                        self.Insertar(nodo.getIzq(),elemento)
                elif elemento > nodo.getElemento():
                        if nodo.getDer() == None:
                            nodo.setDer(Nodo(elemento))
                        else: 
                            self.Insertar(nodo.getDer(),elemento)
                else:
                    if nodo.getElemento()==elemento:
                        print("El elemento ya se encuentra en el arbol")
        else:
            self.__raiz = Nodo(elemento)
    
    def inOrden (self, nodo):
        if nodo != None:
            self.inOrden( nodo.getIzq() )
            print( nodo.getElemento() )
            self.inOrden( nodo.getDer() )
            
    def Buscar(self,elemento,nodo):
        if nodo != None:
            if elemento < nodo.getElemento():
                return self.Buscar(elemento, nodo.getIzq())
            elif elemento >  nodo.getElemento():
                return self.Buscar(elemento, nodo.getDer())
            else:
                return nodo
        else:
            print("error arbol vacio o no encontrado")
    
    def padre (self, nodoHijo, nodo):
        if nodo != None:
            if nodoHijo > nodo.getElemento():
                if nodo.getDer() != None and nodo.getDer().getElemento() == nodoHijo:
                    return nodo
                else:
                    return self.padre( nodoHijo, nodo.getDer() )
            elif  nodoHijo < nodo.getElemento():
                if nodo.getIzq() != None and nodo.getIzq().getElemento() == nodoHijo:
                    return nodo
                else:
                    return self.padre( nodoHijo, nodo.getIzq() )
            return None
    
    def hermanos (self, nodoA, nodoB, nodo):
        if nodo != None:
            padre1 = self.padre(nodoA, nodo)
            padre2 = self.padre(nodoB, nodo)
            if padre1 == padre2:
                print("son hermanos")
            else:
                print("no son hermanos")
        else:
            print("error arbol vacio")
    
    def hijo (self, nodoHijo, nodoPadre, nodo):
        if nodo != None:
            padre = self.padre(nodoHijo, nodo)
            if padre.getElemento() == nodoPadre:
                print(f"{nodoHijo} es hijo de {nodoPadre}")
            else:
                print(f"{nodoHijo} no es hijo de {nodoPadre}")
    
    def mayor (self, nodo):
        if nodo != None:
            if nodo.getDer() == None:
                print("mayor",nodo.getElemento()) 
            else:
                self.mayor(nodo.getDer())
    
    def menor (self, nodo):
        if nodo != None:
            if nodo.getIzq() == None:
                print("menor",nodo.getElemento())
            else:
                self.menor(nodo.getIzq())
    
    def frontera (self, nodo):
         if nodo != None:
            if nodo.getDer() == None and nodo.getIzq() == None:
                print("nodo frontera", nodo.getElemento())
            else:
                self.frontera(nodo.getIzq())
                self.frontera(nodo.getDer())
    
    def altura (self, nodo, i= 0):
        if nodo != None:
            aux = self.altura(nodo.getDer(), i+1)
            aux1 = self.altura(nodo.getIzq(), i+1)
            return max(aux, aux1)
        else:
            return i
    
    def hoja (self, hoja, nodo):
        if nodo != None:
            if nodo.getElemento() == hoja:
                if nodo.getDer() == None and nodo.getIzq() == None:
                    print("es hoja")
                else:
                    print("no es hoja")
            else:
                self.hoja(hoja,nodo.getIzq())
                self.hoja(hoja,nodo.getDer())

    def nivel (self, nodoN, nodo, i = 0):
        if nodo != None:
            if nodo.getElemento() == nodoN:
                return i
            elif nodoN < nodo.getElemento()  :
                return self.nivel(nodoN, nodo.getIzq(), i+1)
            else:
                return self.nivel(nodoN, nodo.getDer(), i+1)

    def _destino (self, destino, nodo): #se encarga de mostrar el camino
        if nodo != None:
            if destino == nodo.getElemento():
                return str(nodo.getElemento())

            elif destino < nodo.getElemento():
                return str(nodo.getElemento()) + "\t" +  self._destino(destino, nodo.getIzq()) 
                 
            elif destino > nodo.getElemento():
                return str(nodo.getElemento()) + "\t" + self._destino(destino, nodo.getDer()) 
            else:
                return ("error")
        else:
                return ("error")

    def camino (self, inicio, destino, nodo):
        if nodo != None:
            if nodo.getElemento() == inicio:
                return self._destino(destino, nodo)
            elif inicio < nodo.getElemento():
                return self.camino(inicio, destino, nodo.getIzq())
            elif inicio > nodo.getElemento():
                return self.camino(inicio, destino, nodo.getDer()) 
            else:
                return ("error")


if __name__ == '__main__':
    arbol = Arbol()
    arbol.Insertar( arbol.getRaiz(), 20 )
    arbol.Insertar( arbol.getRaiz(), 19 )
    arbol.Insertar( arbol.getRaiz(), 23 )
    arbol.Insertar( arbol.getRaiz(), 24 )
    arbol.Insertar( arbol.getRaiz(), 22 )
    arbol.Insertar( arbol.getRaiz(), 18 )
    arbol.Insertar( arbol.getRaiz(), 26 )
    arbol.inOrden( arbol.getRaiz() )
    nodo = arbol.Buscar(18, arbol.getRaiz())
    print("encontrado",nodo.getElemento())
    nodo = arbol.padre(23, arbol.getRaiz())
    if nodo != None:
        print("el padre es: ", nodo.getElemento())
    else:
        print("no tiene padre")
    arbol.hermanos(18,23,arbol.getRaiz())
    arbol.hijo(23,19,arbol.getRaiz()) 
    arbol.mayor(arbol.getRaiz())
    arbol.menor(arbol.getRaiz())
    arbol.frontera(arbol.getRaiz())
    print(arbol.altura(arbol.getRaiz(),0))
    arbol.hoja(20, arbol.getRaiz())
    print("nivel",arbol.nivel(18, arbol.getRaiz(),0))
    print(arbol.camino(20, 38, arbol.getRaiz()))
    
