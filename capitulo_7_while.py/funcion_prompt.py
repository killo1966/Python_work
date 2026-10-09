# A veces necesitará escribir unas instrucciones demas de una línea.
# Puede asignar las indicaciones a una variable para paarla a la función input()

prompt = "Si tu compartes tu nombre, podremos personalizar el mensaje que ves"
prompt += "\n Cual es tu nombre? "

nombre = input(prompt)
print(f"\n Hola, {nombre.title()}!")

