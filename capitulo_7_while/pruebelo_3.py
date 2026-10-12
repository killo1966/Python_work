# 7-8 Bocatería: Haga una lista llmada pedidos_bocadillos y rellénela con 
# los nombres de varios bocadillos.A continuación haga una lista vacía
# llamada bocadillos_terminados. Pase en bucle por la lista de pedidos de bocadillos
# e imprima un mensaje para cada pedido, como "Su bocadillo está listo"
# A medida que se hagan los bocadillos, páselos a la lista de terminados.
# Cuando todos los bocadillos estén hechos, imprima un mensajeque los enumere a todos.

# Lista de pedidos de bocadillos
pedidos_bocadillos = ['atun_con_tomate', 'queso_con_anchoas', 'jamon_serrano', 'chorizo', 'tortilla_de_patatas']

# Lista vacía de bocadillos terminados
bocadillos_terminados = []

# Pasar un bucle por lista de pedidos de bocadillos
while pedidos_bocadillos:

    bocadillos_en_curso = pedidos_bocadillos.pop()
    print(f"Su bocadillo de {bocadillos_en_curso} está listo")

    bocadillos_terminados.append(bocadillos_en_curso)

# Informar que todos los bocadillos estan hechos
print("\nTodos los bocadillos estan preparados, elija su favorito: \n")
for bocadillo in bocadillos_terminados:
    print(f"bocadillo de: {bocadillo}")




