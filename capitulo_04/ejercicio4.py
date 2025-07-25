# Ejercicio 4: ¿Cuál es la utilidad de la palabra clave “def” en Python?
# a) Es una jerga que significa “este código es realmente estupendo”
# b) Indica el comienzo de una función
# c) Indica que la siguiente sección de código indentado debe ser almacenada para
# usarla más tarde
# d) b y c son correctas ambas ✅
# e) Ninguna de las anteriores
# Ejercicio 5: ¿Qué mostrará en pantalla el siguiente programa Python?
# def fred():
# print("Zap")
# def jane():
# print("ABC")
# jane()
# fred()
# jane()
# a) Zap ABC jane fred jane
# b) Zap ABC Zap
# c) ABC Zap jane
# d) ABC Zap ABC ✅
# e) Zap Zap Zap
# Ejercicio 6: Reescribe el programa de cálculo del salario, con tarifa-ymedia para las horas extras, y crea una función llamada calculo_salario
# que reciba dos parámetros (horas y tarifa).
# Introduzca Horas: 45
# Introduzca Tarifa: 10
# Salario: 475.0

def calculo_salario(horas, tarifa) :

    if horas > 40:
        extra = (horas - 40) * tarifa * 1.5
        salario = 40 * tarifa + extra
        return salario
    else:
        salario = horas * tarifa
        return salario


# Ejercicio 7: Reescribe el programa de calificaciones del capítulo anterior usando una función llamada calcula_calificacion, que reciba una
# puntuación como parámetro y devuelva una calificación como cadena.
# Puntuación Calificación
# > 0.9 Sobresaliente
# > 0.8 Notable
# > 0.7 Bien
# > 0.6 Suficiente
# <= 0.6 Insuficiente
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
# Ejecuta el programa repetidamente para probar con varios valores de entrada diferentes.


def calcula_calificacion(puntuacion):

    if puntuacion > 0.9:
        return f"Sobresaliente, tu calificacion es: {puntuacion}."
    elif puntuacion > 0.8:
        return f"Notable, tu calificacion es: {puntuacion}."
    elif puntuacion > 0.7:
        return f"Bien, tu calificacion es: {puntuacion}."
    elif puntuacion > 0.6:
        return f"Suficiente, tu calificacion es: {puntuacion}."
    else:
        return f"Insuficiente, tu calificacion es: {puntuacion}."

try:
    nota = float(input("Introduce una puntuación  entre 0.0 y  1.0: "))
    print(calcula_calificacion(nota))
except ValueError:
    print("Dato inválido.")