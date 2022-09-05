from ej1Contenido import Medio

if __name__ == '__main__':
    lista = Medio()
    lista.crear()
    lista.insertar(4)
    lista.insertar(0)
    lista.insertar(2)
    lista.insertar(1)
    lista.recorrer()
    print("---------------")
    lista.insertar(5)
    lista.insertar(3)
    lista.recorrer()
    #lista.suprimir(2)
    #lista.recorrer()
