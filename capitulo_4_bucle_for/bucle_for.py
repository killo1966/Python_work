invitados = ['encarni', 'aitana', 'rita', 'monica']
for invitado in invitados:
    print(f"Hola, {invitado.title()}, que alegría que vengas a la cena!!")


for numero in range(1,6):
    print(f"Estos son los elementos incluidos en la lista, {numero}")

print("Aquí al no estar dentro de la indentación ya esto fuera del bucle for")

magos = ['ramon','pedro','juan']
for mago in magos:
    print(f"{mago.title()}, tu truco fué genial.\n")
print(f"Magos como vosotros no se encuentran todos los día.")

pizzas = ["margarita", "tropical", "barbacoa"]
ingredientes = ["albahaca", "piña", "carne picada"]

# len(pizzas) nos da 3. range(3) genera los números: 0, 1, 2
for i in range(len(pizzas)):
    print(f"De la pizza {pizzas[i].title()} me gusta la {ingredientes[i]}.")
        

    