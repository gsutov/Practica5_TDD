limite_de_peso = 5
costo_base = 50
costo_extra = 10

def calcular_envio(peso, tipo):
    # Validaciones
    if peso <= 0:
        raise ValueError("El peso debe ser mayor o igual a 0kg")
    if tipo not in ["estandar", "express"]:
        raise ValueError("Tipo de envío inválido")
    
    costo = costo_base
    if peso > limite_de_peso:
        costo += costo_extra * (peso - limite_de_peso)
    if tipo == "express":
        costo *= 2
    return costo