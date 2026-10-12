#%%
pedidos_bocadillos = [
    'pastrami', 'atun', 'tomate', 'queso', 'anchoas', 
    'pastrami', 'jamon_serrano', 'chorizo', 'pastrami', 'tortilla'
]

ingredientes = [
    'pastrami', 'atun', 'tomate', 'queso', 'anchoas', 
    'chorizo', 'huevos', 'patatas', 'pan'
]

# Se crea la lista de bocadillos terminados
bocadillos_terminados = []

# Ponemos en marcha el programa de gestión de pedidos
print("--- Inicializando sistema ---\n")
print(f"Verifique que disponemos de los siguientes ingredientes:")
print(f"{ingredientes}\n")

ingrediente_agotado = input("Introduzca el nombre del ingrediente agotado (o pulse Enter si están todos): ")

# 1. Gestionamos el ingrediente agotado si lo hay
if ingrediente_agotado == "":
    print("\n[Aviso] No hay ningún ingrediente agotado hoy.")
    print(f"Lista de pedidos inicial: {pedidos_bocadillos}\n")
else:
    print(f"\n[Aviso] Sentimos anunciar que el ingrediente '{ingrediente_agotado}' está agotado.")
    print("Repondremos lo antes posible.\n")
    
    # Borramos todas las apariciones de ese ingrediente
    while ingrediente_agotado in pedidos_bocadillos:
        pedidos_bocadillos.remove(ingrediente_agotado)
        
    print(f"Lista de pedidos tras eliminar el ingrediente:")
    print(f"{pedidos_bocadillos}\n")

# 2. LA PREPARACIÓN VA FUERA: Se ejecuta siempre, haya o no ingredientes agotados
print("--- Comenzando la elaboración de los bocadillos ---")
while pedidos_bocadillos:
    bocadillos_en_curso = pedidos_bocadillos.pop()
    print(f"Su bocadillo de {bocadillos_en_curso} ha sido preparado.")
    bocadillos_terminados.append(bocadillos_en_curso)

# Se informa de los bocadillos que están terminados
print(f"\n\t¡Los bocadillos están terminados, elijan sus favoritos!\n")
for bocadillo in bocadillos_terminados:
    print(f"Bocadillo de: {bocadillo}")