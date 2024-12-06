def ingresar_datos():
    suma = 0
    contador = 07
    while True:
        nota = input("Ingrese Nota (0 para finalizar): ")

        if nota.isnumeric() or nota.replace(".", "").isnumeric():
            nota = float(nota)
            if nota > 0:
                suma += nota
                contador += 1
            else:
                break
        else:
            print("Nota no valida.")
    return suma, contador
def promedio_notas():
    x,y = ingresar_datos()
    print(f"El promedio es: {round(x/y,2)}")
promedio_notas()