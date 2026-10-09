# 6-4 Glosario 2 Ahora sustituya las llamadas a print() del ejercicio 6-3 por un bucle que pase
# por las claves y valores del diccionario. Añada cinco terminos mas

glosario = {
    'print': 'imprime el valor de una variable o una cadena de texto',
    'for': 'usada para los bucles',
    'in': 'usada junto con for para hacer un bucle a los elementos de una lista o diccionario',
    'get': 'para obtener el valor de una clave de un diccionario que pueda que no exista sin error',
    'if': 'usada como condicional con elif o else',
    'items': 'para listar todos los pares clave-valor del diccionario',
    'keys': 'lista las claves del diccionario',
    'values': 'lista los valores del diccionario',
    'sorted': 'ordena los resultados de una consulta del bucle',
    'set':'da un resultado de conjunto, impidiendo que datos repetidos aparezcan dos veces en los resultados'
}

for termino, definicion in glosario.items():
    print(f"\n{termino}: {definicion}")

# 6-5 Ríos haga un diccionario con tres ríos imporantes y el país por el que discurre cada uno

ríos = {'ebro':'españa',
        'nilo':'egipto',
        'niagara':'canada',
        'amazonas':'brasil',
        'danubio':'alemania',
        'tamesis':'reino unido',
        'misisipi':'estados unidos',
        }
for rio, pais in ríos.items():
    print(f"El {rio.title()} discurre por {pais.title()}")

# Imprimir todos los riosque aparecen en el diccionario usando un bucle for

print(f"Los Ríos incluidos en mi diccionario son:\n")
for rio in ríos.values():
   print(rio.title())


print(f"Los países por los que pasan los Ríos de mi diccionario son:\n")
for pais in ríos.values():
    print(pais.title())


# 6-6 Sondeos: use el diccionario de lenguajes_favoritos.py y
# Haga una lista de personas que deberían hacer la encuesta sobre lenguajes preferidos
# Incluya algunos nombres que estén ya en el diccionario y otros que no lo esten
# Pase el bucle por la lista de personas que deberían hacer la encuesta.Si ya la han hecho
# deles las gracias por responder. Si todavía no la han completado, imprima un mensaje
# invitandoles a hacerlo.

lenguajes_favoritos = {
    'marta':'c',
    'pepe':'python',
    'miguel':'rubish',
    'ramon':'html',
    'javi':'javascript',
    'luis':'java',
}
friends = ['miguel','ramon','sergio','miguel angel', 'jacobo','abrahan','josualdo','jaun']

for friend in friends:
    if friend in lenguajes_favoritos:
        print(f"{friend.title()}, deberías estudiar algun lenguaje y hacer mi encuesta")
    else:
        print(f"{friend.title()}, gracias por participar en mi encuesta, sigue estudiando")