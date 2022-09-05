from ej1Encadenado import Medio

if __name__ == '__main__':
    lista = Medio()
    lista.crear()
    lista.insertar(1,0)
    lista.insertar(2,1)
    lista.insertar(3,2)
    lista.insertar(4,3)
    lista.recorrer()
    lista.insertar(0,0)
    lista.recorrer()
    #lista.suprimir(2)
    lista.recorrer()

