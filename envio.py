def calcular_envio(peso, tipo):
    if peso <= 0:
        raise ValueError("El peso debe ser mayor o igual a 0kg")
    costo = 50
    if peso > 5:
        costo += 10 * (peso -5)
    if tipo == "express":
        costo *= 2
    return costo