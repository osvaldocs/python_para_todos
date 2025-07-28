# Ejercicio 1: Escribe un bucle while que comience con el último carácter
# en la cadena y haga un recorrido hacia atrás hasta el primer carácter
# en la cadena, imprimiendo cada letra en una línea independiente.

fruta = "mandarina"
indice = len(fruta)

while indice > 0:
    letra = fruta[indice - 1]
    print(letra)
    indice = indice -1

# Ejercicio 2: Dado que fruta es una cadena, ¿que significa fruta[:]?

# fruta = "banana"
# print(fruta[:])

# Es un slice completo de banana desde el principio hasta el final.

# Ejercicio 3: Encapsula este código en una función llamada cuenta, y
# hazla genérica de tal modo que pueda aceptar una cadena y una letra
# como argumentos.

# palabra = 'banana'
#     contador = 0
#     for letra in palabra:
#         if letra == 'a':
#             contador = contador + 1
#     print(contador)

def cuenta(palabra, letra):
    contador = 0
    for char in palabra:
        if char == letra:
            contador = contador + 1
    print(contador)

cuenta("palabra", "a")


# Ejercicio 4: Hay un método de cadenas llamado count que es similar a
# la función del ejercicio previo. Lee la documentación de este método
# en:
# https://docs.python.org/library/stdtypes.html#string-methods
# Escribe una invocación que cuenta el número de veces que una letra
# aparece en “banana”.

palabra = "banana"
print(palabra.count("b"))

# Ejercicio 5: Toma el siguiente código en Python que almacena una cadena:
# str = 'X-DSPAM-Confidence:0.8475'
# Utiliza find y una parte de la cadena para extraer la porción de la cadena
# después del carácter dos puntos y después utiliza la función float para
# convertir la cadena extraída en un número de punto flotante.

str = 'X-DSPAM-Confidence:0.8475'

desde = str.find(":")
parte = str[desde + 1 :]
flotante = float(parte)
print(flotante)

# Ejercicio 6: Lee la documentación de los métodos de cadenas en
# https://docs.python.org/library/stdtypes.html#string-methods Quizá
# quieras experimentar con algunos de ellos para asegurarte de entender
# como funcionan. strip y replace son particularmente útiles.
# La documentación usa una sintaxis que puede ser confusa. Por ejemplo, en find(sub[, start[, end]]), los corchetes indican argumentos opcionales. De modo que sub es requerido, pero start es opcional, y si se
# incluye start, entonces end es opcional.