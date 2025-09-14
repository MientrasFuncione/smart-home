import pytest
from src.app.usuario import Usuario


def test_rol_admin_valido():
    usuario = Usuario(1, "Gadiel", "correo@correo.com")
    usuario.rol = "admin"
    assert usuario.rol == "admin"


def test_rol_usuario_valido():
    usuario = Usuario(1, "Gadiel", "correo@correo.com")
    usuario.rol = "usuario"
    assert usuario.rol == "usuario"


def test_agregar_usuario():
    usuario = Usuario(
        id=1,
        nombre="Gadiel",
        email="correo@correo",
        telefono="123456789",
        contraseña="1234",
        rol="admin",
    )

    assert usuario.nombre == "Gadiel"
    assert usuario.email == "correo@correo"
    assert usuario.telefono == "123456789"
    assert usuario.rol == "admin"


def test_contraseña():
    usuario = Usuario(1, "Gadiel", "correo@correo.com", "123546897", "admin")
    assert usuario.contraseña == usuario.contraseña


# python -m pytest test/test_usuario.py -v
