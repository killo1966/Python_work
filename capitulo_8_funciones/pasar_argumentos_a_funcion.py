# La llamada a una función puede tener varios argumentos. Podemos pasar
# argumentos a las funciones de varias maneras. Podemos pasar argumentos
# posicionales, que tienen que estar en el mismo orden en el que e escribieron
# parámetros de clave, donde cada argunmento consta de un nombre de variable y
# un valor; y listas y diccionarios de valores.

# --- Argumentos posicionales --- 
# Cuando llamamos a una función, Python debe asociar cada argumento de la llamada
# con un parametro de la definición. La forma más fácil de hacerlo se basa en el
# orden de los argumentos proporcionados. Los valores asociados así se denominan
# "Argumentos posicionales". 
# Para ver como fucionan, consideraremos una función que muestre información sobre
# mascotas La función nos dice qué tipo de animal es cada mascota y có0mo se llama.

#%%
def describe_pet(animal_tipe, pet_name):
    """Muestra informacion sobre una mascota"""
    print(f"\nI have a {animal_tipe}.")
    print(f"My {animal_tipe}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Múltiples llamadas a una función

# Podemos llamar a una función todas las veces que haga falta. Describir una
# segunda mascota, requerirá otra llamada a describe_pet()

#%%
# ---- Argumentos de palabra clave ---
# Un argumento de palabra clave es un par nombre-valor que pasamos a una función
# Se asocia directamente el nombre y el valor dentro del argumento, así que, cuando
# pasamos el argumento a la función, no hay confusiones(no acabaremos con un harry llamadao Hámster).
# Los argumentos de palabra clave nos evitan tener que preocuparnos por  el orden correcto de los
# argumentos en la llamada a la función aclaran el papel de cada valor en la llamada.
# Vamos a reescribir pets.py usando argumentos de palabra clave para llamar a describe_pet()

def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

# %%


# --- Valores predeterminados ---
# Cuando escribimos una función, podemosdefinir un valor para cada parámetro.
# Si se proporciona un argumento para un parámetro enla llamada a la función, Pthon
# usa el valor del argumento. De lo contrario, utiliza el valor predeterminado del
# parámetro. Así al definir un valor predeterminado para un parámetro, podemos excluir
# el argumento correspondiente que normalmente escribiríamos en la llamada a la función.
# Usar valores predeterminados permite simplificar las llamadas a funciones y aclarar de
# qué forma se suelen utilizar nuestras funciones.
# Por ejemplo, si observa que la mayoría de las llamadas a describe_pet() se usan para
# describir perros, puede establecer el valor predeterminado de animal_type en 'dog'
# Entonces, cualquier que llame a describe_pet() para describir un perro podrá
# omitir esa información.
# Cuando use valores predeterminados, debe colocar cualquier parámetro con un valor
# predeterminado después de todos los parámetros que no tienen valores predeterminados.
# De este modo, Python podrá seguir interpretando argumentos posicionales correctamente.


def describe_pet(pet_name, animal_type='dog'):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# %%
