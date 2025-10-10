import pytest
from app.dominio.dispositivo import Dispositivo


def test_crear_dispositivo():
    dispositivo = Dispositivo(1, "Monteabaro", "LG", "Aspiradora")
    assert dispositivo.id == 1
    assert dispositivo.nombre == "Monteabaro"
    assert dispositivo.marca == "LG"
    assert dispositivo.tipo == "Aspiradora"
    assert dispositivo.estado == "apagado"


def test_encender():
    dispositivo = Dispositivo(1, "Monteabaro", "Aspiradora", "LG")

    dispositivo.encender_dispositivo()
    assert dispositivo.estado == "encendido"


def test_apagar():
    dispositivo = Dispositivo(1, "Monteabaro", "Aspiradora", "LG", estado="encendido")

    dispositivo.apagar_dispositivo()
    assert dispositivo.estado == "apagado"


# python -m pytest test/test_dispositivo.py -v
