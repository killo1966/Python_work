# quiero saber si puedo usar la función remove con una variable

pets = ['cat', 'dog', 'rabbit','goldfish','cat','python']
print(pets)

eliminar = 'cat'

while eliminar in pets:
    pets.remove(eliminar)
print(f"Nueva lista {pets}")


