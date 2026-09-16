name = "Javier"
last_name = "Serrano"
full_name = f"{name} {last_name}" # Concatenación de cadenas usando f-strings. 
message = f"Hola, {full_name.title()}. Bienvenido al curso de Python." # Formateo de la cadena de mensaje. 
print(message)

# Añadir espacios en blanco a cadenas con tabulaciones o nuevas líneas.
print("Python")
print("\tPython") # Añadir una tabulación antes de la palabra "Python".
print("Python\nJavascript") # Añadir una nueva línea entre las dos palabras.

print("Languages:\n\tPython\n\tJavascript\n\tC++") # Añadir una nueva línea y tabulaciones para listar los lenguajes.

favorite_language = ' html '
print(favorite_language) # Imprime la cadena con espacios en blanco.
print(favorite_language.rstrip()) # Imprime la cadena sin espacios en blanco a la derecha.
favorite_language = favorite_language.rstrip() # Elimina los espacios en blanco a la derecha de la cadena.

favorite_language = ' css '
print(favorite_language) # Imprime la cadena con espacios en blanco.
print(favorite_language.lstrip()) # Imprime la cadena sin espacios en blanco a la izquierda.
favorite_language = favorite_language.lstrip() # Elimina los espacios en blanco a la izquierda de la cadena.
print(favorite_language) # Imprime la cadena sin espacios en blanco a la izquierda. 

# Eliminar prefjijos

url = 'https://www.python.org/'
url.removeprefix('https://') # Elimina el prefijo 'https://' de la cadena.
print(url.removeprefix('https://')) # Imprime la cadena sin el prefijo 'https://'.

# Asinación multiple
x, y, z, t = 10, 20, 30, 40
print(x, y, z, t) # Imprime los valores de las variables x, y, z y t.
print(x + t)

suma = 2 + 3
print(suma) # Imprime el resultado de la suma de 2 y 3.
resta = 5 - 2
print(resta) # Imprime el resultado de la resta de 5 y 2.
multiplicacion = 2 * 3
print(multiplicacion) # Imprime el resultado de la multiplicación de 2 y 3.
division = 6 / 2
print(division) # Imprime el resultado de la división de 6 y 2.
