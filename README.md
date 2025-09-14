# Modulo Programador - ( Tercera Instancia )

### Introducción

En esta instancia, seguimos con el proyecto smart-home, pero a diferencia del anterior donde se trabaja la programación estructurada, en este lo abordaremos sobre la Programación Orientada a Objetos.

En esta documentación se vera implementada, los modelos de clase siguiendo lo establecido en los modelos de base de datos.

Se implemento el uso del módulo de pytest, para hacer algunas pruebas unitarias, como la creacion de usuario y dispositivo y respecitvas funciones como apagar y prender.

---

### SRC

En esta carpeta se encuentran dos carpetas; app y services

- app

Contiene las clases desarrolladas, donde se implementaron segun el diagrama de clases y teniendo sentido con el modelo establecido en bases de datos.

- services

Carpeta que contiene las funciones de la evidencia anterior, tales como “registrar_usuario”, “listar_usuarios”…etc.

ya que para esta evidencia no se pedia, es un implemento para estructurar mejor las responsabilidades de las clases.
**ACLARACIÓN: Todos los miembros del equipo (dos) sabemos de su implementación**

---

### PyTest en Usuario

- test_rol_admin_valido()

```python
def test_rol_admin_valido():
    usuario = Usuario(1, "Gadiel", "correo@correo.com")
    usuario.rol = "admin"
    assert usuario.rol == "admin"
```

Permite verficar que la clase Usuario asigne correctamente el rol “admin” a un usuario.

---

- test_rol_usuario_valido

```python
def test_rol_usuario_valido():
    usuario = Usuario(1, "Gadiel", "correo@correo.com")
    usuario.rol = "usuario"
    assert usuario.rol == "usuario"
```

Permite verficar que la clase Usuario asigne correctamente el rol “usuario” a un usuario.

---

- test_agregar_usuario()

```python
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
```

Permite instanciar de manera correcta el objeto de Usuario.

---

- test_cambiar_contraseña()

```python
def test_cambiar_contraseña():
    usuario = Usuario(
        3, "Gadiel", "correo@correo.com", contraseña="123456789", rol="admin"
    )
    usuario.contraseña = "987654321"
    assert usuario.contraseña == "987654321"
```

Permite cambiar correctamente la contraseña , asegurandose de pasar las validaciones, en este caso, la contraseña debe tener mas de cuatro (4) caracteres.

---

### PyTest en Dispositivo

- test_crear_dispositivo()

```python
def test_crear_dispositivo():
    dispositivo = Dispositivo(1, "Monteabaro", "LG", "Aspiradora")
    assert dispositivo.id == 1
    assert dispositivo.nombre == "Monteabaro"
    assert dispositivo.marca == "LG"
    assert dispositivo.tipo == "Aspiradora"
    assert dispositivo.estado == "apagado"
```

Permite instanciar de manera correcta el objeto Dispositivo

---

- test_encender()

```python

def test_encender():
    dispositivo = Dispositivo(1, "Monteabaro", "Aspiradora", "LG")

    dispositivo.encender_dispositivo()
    assert dispositivo.estado == "encendido"
```

Permite verificar que un dispositivo cuyo estado esta en “apagado” cambie a “encendido”

---

- test_apagar()

```python
def test_apagar():
    dispositivo = Dispositivo(1, "Monteabaro", "Aspiradora", "LG", estado="encendido")

    dispositivo.apagar_dispositivo()
    assert dispositivo.estado == "apagado"
```

Permite verificar dispositivo cuyo estado esta en “encendido” cambie a “apagado”

---

**ACLARACIÓN GENERAL DE DESARROLLO**

Nuestro grupo conto de numerosas bajas en el desarrollo y la incorporacion de un nuevo integrante, quedando solamente dos al momento de desarrollar, se hicieron modificaciones con respecto al trabajo anterior (habladas y aprobadas por el equipo)
