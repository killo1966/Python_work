coste_cena = 101    # Importe base de la cena
IMPUESTOS = 0.21    # Constante relativa a los impuestos a pagar (IVA)
coste_impuestos = coste_cena * IMPUESTOS    # Importe de los impuestos
personas = 4
coste_total = coste_cena + coste_impuestos
coste_persona = coste_total / personas
despedida = "Esperamos que todo haya sido de su agrado"
cabecera_ticket = "restaurante ramon"
direccion = "avenida buen comer, 25 (murcia)"
reservas = "Pueden hacer sus reservas en el 668334455"
print(f"{cabecera_ticket.title()}\n{direccion.title()}\n\nCoste de la cena: {coste_cena} euros\nImpuestos: {coste_impuestos:.2f} euros\nTotal incluido Impuestos: {coste_total:.2f} euros\nPrecio a pagar por persona: {coste_persona:.2f} euros\n\n{despedida}\n{reservas}")