# ejercicio 4.1 Pizzas
pizzas = ['cuatro_estaciones', 'margarita', 'carbonara']
opiniones = ['me apasiona', 'me gusta', 'me encanta']
print('Mis pizzas favoritas son:')
for pizza in pizzas:
    print(pizza)

for i in range(len(pizzas)):
    print(f"La pizza: {pizzas[i]}, {opiniones[i]}")
print("Como se puede ver, soy un apasionado de la pizza!!!")