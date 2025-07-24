# 3.11 Ejercicios
# Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
# 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

# Introduzca las Horas: 45
# Introduzca la Tarifa por hora: 10
# Salario: 475.0

horas = int(input("Introduce las horas trabajadas: "))
tarifa = float(input("Introduce la tarifa por hora: "))
salario = ""
if horas > 40:
    horas_extra = horas - 40
    salario = (40 * tarifa) + (horas_extra * tarifa * 1.5)
else:
    salario = horas * tarifa

print("salario: ", salario)
# Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
# programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
# un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
# del programa:
# Introduzca las Horas: 20
# Introduzca la Tarifa por hora: nueve
# Error, por favor introduzca un número
# Introduzca las Horas: cuarenta
# Error, por favor introduzca un número


try:
    horas = int(input("Introduce las horas trabajadas: "))
    tarifa = float(input("Introduce la tarifa por hora: "))

    if horas > 40:
        horas_extra = horas - 40
        salario = (40 * tarifa) + (horas_extra * tarifa * 1.5)
    else:
        salario = horas * tarifa

    print(f"Salario: {salario:.2f}")
except ValueError:
    print("Por favor, introducí un numero.")

# Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
# puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
# está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:
# Puntuación Calificación
# >= 0.9 Sobresaliente
# >= 0.8 Notable
# >= 0.7 Bien
# >= 0.6 Suficiente
# < 0.6 Insuficiente
# Introduzca puntuación: 0.95
# Sobresaliente
# Introduzca puntuación: perfecto
# Puntuación incorrecta
# Introduzca puntuación: 10.0
# Puntuación incorrecta
# Introduzca puntuación: 0.75
# Bien
# Introduzca puntuación: 0.5
# Insuficiente
# Ejecuta el programa repetidamente, como se muestra arriba, para probar con varios
# valores de entrada diferentes.

try:
    puntuacion = float(input("Introduce una puntuación  entre 0.0 y  1.0: "))

    if puntuacion < 0.0 or puntuacion > 1.0:
        print("Error, puntuación fuera de rango.")
    elif puntuacion >= 0.9:
        print("Sobresaliente.")
    elif puntuacion >= 0.8:
        print("Notable")
    elif puntuacion >= 0.7:
        print("bien")
    elif puntuacion >= 0.6:
        print("Suficiente")
    elif puntuacion < 0.6:
        print("Insuficiente")
except ValueError:
    print("Ingresa un número")


