import pytest
from app.dominio.automatizacion import Automatizacion


def test_automatizacion_activar():
    automatizacion = Automatizacion(
        1,
        "Encender todos los dispositivos",
        "Enciende todos los dispositivos",
        estado="activa",
    )
    assert automatizacion.id == 1
    assert automatizacion.nombre == "Encender todos los dispositivos"
    assert automatizacion.descripcion == "Enciende todos los dispositivos"
    assert automatizacion.estado == "activa"


def test_automatizacion_apagar():
    automatizacion = Automatizacion(
        1,
        "Apagar todos los dispositivos",
        "Apaga todos los dispositivos",
        estado="activa",
    )
    assert automatizacion.id == 1
    assert automatizacion.nombre == "Apagar todos los dispositivos"
    assert automatizacion.descripcion == "Apaga todos los dispositivos"
    assert automatizacion.estado == "activa"


def test_automatizacion_inactiva():
    automatizacion = Automatizacion(
        1,
        "Encender todos los dispositivos",
        "Enciende todos los dispositivos",
    )
    assert automatizacion.id == 1
    assert automatizacion.nombre == "Encender todos los dispositivos"
    assert automatizacion.descripcion == "Enciende todos los dispositivos"
    assert automatizacion.estado == "inactiva"


def test_automatizacion_inactiva():
    automatizacion = Automatizacion(
        1,
        "Apagar todos los dispositivos",
        "Apaga todos los dispositivos",
    )
    assert automatizacion.id == 1
    assert automatizacion.nombre == "Apagar todos los dispositivos"
    assert automatizacion.descripcion == "Apaga todos los dispositivos"
    assert automatizacion.estado == "inactiva"

# python -m pytest test/test_automatizacion.py -v