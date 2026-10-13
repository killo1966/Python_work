# 8-1: Mensaje: Escriba una función llamada mostrar_mensaje() que imprima
# una oración diciendo a todos lo que está aprendiendo en este capítulo.
# Llame a la función y asegúrese de que el mensaje se muestra claramente.

def mostrar_mensaje():
    """Mostrar mensaje de lo mucho que aprendo"""
    print(f"Con este curso de python aprendo mogollón")

# Ahora desde aquí abajo llamo a la función

mostrar_mensaje()

#%%
# 8-2. Libro favorito: Escriba una función llmada libro_favorito() que acepte
# un parámetro título. La función debería imprimir un mensaje como "Uno de mis
# libros favoritos es Alicia en el País de las Maravillas". Llame a la función
# asegurandose de incluir el título de un libro como argumento en la llamada a 
# función.

def libro_favorito(titulo):
    """Muestra el título de un libro y un mensaje"""
    print(f"{titulo}, es un magnifico libro basado en la época de Cristo")

libro_favorito('Caballo de Troya')
