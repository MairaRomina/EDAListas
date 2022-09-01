from lista import Cola

if __name__ == '__main__':
    cola = Cola(7)
    for i in range(7):
        resultado = cola.insertar(i + 1)
        if resultado != 0:
            print("Se inserto: ", resultado)
        else:
            print("No se pudo insertar, se lleno la lista")
    
    for i in range(5):
        resultado = cola.suprimir()
        if resultado != 0:
            print("Se suprimio: ", resultado)
        else:
            print("No se pudo suprimir, lista vacia")

    for i in range(2):
        resultado = cola.insertar(i + 1)
        if resultado != 0:
            print("Se inserto: ", resultado)
        else:
            print("No se pudo insertar, se lleno la lista")

    cola.recorrer()