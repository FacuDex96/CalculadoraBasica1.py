def ingresar_datos():
    while True:
        alto = input("Ingrese el Alto, solo números enteros): ")

        if alto.isdigit():
            alto = int(alto)
            while True:
                ancho = input("Ingrese el Ancho, solo números enteros y no puede ser igual al Alto): ")

                if ancho.isdigit():
                    ancho = int(ancho)
                    if alto == ancho:
                        print("ambos valores no pueden ser iguales")
                    else:
                        break
                else:
                    print("Valor no valido.")
            break
        else:
            print("Valor no valido.")
    return alto,ancho
def dibujar_rectangulo(valores):
    
    for i in range(valores[0]):
        for i in range(valores[1]):
            print("*", end="")
        print("")
dibujar_rectangulo(ingresar_datos())