alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
newpoints = alien_0['points']
print(f"El número de puntos por matar al alien verde es: {newpoints} puntos")

# Como añadir elementos clave valor en un diccionario

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_1 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print(f"Original position, x_position: {alien_1['x_position']}")

# Mueve el alien hacia la derecha
# Determina cuánto se mueve el alien basándose en su velocidad actual

alien_1['speed'] = 'fast'

if alien_1['speed']  == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # Debe ser un alien rápido
    x_increment = 3

# La nueva posición es la antigua más el incremento
alien_1['x_position'] = alien_1['x_position'] + x_increment
print(f"La nueva posición del alient es: {alien_1['x_position']}")

