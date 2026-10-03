coche = 'subaru'
print(coche == 'subaru')
print(coche == 'audi')

print("Is car == 'subaru' I predict True.")
print(coche == 'subaru')


# Comprobamos si un elemento está o no está en una lista
verduras = ['lechugas', 'calabazas', 'pimientos', 'calabacines']
verdura = 'pepinos'
if verdura not in verduras:
    (f"No tenemos {verdura.title()}, debemos comprar")
verdura = 'lechugas'
if verdura in verduras:
    (f"No compres mas {verdura.title()}, se nos van a pasar")
