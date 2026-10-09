# 7-1 Coche de alquiler: Escriba un programa que pregunte al usuario qué tipo de 
# coche desea alquilar. Imprima un mensaje sobre el coche, como "Veamos si tenemos un Subaru paa usted"

mensaje = input("Que tipo de coche desea? ")
print(mensaje)
print(f"Veamos si tenemos un Subaru para usted")



# 7-2 Mesa en un restaurante: Escriba un programa que pregunte al usuario cuántos
# vienen a cenar. Si la respuesta es mas de ocho, imprima un mensaje diciendo
# al usuario que tendrán que esperar mesa. De lo contrario, digaleque su mesa 
# está lista.


bienvenida = "Bienvenidos al Restaurante de Javier"
print(bienvenida)
mesa = input("Para cuantos comensales necesita mesa? ")
print(mesa)
mesa = int(mesa)
if mesa > 8 :
    print(f"De momento no nenemos diponible una mesa para {mesa} personas.")
    print(f"El tiempo de espera será de 20 minutos")
else:
    print(f"Pasen, su mesa para {mesa} personas, está preparada")

#%%
# 7-3 Múltiplos de diez: Pida al usuario un número y luego infórmele de 
# si ese número es múltiplo de 10 o no.

mensaje = input(f"Por favor introduzca un múltiplo de 10: ")
mensaje = int(mensaje)
if mensaje % 10 == 0:
    print(f"Felicidades su número {mensaje} es un múltiplo de 10")
else:
    print(f"Lo siento pero el número que ha introducido: {mensaje} no es múltiplo de 10")



# %%
