invitados = ["ana", "pepe", "luis"]
print(f"El primer invitado es: {invitados[0].title()}")

# Añadimos un invitado al final de la lista de invitados
invitados.append("marta")

print(invitados)

print(f"El último invitado en llegar es: {invitados[-1].title()}")

invitados.insert(1, "manuel") # Inserta al invitado "manuel" en la segunda posición de la lista
print(invitados)

del invitados[0] # Borra el indice que ya no volveré a usar
print(invitados)

invitado_ausente = invitados.pop(2) # Borra el indice que queramos de la lista o el último, pero antes permite guardarlo en una variable
print(invitados)
print(f"El invitado que no vendra a la fiesta es: {invitado_ausente.title()}") 
invitado_enfermo = invitados.pop() # Elimina el último elemento de de la lista
print(f"{invitado_enfermo.title()} no podrá venir porque está enferma")

invitados.remove("manuel") # Elimino un elemento de lista por su valor
print(invitados)

invitados_actuales = len(invitados)
print(f"El número de invitados en estos momentos es de: {invitados_actuales}")

marcas = []  # Creo la lista marcas sin ningun elemento
marcas.append('seat')
marcas.append('renault')
marcas.append('honda')
marcas.append('hyundai')
marcas.append('toyota')
marcas.append('subaru')
marcas.append('bmw')
marcas.append('kia')
marcas.append('opel')
marcas.append('nissan')

print(marcas)

print(f"Las marcas de coche actuales son: {sorted(marcas)}")
print(marcas)
print(f"El número de marcas de coches en mi lista es: {len(marcas)}")









