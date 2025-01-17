numero_1=int(input("Introduce un numero"))
numero_2=int(input("Introduce un numero"))
if numero_1 > numero_2:
    print(numero_1, "Es mayor que", numero_2)
elif numero_2 > numero_1:
    print(numero_2, "es mayor que", numero_1)
elif numero_1 == numero_2 or numero_2 == numero_1:
    print("Estos numeros son iguales")