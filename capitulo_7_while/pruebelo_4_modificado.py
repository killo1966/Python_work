# 7-9 Variante del ejercicio 7-9 en la que se se ofrece la alternativa de otro bocadillo
# en el caso de que falte algun ingrediente.

#%%
pedidos_bocadillos = ['pastrami',
                      'atun',
                      'tomate',
                      'queso',
                      'anchoas',
                      'jamon_serrano',
                      'chorizo',
                      'tortilla'
                     ]
ingredientes = [
                'pastrami',
                'atun',
                'tomate',
                'queso',
                'anchoas',
                'chorizo',
                'huevos',
                'patatas',
                'pan'
            ]

 # Se crea la lista de bocadillos terminados
bocadillos_terminados = []

# Ponemos en marcha el programa de gestión de pedidos de bocadillos
print("--- Inicializando sistema ---\n")
print(f"\nVerifique que disponemos de los siguientes ingredientes para la elaboración: ")
print(f"\n {ingredientes}")

ingrediente_agotado = input("Introduzca el nombre del ingrediente agotado (o pulse Enter si están todos): ")

if ingrediente_agotado == 'pan':
    print(f"\nNo sabe cuanto lo sentimos, el servicio está interrumpido por falta de {ingrediente_agotado}")
    print(f"\nSin {ingrediente_agotado}, no podemos hacer ningun tipo de bocadillo")
    print(f"\nDisculpen las molestias. Intentaremos restablecer el servicio lo antes posible")


    
else:
    if ingrediente_agotado == "":
        print(f"\n Hoy no nos falta ningun ingrediente. Puede elegir caulquier bocadillo")
        print(f"\n ------ Lista  completa de bocadillos ---")
        print(f"{pedidos_bocadillos}\n")


         
    else:
        # Aviso de ingrediente agotado
        prompt = f"\nSentimos anunciarles que el bocadillo de {ingrediente_agotado} está agotado."
        prompt += "\nDisculpen las molestias. Repondremos el bocadillo lo antes posible\n"
        message = prompt
        print(message)
        
        while ingrediente_agotado in pedidos_bocadillos:
        # Se elimina todas las referencias del ingrediente agotado en pedidos_bocadillos
            pedidos_bocadillos.remove(ingrediente_agotado)

        # imprime la nueva lista de pedidos_bocadillos mientras no se reponga el ingrediente agotado
        print(f"A falta de {ingrediente_agotado}, pueden elegir entre los siguientes bocadillos:")
        print(pedidos_bocadillos)

while pedidos_bocadillos:
    bocadillos_en_curso = pedidos_bocadillos.pop()
    print(f"Su bocadillo de {bocadillos_en_curso},  ha sido preparado")

    # Añadimos los bocadillos encurso a la lista de bocadillos terminados
    bocadillos_terminados.append(bocadillos_en_curso)

# Se informa de los bocadillos que estan terminados
print(f"\n\tLos bocadillos estan terminados, elijan sus favoritos!!!\n")
for bocadillo in bocadillos_terminados:
    print(f"Bocadillo de: {bocadillo}")


