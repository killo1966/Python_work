#%%
# 8-3 Camiseta: Escriba una función llamada hacer_camiseta() que acepte una talla y un texto
# para un mensaje que habría que imprimir en la camiseta. La función debería imprimir una
# frase resumiendo la talla de la camiseta y el mensaje impreso.
# Llame a la función una vez con argumentos posicionales para hacer una camiseta.
# Llame a la función por segunda vez usando argumentos de palabra clave.


# Llamada a la camiseta con argumentos posicionales
def hacer_camiseta(talla, texto):
    """Muestra información sobre la camiseta"""
    print(f"\n talla {talla}, esta camiseta es de {texto}.")


hacer_camiseta(42,'algodon')
hacer_camiseta(talla=42, texto='algodon')

# %%

# 8-4 Camisetas grandes: Modifique la función hacer"_camiseta() para que las camisetas
# sean grandes por defecto con un mensaje que diga "Me encanta Python" Haga una camiseta grande
# y una mediana con el mensaje predeterminado y una de cualquier talla con un mensaje diferente

def hacer_camiseta(talla='Grande', mensaje='Me encanta Python'):
    """Muestra información sobre la camiseta"""
    print(f"\nTodas estas camisetas son de talla {talla}.")
    print(f"Estoy aprendiendo Python y veo que: {mensaje}:")

# Camiseta Grande con mensaje predeterminado
hacer_camiseta()

# Camiseta mediana con mensaje predeterminado
hacer_camiseta(talla='Mediana')

# Camiseta Pequeña con un mensaje diferente
hacer_camiseta('Pequeña', 'debería haber empezado antes!!!')

# %%


# 8-5 Ciudades:  Escriba una función llamada describir_ciudad() que acepte el nombre de una
# ciudad y su país. La función debería imprimir una oración simple, como "Reikiavik está en Islandia"
# Dé al parametro del país un valor predeterminado. Llame a la función para tres ciudades diferentes,
# con al menos una que no esté en el país predeterminado.

def describir_ciudad(ciudad, país='España'):
    """La función muestra la ciudad y el País en el que se encuentra"""
    print(f"\nLa ciudad de {ciudad.title()}, pertenece a: {país.title()}.")

describir_ciudad('malaga')
describir_ciudad('cadiz')
describir_ciudad('londres', país='Reino Unido')
# %%
