age = 16
if age >= 18:
    print(f"Puedes votar, ya que tienes: {age} años")
else:
    print(f"No puedes votar, tu edad es: {age} y solo se puede votar si eres mayor de 18")

age = 34
if age < 4:
    print(f"Tu entrada es gratuíta por tener menos de 4 años")
elif age < 18:
    print(f"El precio de tu entrada es de 25 euros")
else:
    print(f"El precio de tu entrada es 40 euros")

# en vez imprimir el precio dentro del bloque if-elif-else se imprime al final

age = 23
if age < 8:
    precio = 0
if age < 18:
    precio = 25
else:
    precio = 40
print(f"El precio de su entrada, atendiendo a su edad es: {precio} euros")
