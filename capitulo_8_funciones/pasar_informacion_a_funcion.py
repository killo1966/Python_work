# Si modificamos ligeramente la función greet_user(), saludará al usuario por
# su nombre. Para que esto suceda, escribiremos username entre los parentesis
# de definición en def greet_user(). Al añadir aquí username, permitimos que
# la función acepte cualquier valor para username cada vez que la llamemos
# Al llamar a greet_user(), podemos pasarle un nombre, como 'jesse' dentro
# de los parentesis.

#%%
def greet_user(username):
    """Muestra un simple saludo"""
    print(f"Hello, {username.title()}!")

greet_user('javi')

# Argumentos y parámetros
# Un argumento es una información que se pasa desde una funciñon para llamar a una función.
# Cuando llamamos a la función, colocamos el falor con el que queremos que trabaje entre
# parentesis. En este caso, pasamos el argumento 'javi' al función geet_user() y asignamos
# el valor al parámetro username