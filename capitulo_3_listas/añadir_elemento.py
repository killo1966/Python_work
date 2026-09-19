# Como insertar elementos numericos y no numéricos en una lista desde un bucle

lista_numerica = list(range(1,10))
print(lista_numerica)

#calculo de cuadrados
cuadrados = []
for value in range(1,11):
    cuadrado = value ** 2
    cuadrados.append(cuadrado)
print(cuadrados)

# Como insetar una cadena desde una lista en otra con un bucle for
alimentos = []
frutas = ['manzanas', 'peras', 'uvas','melocotones', 'nectarinas']
vegetales = ['zanahoria', 'cebolla', 'lechuga']

for i in range(len(frutas)):
    alimento = frutas[i]
    alimentos.append(alimento)
print(f"los alimentos son: {alimentos}")
