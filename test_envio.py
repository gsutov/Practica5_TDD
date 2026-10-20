import pytest
from envio import calcular_envio

def test_estandar_paquete_pequeno_cuesta_50():
    assert calcular_envio(3, "estandar") == 50