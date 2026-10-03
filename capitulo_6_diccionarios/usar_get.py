# Usar claves entre corchetes para recuperar el valor que nos interesa
# en un diccionario puede causar un problema si la clave que pedimos no existe

alien_0 = {'color':'green', 'speed':'slow'}
print(alien_0['points'])


# El método get() requiere una clave como primer argumento. Como segundo argumento
# opcional, podemos pasar el valor que se devolverá si la clave no existe.

alien_0 = {'color':'green', 'speed':'slow'}
point_value = alien_0.get('points', 'not point value assigned')
print(point_value)

