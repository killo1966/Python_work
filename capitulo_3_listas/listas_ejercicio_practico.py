invitados = ['carlos', 'sergio', 'andres', 'luis']  # Lista inicial
print(f"Lista inicial de invitados: {invitados}")
print(f"Espero que vengas a mi cena de cumpleaños {invitados[0].title()}")  # Mensaje de Bienvenida personalizado
print(f"Me alegraría mucho que asistieras a mi cena de cumpleaños {invitados[1].title()}") # Mensaje de Bienvenida personalizado
print(f"Sería un placer verte de nuevo este año {invitados[2].title()}") # Mensaje de Bienvenida personalizado
print(f"Podria contar contigo este año, {invitados[3].title()}, los demás ya están confirmando. Lo pasaremos genial") # Mensaje de Bienvenida personalizado

invitados.pop()  # luis tiene un imprevisto y no podrá venir
print(invitados)
invitados.append('marta') # Se invita en su lugar a marta
print(f"La nueva lista de invitados después del imprevisto de Luis es: {invitados}")
message = "Noticias, chic@s, aún seremos más, he encontrado un restaurante con una mesa mas grande"
print(message)

invitados.insert(0,'lola')
invitados.insert(3, 'vickie')
invitados.append('monica')
print(f"Ahora, seremos más. Nueva lista de invitados: {invitados}")
print(sorted(invitados))
print(f"La lista de invitados al final contiene {len(invitados)}, invitados")

invitados.sort()
print(invitados)






