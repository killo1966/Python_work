# 4-3 Contar hasta 20 primero y último incluidos
for i in range(1, 21):
    print(i)
print("_____________________________________________________________\n")

# 4-5 Sumar hasta 100
lista_numerica = list(range(1,101))
print(lista_numerica)
total_suma = sum(lista_numerica)
print(f"El total de la suma de los 100 primeros números es: {total_suma}")
print(f"El menor de todos los números es: {min(lista_numerica)}")
print(f"El mayor de todos los números es: {max(lista_numerica)}")

print("_____________________________________________________________\n")    

# 4-6 Númros impares
print(f"Los números son: ")
for i in range(1,20,2):
    print(i)
print("_____________________________________________________________\n")

#4-7 Treses
print("Estos son los múltiplos de tres hasta el 30")
for i in range(3, 33, 3):
    print(i) 
print("_____________________________________________________________\n")

# 4-8 Cubos
for i in range(1,11):
    cubo = i ** 3
    print(f"El cubo de {i} es, {cubo}")
print("_____________________________________________________________\n")

# 4-9 Comprensión de cubos. Usar una lista por comprensión para los 10 primeros cubos
for j in range(1, 11):
    print(f"El cubo de {j} es, {j ** 3 }")
