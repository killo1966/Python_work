# Que ocurre si queremos eliminar todas las apariciones de un vaor en una lista?

# ejemplo ---- Eliminar todos los valores de 'cat' en la lista de animales

# para ello usaremos la función remove()  junto al bucle while

pets = ['dog', 'cat', 'dog', 'golfish', 'cat','rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)