# Rellenar un diccionario con entrada del usuario.
# Pediremos a los usuarios toda la información necesaria en cada paso mediante while

# Hacer un programa de sondeo en el que en cada paso por el bucle while se pida:
# nombre del participante y una respuesta. Los datos se guardaran en un diccionario
# para poder conectar cada respuestaa con el correspondiente usuario.

# Se crea el diccionario vacio donde se almacenaran los datos finales

responses = {}

# Configura una bandea para indicar que la encuesta está activa
polling_active = True

while polling_active: 
    # Pide el nombre y la respuesta a la persona.
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Guarda la respuesta en el diccionario
    responses[name] = response

    # Averigua si alguien más va a hacer la encuesta.
    repeat = input("Would you like to let another person respond? (yes/no)? ")
    if repeat == 'no':
        polling_active = False

# La encuesta está completa. Muestra los resultados.
print("\n ---- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

