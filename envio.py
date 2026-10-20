def calcular_envio(peso, tipo):
    costo = 50
    if peso > 5:
        return 50 + 10 * (peso -5)
    if tipo == "express":
        costo *= 2
    return costo