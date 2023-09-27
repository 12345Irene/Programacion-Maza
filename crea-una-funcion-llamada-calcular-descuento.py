def calculardescuento(monto_total, porcentaje_descuento=10):
    # calcula el descuento aplicando el porcentaje al monto total
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento


monto_total_compra: int = 100
descuento_calculado = calculardescuento(monto_total_compra)
print(f"El descuento calculado es: {descuento_calculado}")