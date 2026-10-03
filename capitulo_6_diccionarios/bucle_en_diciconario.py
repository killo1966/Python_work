# Guarda en un diccionario los datos de un usuario de una página web
# imprime los pares clave(key), valor(Value)  de todo el diccionario usando un bucle for

user_0 = {
    'username':'toñi',
    'first':'garcía',
    'last':'lópez',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

# ejemplo de uso de for en un diccionario para imprimir la clave y valor

equipo_favorito = {
    'pedro':'real madrid',
    'jaime':'barcelona',
    'matias':'betis',
    'juan':'cadiz',
    'pepe':'sevilla',
}

for nombre, equipo in equipo_favorito.items():
    print(f"El equipo favorito de: {nombre.title()} es: {equipo.title()}")

# Ahora si solo quiero imprimir los nombres de las personas que dijeron su equipo favorito:

for nombre in equipo_favorito.keys():
    print(f"El nombre de la persona que dijo su favorito es: {nombre.title()}")
