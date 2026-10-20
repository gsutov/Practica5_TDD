import pytest
from envio import calcular_envio

def test_estandar_paquete_pequeno_cuesta_50():
    assert calcular_envio(3, "estandar") == 50

def test_estandar_5kg_cuesta_50():
    assert calcular_envio(5, "estandar") == 50

def test_estandar_6kg_cuesta_60():
    assert calcular_envio(6, "estandar") == 60

def test_estandar_7kg_cuesta_70():
    assert calcular_envio(7, "estandar") == 70

def test_express_paquete_pequeno_cuesta_100():
    assert calcular_envio(3, "express") == 100