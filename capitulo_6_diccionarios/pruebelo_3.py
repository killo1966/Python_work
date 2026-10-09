# 6-7 Personas: Cree dos diccionarios nuevos que representen a distintas personas como el de 6-1 y
# guarde los tres diccionarios en una lista llamada personas. Pase en bucle por la lista.
# Al hacerlo, imprima todo lo que sabe sobre cada persona.

datos_javier = {'nombre':'francisco javier',
                    'apellidos':'serrano cornejo',
                    'edad': 60,
                    'ciudad':'san fernando'
}

datos_toñi = {'nombre':'toñi',
                        'apellidos':'garcía lópez',
                        'edad':59,
                        'ciudad':'murcia'

}
datos_paloma = {'nombre':'paloma',
                           'apellidos':'serrano garcía',
                           'edad':27,
                           'ciudad':'murcia'
}
# 1. Creamos la lista metiendo las variables de los diccionarios SIN COMILLAS
personal = [datos_javier, datos_toñi,datos_paloma]

# 2. Recorremos la lista
for persona in personal:
    print("\n ----------------- Información de la persona --------------------")

    # 3. Recorremos cada diccionario con .items() para sacar sus claves y valores
    for clave, valor in persona.items():
        # Si el valor es texto, le ponemos .title(); si es un número (como la edad), lo dejamos tal cual
        if isinstance(valor, str):
            print(f"{clave.title()}:{valor.title()}")
        else:
            print(f"{clave.title()}:{valor}")



# 6-8 Mascotas. Cree varios diccionarios, cada uno representando una mascota diferente. En cada uno
# incluya el tipo de animal, y el nombre del dueño. Guarde estos diccionarios en una lista llamada mascotas
# A continuación pase un bucle por la lista y, al hacerlo imprima todo lo que sabe sobre cada mascota

terri = {
    'animal':'gato',
    'dueño':'lolo'
}
samanta = {
    'animal':'serpiente',
    'dueño': 'peter'
}
toni = {
    'animal':'hamster',
    'dueño':'jose'
}
tipi = {
    'animal':'caballo',
    'dueño':'marina'
}

# 1- Creo la lista
mascotas = [terri,samanta,toni,tipi]

# 2- recorro la lista
for mascota in mascotas:
    print(f"------------ Información de la mascota -----------")
# 3 - Recorremos cada diccionario con items para sacar sus claves y valores
    for clave, valor in mascota.items():
        print(f"{clave.title()}:{valor.title()}")



# 6-9 Lugares favoritos: Cree un diccionario llamado lugares favoritos. Piense en tres nombres para usar
# como claves en el diccionario y guarde entre uno y tres lugares favoritos por cada persona. 
# Para hacer este ejercicio un poco mas interesante, pregunta a algunos amigos por sus sitios preferidos.
# Pase un bucle por el diccionario e imprima el nombre y el lugar favorito de cada persona.

lugares_favoritos = {
    'marina': ['casa','playa','catedral'],
    'toñi':['pueblo','ciudad','extranjero'],
    'javi':['playa','hbitacion','gym']
}

for persona, lugares in lugares_favoritos.items():
    print(f"\n Lugares favoritos de {persona.title()}:")
    for lugar in lugares:
        print(f"\t{lugar.title()}")

# 6-10 Números favoritos: Modifique el programa del ejercicio 6-2 para que cada persona pueda tener
# mas de un número favorito. Luego imprima el nombre de cada persona junto con su(s) número(s) favorito(s)

numeros_favoritos = {
    'javier': [22],
    'toñi':[25,67,4,46,55],
    'javi':[1,28,88,25],
    'paloma':[5,10,99,4],
    'juanjo':[10,7,4,25],
    'marina':[28,8,3,4,22,25]
}

for nombre, numeros in numeros_favoritos.items():
    varios = len(numeros)
    if varios > 1:
        print(f"Los numeros favoritos de {nombre.title()} son: ")
    else:
        print(f"El numero favorito de {nombre.title()} es: ")
    for numero in numeros:
        print(f"\t {numero}", end=" ")
    print("\n")
# la \t produce una identación y el codigo end=" " hace que no salgan los resultados
# en columna, sino uno a continuación de otro dejando un espacio o el simbolo que queramos
# dentro de las comillas del end

# 6-11 Cree un diccionario llamado ciudades. Use los nombres de tres ciudades como claves 
# en su diccionario. Cree un diccionario de información sobre cada ciudad e incluya 
# el país en el que se encuentra, su población aproximada y alguna curiosidad sobre
# la ciudad. Las claves para cada ciudad serían pais, población y curiosidad. Imprima
# el nombre de cada ciudad y toda la información que tenga guardada sobre ella

ciudades = {
    'madrid': {'pais': 'españa', 'población': '5M', 'curiosidad':'templo de debod'},
    'londres': {'pais':'reino unido', 'población':'10M', 'curiosidad':'big ben'},
    'paris':{'pais':'francia', 'población':'15M', 'curiosidad':'torre eiffel'}
}
for ciudad, informacion in ciudades.items():
    print(f"\n{ciudad.title()}:")
    print(f"\tDatos relevantes:")
    for clave, valor in informacion.items():
        print(f"\t\t- {clave.title()}: {valor.title() if isinstance(valor, str) else valor}")

# isinstance() es una función nativa de Python que sirve para preguntar de qué tipo es un dato.
# Le decimos: "Oye Python, comprueba si valor es de tipo str (texto/string)".Si es texto, devuelve True;
# si es de otro tipo (como un número entero int, un decimal, etc.), devuelve False.
# Si valor es un texto (isinstance(valor, str) es verdadero), entonces aplica .title() para poner 
# la primera letra en mayúscula. Si no lo es (else), deja el valor tal cual está (valor).

