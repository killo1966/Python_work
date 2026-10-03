# 6-1 Personas. Use un diccionario para almacenar información sobre una persona que conozca
# Guarde su nombre, apellido, edad, y ciudad en la que vive. Imprima toda la información
# guardada en su diccionario.

datos_personales = {'nombre':'francisco javier',
                    'apellidos':'serrano cornejo',
                    'edad': 60,
                    'ciudad':'Murcia'
                    }
print(f"Este es el diccionario de mis datos personales:\n {datos_personales}")
print(f"Nombre: {datos_personales['nombre'].title()}")
print(f"Apellidos: {datos_personales['apellidos'].title()}")
print(f"Edad: {datos_personales['edad']}")
print(f"Ciudad: {datos_personales['ciudad'].title()}")

# 6-2 Números favoritos: Useun diccionario para guarar los números favoritos de distintas personas.
# Piense en 5 nombres y úselos como claves en su diccionario. Imprima el nombre y el número favorito
# de cada persona.

numero_favorito = {
    'toñi': 25,
    'javi': 15,
    'paloma': 5,
    'juanjo': 10,
    'marina': 28,
}
print(f"El número favorito de Toñi es: {numero_favorito['toñi']}")
print(f"El número favorito de Javi es: {numero_favorito['javi']}")
print(f"El número favorito de Paloma es: {numero_favorito['paloma']}")
print(f"El número favorito de Juanjo es: {numero_favorito['juanjo']}")
print(f"El número favorito de Marina es: {numero_favorito['marina']}")


# 6-3: Glosario. Usar 5 palabras aprendidas de python y usarlas como clave de un diccionario.
# usar sus significados como valores. Imprima cada palabra con un formato limpio, primero el nombre
# de la palabra y en otro renglon aparte su significado.

glosario = {
    'print': 'imprime el valor de una variable o una cadena de texto',
    'for': 'usada para los bucles',
    'in': 'usada junto con for para hacer un bucle a los elementos de una lista o diccionario',
    'get': 'para obtener el valor de una clave de un diccionario que pueda que no exista sin error',
    'if': 'usada como condicional con elif o else',
}
print(f"print:\n{glosario['print']}")
print(f"for:\n{glosario['for']}")
print(f"in:\n{glosario['in']}")
print(f"get():\n{glosario['get']}")
print(f"if:\n{glosario['if']}")

