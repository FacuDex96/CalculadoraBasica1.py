def ingrese_color():
    color = input("ingrese un color (nombre del color): ")
    return color
def es_primario(color):
    if color.lower() == "azul" or color.lower() == "rojo" or color.lower() == "amarillo":
        return True, color
    else:
        return False, color
def salida_color(primario):
    
    if primario[0]:
        print(f"El color {primario[1]} es primario.")
    else:
        print(f"El color {primario[1]} no es primario.")

salida_color(es_primario(ingrese_color()))