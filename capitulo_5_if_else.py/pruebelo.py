# 5-3 Colores de aliens #1
color_alien = 'rojo'
if color_alien == 'verde':
    print(f"El color del alien es: {color_alien}, por tanto ha ganado 5 puntos")
else:
    print('')

# 5-4 Colores de aliens #2
color_alien = 'verde'
if color_alien == 'verde':
    print(f"El color de alien es verde, haganado 5 puntos por disparar al alien")
if color_alien != 'verde':
    print(f"El alien no es verde, ha ganado 10 puntos")
# 5-4 Colores de aliens #2 bis

color_alien = 'rojo'
if color_alien == 'verde':
    print(f"El colo del alien es verde, ha ganado 5 puntos")
else:
    print(f"El alien no es verde, ha ganado 10 puntos")

# 5-5 Colores de aliens #3
color_alien = 'rojo'
if color_alien == 'verde':
    print(f"El alien al que disparó es: {color_alien}, ha ganado 5 puntos")
elif color_alien == 'amarillo':
    print(f"El alien al que disparó es: {color_alien}, ha ganado 10 puntos")
else:
    print(f"El alien al que disparó es: {color_alien}, ha gando 15 puntos")

# 5-6 Etapas vitales
edad = 65
if edad < 2:
    print(f"Usted es un bebé ya que su edad es de: {edad} años")
elif edad >= 2 and  edad < 4:
    print(f"Usted es un niño pequeño, ya que su edad es de: {edad} años")
elif edad >= 4 and edad < 13:
    print(f"Usted es un niño, ya que su edad es de: {edad} años")
elif edad >= 13 and edad < 20:
    print(f"Usted es un adolescente, ya que su edad es de: {edad} años")
elif edad >= 20 and edad < 65:
    print(f"Usted es un adulto, ya que su edad es de: {edad} años")
else:
    print(f"Usted tiene 65 o mas años, su edad es de: {edad} años")


# 5-7 Fruta Favorita
frutas_favoritas = ['manzanas', 'platanos', 'peras', 'uvas', 'melocotones']
for fruta_favorita in frutas_favoritas:
    if fruta_favorita == 'manzanas':
        print(f"Las {fruta_favorita} mantienen la boca sana")
    if fruta_favorita == 'platanos':
        print(f"Los {fruta_favorita}, siempre de Canarias")
    if fruta_favorita == 'peras':
        print(f"Me gustan las {fruta_favorita} conferencia")
    if fruta_favorita == 'uvas':
        print(f"Las {fruta_favorita} me gustan tanto negras como blancas")
    if fruta_favorita == 'melocotones':
        print(f"Los {fruta_favorita} siempre grandes y tiernos")

# 5-8 Hola, Admin
nombres_usuarios = ['admin', 'juan', 'pedro', 'jose', 'antonio', 'andres', 'jose antonio', 'luis']
for nombre_usuario in nombres_usuarios:
    if nombre_usuario == 'admin':
        print(f"Hola {nombre_usuario.title()}, quieres ver uninforme de estado?")
    if nombre_usuario == 'juan':
        print(f"Hola {nombre_usuario.title()}, nos encanta tenerte de nuevo por aquí")
    if nombre_usuario == 'pedro':
        print(f"Hola {nombre_usuario.title()}, Bienvenido")
    if nombre_usuario == 'jose':
            print(f"Hola {nombre_usuario.title()}, Buenos días")
    if nombre_usuario == 'antonio':
            print(f"Hola {nombre_usuario.title()}, ya estas logeado")
    if nombre_usuario == 'andres':
            print(f"Hola {nombre_usuario.title()}, has hecho login correctamente!!!")
    if nombre_usuario == 'jose antonio':
            print(f"Hola {nombre_usuario.title()}, Bienvenido a nuestra web")
    if nombre_usuario == 'luis':
            print(f"Hola {nombre_usuario.title()}, sé Bienvenido")

# 5-9 Sin usuarios
