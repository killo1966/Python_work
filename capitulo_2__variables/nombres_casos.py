nombre = "fancisco javier"
print("Hola " + nombre.title() + ", ¿cómo va el curso de Python?") # Concatenación de cadenas usando el operador +.

name = "fancisco javier"
last_name = "serrano"
last_name2 = "cornejo"
full_name = f"{name} {last_name} {last_name2}" # Concatenación de cadenas usando f-strings.
print(f"Hola, {full_name.title()}")

nombre = "Albert Einstein"
cita = "Una persona que nunca cometió un error nunca intentó algo nuevo."
message = f'{nombre} dijo: "{cita}"' # Concatenación de cadenas usando f-strings.
print(message) # Imprime la cadena que contiene comillas dobles dentro de comillas simples.

# Guiones con números

edad_de_piedra = 2_500_000_000 # Uso de guiones bajos para mejorar la legibilidad de números grandes.
print(edad_de_piedra) # Imprime el número con guiones bajos para mejorar la legibilidad.

