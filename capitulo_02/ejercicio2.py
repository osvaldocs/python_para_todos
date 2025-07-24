
# 2.15 Ejercicios
# Ejercicio 2: Escribe un programa que use input para pedirle al usuario su nombre y luego darle la bienvenida.

nombre = input("Ingresá tu nombre: ")
print(f"\nBienvenido, {nombre}.")

# Ejercicio 3: Escribe un programa para pedirle al usuario el número de  horas y la tarifa por hora para calcular el salario bruto.
# Introduzca Horas: 35
# Introduzca Tarifa: 2.75
# Salario: 96.25
# Por ahora no es necesario preocuparse de que nuestro salario tenga exactamente
# dos dígitos después del punto decimal. Si quieres, puedes probar la función interna
# de Python round para redondear de forma adecuada el salario resultante a dos
# dígitos decimales.

horas = float(input("Ingrese la cantidad de horas trabjadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
salario_bruto = horas * tarifa

print(salario_bruto)

# Ejercicio 4: Asume que ejecutamos las siguientes sentencias de asignación:
# ancho = 17
# alto = 12.0
# Para cada una de las expresiones siguientes, escribe el valor de la expresión y el
# tipo (del valor de la expresión).
# 1. ancho/2 (valor 8.5, tipo float)
# 2. ancho/2.0 (valor 8.5, tipo float)
# 3. alto/3 (valor 4.0, tipo float)
# 4. 1 + 2 * 5 (valor 11, tipo int)
# Usa el intérprete de Python para comprobar tus respuestas.
# Ejercicio 5: Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima
# por pantalla la temperatura convertida.

temp_celsius = float(input("Ingresá la temperatura en °C: "))
temp_fahrenheit = temp_celsius *9/5 + 32
print(f"La temperatura en grados Fahrenheit es: {temp_fahrenheit:.2f}°F.")