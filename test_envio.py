import pytest
from envio import calcular_envio

# Ciclo 1
def test_estandar_paquete_pequeno_cuesta_50():
    assert calcular_envio(3, "estandar") == 50

# Ciclo 2
def test_estandar_5kg_cuesta_50():
    assert calcular_envio(5, "estandar") == 50

def test_estandar_6kg_cuesta_60():
    assert calcular_envio(6, "estandar") == 60

def test_estandar_7kg_cuesta_70():
    assert calcular_envio(7, "estandar") == 70

# Ciclo 3
def test_express_paquete_pequeno_cuesta_100():
    assert calcular_envio(3, "express") == 100

def test_express_paquete_pesado_cuesta_140():
    assert calcular_envio(7, "express") == 140

# Ciclo 4
def test_0kg ():
    with pytest.raises(ValueError):
        calcular_envio(0, "express")

def test_peso_negativo ():
    with pytest.raises(ValueError):
        calcular_envio(-3, "express")

# Ciclo 5
def test_tipo_envio_invalido():
    with pytest.raises(ValueError):
        calcular_envio(3, "batman")