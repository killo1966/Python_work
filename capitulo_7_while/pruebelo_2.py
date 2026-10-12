# 7-4 Ingredientes de piezza: Escriba un bucle que pida al usuario que introduzca
# una serie de ingredientes de piezzza y termine escribiendo el valor 'quit'
# Cuando introduzca cada ingrediente, imprima un mensaje diciendo que lo añadirá
# a su pizza.

#%%
prompt ="\n Introduzca un ingrediente de su pizza favorita,"
prompt += "\n escriba 'quit' para salir cuando no haya mas ingredientes: "

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(f"Por su puesto, añadiremos {message} a su pizza")

# %%
# 7-5 Entradas de cine: Un cine cobra las entradas a distinto precio en función
# de la edad del espectador. Los menores de 3 años entran gratis, los niños
# entre 3 y 12 años pagan 8 euros y la entrada para mayores de 12 años cuesta
# 12 euros. Escriba un bucle para preguntar a los usuarios su edad y luego 
# digales el precio de su entrada.

prompt = "\n Bienvenido a cine de barrio. Los precios de las entradas son gratis, 8 euros"
prompt += "\n y 12 euros, y van en función de la edad. Cual es su edad? "

edad = ''
while edad != 'quit':
    edad = input(prompt)
    if edad == 'quit':
        break
    edad = int(edad)
    if edad < 3:
        print(f"Su entrada es gratuíta, por tener menos de {edad} años")
    elif edad <= 12:
        print(f"El precio de su entrada es de 8 euros, por tener {edad} años")
    else:
        print(f"El precio de su entrada es de 12 euros al tener usted {edad} años")

# %%
# 7-6 Tres salidas: Escriba distintas versiones de los ejercicios 7-4 o 7-5 haciendo
# cada uno de los siguientes como mínimo una vez:
# Use una prueba condicional en la entencia while para detener el bucle
# Use una variable active para contolar cuanto tiempo se ejecuta el bucle
# Use una sentencia break para salir del bucle cuando el usuario introduzca el valor 'quit'

