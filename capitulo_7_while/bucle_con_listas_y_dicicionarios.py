# Un bucle for es efectivopara pasar por una lista, pero no conviene modificar
# una lista dentro de un bucle for porque Python tendrá problemas paa hacer el 
# seguimiento delos elementos de la lista. Si hay que modificar una lista cuando
# se trabaja con ella, es mejor usar unbucle while. Emplear bucles while con listas
# y diccionarios nos permite recoger, almacenar y organizar muchas entradas para
# examinarlas e informar luego.

# --- Pasar elementos deuna lista a otra ---

# ejemplo: mover usuarios de una lista no confirmada a una lista confirmada

# Empieza con usuarios que hay que confirmar,
# y una lista vacía para alojar a los usuarios confirmados.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifica cada usuario hasta que ya no hay usuarios sin confirmar.
# Mueve a cada usuario verificado a la lisa de usuarios confirmados.

while unconfirmed_users:
    current_users =  unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

# Muestra todos los usuarios confirmados.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
