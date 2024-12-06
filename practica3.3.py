def ingresar_datos():
    mayor = None
    
    while True:
        n = input("Ingrese un número (Ingrese una letrita para finalizar): ")
        
        if n.isdigit():
            n = int(n)
        elif "." in n:
            n = float(n)
        else:
            break

        if mayor == None:
            mayor = n
        elif n > mayor:
            mayor = n
            
    return mayor
def n_mayor():
    n = ingresar_datos()
    
    if n == None:
        print("No ingresaste ningun numero.")
    else:
        print(f"El mayor número ingresado es: {n}")
n_mayor()