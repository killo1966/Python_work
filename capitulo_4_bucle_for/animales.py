animales = ['perro', 'gato', 'loro', 'hamster']
opiniones = ['escelente mascota', 'gran compañia', 'conversacion constante', 'preocupacion permanente']
for animal in animales:
    print(animal)

for i in range(len(animales)):
    print(f"Un {animales[i]}, sería una {opiniones[i]}")