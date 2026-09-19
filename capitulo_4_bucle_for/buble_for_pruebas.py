dulces = ['merenges', 'borrachos', 'tartas_de_san_marcos', 'rosco_vino', 'magdalenas']
caracteristicas = ['cremosos', 'blandos', 'dulces', 'aromaticos', 'espumosas']
for i in range(len(dulces)):
    print(f"Los/Las {dulces[i]}, estan muy {caracteristicas[i]}.")

platos = ('ensalada,', 'huevos_fritos', 'pollo_asado', 'lentejas', 'alubias')
print(len(platos))


bufé = ('centollo', 'lubina', 'pollo_asado', 'lentejas', 'alubias')
print("Los platos del menú son:")
for plato in platos:
    print(plato.title())

