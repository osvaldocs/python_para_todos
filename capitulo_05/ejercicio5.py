# 5.10 Ejercicios
# Ejercicio 1: Escribe un programa que lea repetidamente números hasta
# que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
# muestra por pantalla el total, la cantidad de números y la media de
# esos números. Si el usuario introduce cualquier otra cosa que no sea un
# número, detecta su fallo usando try y except, muestra un mensaje de
# error y pasa al número siguiente.
# Introduzca un número: 4
# Introduzca un número: 5
# Introduzca un número: dato erróneo
# Entrada inválida
# Introduzca un número: 7
# Introduzca un número: fin
# 16 3 5.33333333333

total = 0
contador = 0
media = 0

while True:
    entrada = input("Ingresá un número:")
    if entrada == "fin":
        break
    try:
        numero = float(entrada)
        contador = contador + 1
        total = total + numero
        media = total / contador

    except ValueError:
        print("Entrada inválida. Por favor, ingresá un número: ")
        continue

print(total, contador, media)

# Ejercicio 2: Escribe otro programa que pida una lista de números como
# la anterior y al final muestre por pantalla el máximo y mínimo de los
# números, en vez de la media.

maximo = None
minimo = None

while True:
    entrada = input("Ingresá un número ")
    if entrada == "final":
        break
    try:
        numero = float(entrada)
        if maximo is None or numero > maximo:
            maximo = numero
        if minimo is None or numero < minimo:
            minimo = numero
    except ValueError:
        print("Entrada inválida. Por favor ingresá un número: ")

print(f"maximo es: {maximo}.\nminimo es: {minimo}.")