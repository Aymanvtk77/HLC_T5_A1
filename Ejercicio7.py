def suma():
    numero_1=int(input("Introduce un numero:v"))
    numero_2=int(input("Introduce un numero:v"))
    suma=numero_1+numero_2
    return suma
def mostrarSuma():
    resultado=suma()
    print("La suma de esto es", resultado)
mostrarSuma()