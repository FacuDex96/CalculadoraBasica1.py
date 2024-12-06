def ingresar_datos():
    while True:
        n = input("Ingrese un número, pero solo números enteros: ")

        if n.isdigit():
            n = int(n)
            if n > 0:
                break
            else: 
                print("El número debe ser positivo")
        else:
            print("Valor no valido.")
    
    return n

def factorial_n(n):
    factorial = 1
    for i in range(1, n + 1):
      factorial *= i
   
    print(f"El facotrial de {n} es: {factorial}")

factorial_n(ingresar_datos())