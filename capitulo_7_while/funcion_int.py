# Cuando usamos la función input python interpreta que todo lo que se introduce son cadenas
# si queremos que un número no se trate como una cadena se usa la función int

edad = input("Por favor introduzca su edad y le diré si es mayor de edad en España: ")
edad = int(edad)
if edad < 18:
    print(f"En España con {edad} años eres menor de edad")
else:
    print(f"En España con su edad: {edad} años, usted ya es considerado mayor de edad")

print(f"\tGracias por informarnos de su edad")
