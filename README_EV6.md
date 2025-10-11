# Modulo Programador - ( Tercera Instancia )

### Introducción

En esta instancia, a partir de las clases previamente implementadas en el **dominio**, se incorporan las **clases e interfaces correspondientes al patrón de diseño DAO**, con el objetivo de **separar la lógica de acceso a datos de la lógica de negocio**.

Además, se implementa la **conexión a la base de datos** utilizando el motor **MySQL**, lo que permite generar **persistencia** para los datos del sistema.

El programa se ejecutará desde consola, a través del menú principal implementado en el archivo **main.py**, desde el cual será posible realizar las siguientes acciones:

- **Registrar un nuevo usuario estándar**, el cual quedará almacenado en la base de datos.
- **Iniciar sesión en el programa**, siempre que las credenciales ingresadas coincidan con un usuario previamente registrado.
- **Usuario estándar:** una vez autenticado, podrá consultar sus datos personales y visualizar todos los dispositivos registrados en la base de datos.
- **Usuario administrador:** además de poder iniciar sesión, tendrá acceso a la **gestión completa de dispositivos (CRUD)** y a la posibilidad de **modificar el rol** de un usuario específico.
---

### Estructura del Proyecto

En el directorio **app** se encuentran los componentes principales del proyecto. Allí tendremos los **objetos de dominio**, cada uno con sus respectivos atributos y métodos.

Dentro de **app** estará el directorio **dao**, encargado de manejar la **lógica de acceso a datos**, separándola de la **lógica de negocio**, que se encuentra en el directorio **gestion**.

En el interior de **dao** encontraremos el subdirectorio **interfaces**, donde se definen los métodos que realizan las operaciones **CRUD** y otras interacciones con la base de datos. Esto resulta fundamental para mantener una **implementación desacoplada** de los detalles de persistencia.

También dispondremos del directorio **test**, que contendrá las **pruebas unitarias** relacionadas con nuestro **dominio**, asegurando el correcto funcionamiento de las clases y métodos.

El archivo **.gitignore** permitirá indicarle a Git qué archivos o directorios no deben ser rastreados, como por ejemplo el archivo **.env**, que puede contener información sensible sobre la base de datos o configuraciones locales.

Finalmente, el archivo principal **main.py** será el punto de entrada del programa: allí se integrarán todos los módulos y se mostrará un **menú en consola**, desde el cual podremos visualizar y manipular la información de forma práctica.
---

### Conexion a MySQL

```python
import os
import mysql.connector
from dotenv import load_dotenv

# variables de entorno
load_dotenv()
HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("USER")
PASS = os.getenv("PASS")
PORT = os.getenv("PORT")

class DBConnection:

    @staticmethod
    def get_connection():
        try:
            return mysql.connector.connect(
                host=HOST, database=DB_NAME, user=USER, password=PASS, port=PORT
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

```

En la implementación de la conexión, definimos la clase DBConnection y establecimos la conexión a la base de datos MySQL usando las credenciales guardadas en un archivo de variables de entorno .env, el cual, al estar incluido en .gitignore, no se visualiza en el repositorio de GitHub.

Este código primero se encarga de leer esas variables mediante load_dotenv, para cargar los datos del .env.

La clase DBConnection tiene un método, definido como método estático get_connection, que, a través de un bloque try-except, intenta conectarse a la base de datos con estos parámetros.

En caso de que la conexión sea exitosa, el método devuelve un objeto de conexión de MySQL, que puede ser utilizado para ejecutar consultas mediante un cursor.

Si ocurre un error, como credenciales incorrectas o problemas de acceso, se imprime un mensaje de error en la consola y se retorna None.
---

- **Dispositivo**

```python
from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
    @abstractmethod
    def create_device(self, dispositivo, id_usuario):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, dispositivo):
        pass

    @abstractmethod
    def get_device_by_user(self, id_usuario):
        pass

    @abstractmethod
    def delete(self, id_dispositivo):
```

Se implementa la clase **IDispositivoDAO(ABC)**, la cual establece las reglas básicas para trabajar con los dispositivos en la base de datos.

Podemos consiCderarla como un **molde** que define **qué métodos debe tener** cualquier clase que gestione dispositivos, pero **no especifica cómo deben implementarse**. Esa lógica concreta se desarrolla dentro del DAO.

En el directorio **dao**, se crea el archivo **dispositivo_dao.py**, donde se implementa toda la lógica de acceso a datos relacionada con los dispositivos, siguiendo la estructura definida en la interfaz.

```python
 def create_device(self, dispositivo, id_usuario):
        with self.connection.cursor() as cursor:
            try:
                query = "INSERT INTO Dispositivo (nombre, marca, tipo, estado) VALUES (%s, %s, %s, %s)"
                values = (
                    dispositivo.nombre,
                    dispositivo.marca,
                    dispositivo.tipo,
                    dispositivo.estado,
                )
                cursor.execute(query, values)

                id_dispositivo = cursor.lastrowid

                query = "INSERT INTO DispositivoUsuario (id_usuario,id_dispositivo) VALUES (%s, %s)"
                values = (id_usuario, id_dispositivo)
                cursor.execute(query, values)

                self.connection.commit()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
```

- El metodo **create_device** se encarga de crear un nuevo dispositivo, no solo eso, sino que tambien lo asocia al usuario que lo creo, el cual veremos que solo lo puede implementar el usuario **Admin**

```python
    def get_all(self):
        with self.connection.cursor() as cursor:
            try:
                query = (
                    "SELECT id_dispositivo, nombre,marca,tipo,estado FROM Dispositivo"
                )
                cursor.execute(query)
                rows = cursor.fetchall()
                dispositivos = [Dispositivo(r[0], r[1], r[2], r[3], r[4]) for r in rows]
                return dispositivos

            except mysql.connector.Error as err:
                raise Exception(f"Error al consultar los dispositivos: {err}")
```

- El metodo **get_all**  se encarga de obtener todos los dispositivos guardados en la base de datos, funcionalidad que puede ejecutar el usuario **estandar**.

```python
def update(self, dispositivo):
        with self.connection.cursor() as cursor:
            try:
                query = "UPDATE Dispositivo SET nombre = %s, marca = %s, tipo = %s WHERE id_dispositivo = %s"
                values = (
                    dispositivo.nombre,
                    dispositivo.marca,
                    dispositivo.tipo,
                    dispositivo.id,
                )
                cursor.execute(query, values)
                self.connection.commit()
            except mysql.connector.Error as err:
                raise Exception(f"Error al intenar actualziar el dispositivo: {err}")
```

- El metodo **update** se encarga de actualizar los valores de un dispositivo previamente registrado, probablemente por error del usuario al ingresar datos.

```python
    def get_device_by_user(
        self,
        id_usuario,
    ):
        with self.connection.cursor() as cursor:
            try:
                query = "SELECT d.id_dispositivo, d.nombre, d.marca, d.tipo, d.estado FROM Dispositivo d INNER JOIN DispositivoUsuario ud ON d.id_dispositivo = ud.id_dispositivo WHERE ud.id_usuario = %s"

                cursor.execute(query, (id_usuario,))
                rows = cursor.fetchall()
                return [Dispositivo(r[0], r[1], r[2], r[3], r[4]) for r in rows]
            except mysql.connector.Error as err:
                raise Exception(f"Error al consultar los dispositivos: {err}")
```

- El metodo **get_device_by_user** se encarga de obtener todos los dispositivos vinculados a un determinado usuario, metodo que puede ejecutar el **Admin.**

```python
def delete(self, id_dispositivo):
        with self.connection.cursor() as cursor:
            try:
                query = "DELETE FROM DispositivoUsuario WHERE id_dispositivo = %s"
                cursor.execute(query, (id_dispositivo,))

                query = "DELETE FROM Dispositivo WHERE id_dispositivo = %s"
                cursor.execute(query, (id_dispositivo,))
                self.connection.commit()
            except mysql.connector.Error as err:
                print(f"Error al eliminar dispositivo: {err}")
```

- El metodo **delete** se encarga de eliminar un dispositivo de la base de datos, metodo que solo puede ejecutar el **Admin**

**Aclaracion**

Tener en cuenta que los metodos como eliminar o agregar , tambien trabaja con las tablas intermedias, permitiendo una mejor implementación en el programa.

---

- **Usuario**

```python
from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
    @abstractmethod
    def create(self, usuario):
        pass

    @abstractmethod
    def update_rol_user(self, id_usuario, nuevo_rol):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_user(self, nombre):
        pass

```

Se implementa la clase  IUsuarioDAO(ABC) donde marcamos las reglas para trabajar con los usuarios en la base de datos

Como aclaramos anteriormen,  un molde el cual nos dice que metodos debe tener cualquier clase que maneje usuarios, pero no dice como, eso lo implementamos en el dao

Dentro de nuestro dao, generamos el archivo **usuario_dao.py,** ahi nos encargaremos de toda la lógica de acceso a datos de nuestros dispositivos.

```python

    def create(self, usuario):
        with self.connection.cursor() as cursor:
            try:
                query = "INSERT INTO Usuario (nombre, email, telefono, contraseña, rol) VALUES (%s, %s, %s, %s, %s)"
                values = (
                    usuario.nombre,
                    usuario.email,
                    usuario.telefono,
                    usuario.contraseña,
                    usuario.rol,
                )
                cursor.execute(query, values)
                self.connection.commit()
            except mysql.connector.Error as err:
                print(f"Error: {err}")

```

- El metodo **create** es el encargado de registrar un nuevo usario en la base de datos

```python
 def update_rol_user(self, id_usuario, nuevo_rol):
        with self.connection.cursor() as cursor:
            try:
                query = "UPDATE Usuario SET rol = %s WHERE id_usuario = %s"
                values = (
                    nuevo_rol,
                    id_usuario,
                )
                cursor.execute(query, values)
                self.connection.commit()
            except mysql.connector.Error as err:
                print(f"Error: {err}")
```

- El metodo **update_rol_user** es el encargado de actualizar el rol del usuario, aca es donde podemos asignar un nuevo rol a un usuario determinado, metodo que se explicara en la parte de GestionUsuario

```python
  def get_all(self):
        with self.connection.cursor() as cursor:
            try:
                query = "SELECT id_usuario, nombre, email, telefono,  rol FROM Usuario"
                cursor.execute(query)
                rows = cursor.fetchall()
                usuarios = [
                    Usuario(id=r[0], nombre=r[1], email=r[2], telefono=r[3], rol=r[4])
                    for r in rows
                ]
                return usuarios
            except mysql.connector.Error as err:
                raise Exception(f"Error al listar usuarios: {err}")
```

- El metodo **get_all** nos permite obtener todos los usuarios registrados en la base de datos, donde aclaramos que nos muestre su id, nombre, email, telefono y rol

```python
    def get_user(self, nombre):
        with self.connection.cursor() as cursor:
            try:
                query = "SELECT id_usuario, nombre, email, telefono, contraseña, rol FROM Usuario WHERE nombre = %s"
                cursor.execute(query, (nombre,))
                row = cursor.fetchone()
                if row:
                    return Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
            except mysql.connector.Error as err:
                print(f"Error: {err}")
                return None
```

- El metodo **get_user** nos permite obtener un usuario determinado de la base de datos, el cual es utilizado para implementar el inicio de sesión dentro de nuestro gestor

---

### Gestion Usuario y Gestion Dispositivo

```python
 def registrar_usuario(self, nombre, email, telefono=None, contraseña=None):
        if not nombre or not email:
            return "Nombre, email y contraseña son obligatorios."

        if contraseña is None or len(contraseña) < 4:
            return "La contraseña debe tener al menos 4 caracteres."

        nuevo_usuario = Usuario(None, nombre, email, telefono, contraseña)

        self.usuario_dao.create(nuevo_usuario)
        return f"Usuario {nombre} registrado exitosamente."

    def iniciar_sesion(self, nombre, contraseña):
        usuario = self.usuario_dao.get_user(nombre)

        if usuario and usuario.contraseña == contraseña:
            print(f"Bienvenido {usuario.nombre}")
            return usuario

        return None
    
    def modificar_rol_usuario(self, id_usuario, nuevo_rol):
        if not id_usuario:
            return "El id es necesario para modifcar el rol"
        if nuevo_rol not in ["admin", "usuario"]:
            return "Solo se permite 'admin' o 'usuario'"

        self.usuario_dao.update_rol_user(id_usuario, nuevo_rol)
        return "El rol del usuario fue modificado exitosamente."
    
    def listar_usuarios(self):
        print("Lista de usuarios disponibles: ")
        usuarios = self.usuario_dao.get_all()
        for usuario in usuarios:
            print(usuario)
```

- Podemos visualizar los métodos implementados en la clase GestionUsuario, así como los métodos definidos en el Usuario DAO, que se encargan de la interacción con la base de datos.
- El método registrar_usuario, además de realizar validaciones básicas, crea una instancia de la clase Usuario de nuestro dominio, respetando los principios de la POO, y utiliza el método create del Usuario DAO para guardar el usuario en la base de datos.
- En el método iniciar_sesion, se utiliza el método get_user, que si encuentra al usuario en la base de datos, retorna el objeto correspondiente. Esto nos permite conocer su rol y determinar sus acciones futuras dentro del programa.
- El método modificar_rol_usuario valida que solo se puedan asignar los roles admin o usuario, y modifica el rol del usuario, afectando así las funcionalidades que podrá ejecutar dentro del programa.
- El método listar_usuarios, como su nombre lo indica, permite obtener todos los usuarios registrados, lo cual es útil para decidir a quién se le asignará un nuevo rol.

```python
    def agregar_dispositivo(self, nombre, marca, tipo, id_usuario):
        if not nombre or not marca or not tipo:
            return "El nombre, la marca y el tipo son obligatorios."
        nuevo_dispositivo = Dispositivo(id, nombre, marca, tipo)
        self.dispositivo_dao.create_device(nuevo_dispositivo, id_usuario)
        return "Dispositivo agregado exitosamente."

    def listar_dispositivos(self):
        dispositivos = self.dispositivo_dao.get_all()
        if not dispositivos:
            print("El usuario no tiene registrado ningún dispositivo.")
            return
        for dispositivo in dispositivos:
            print(dispositivo)

    def listar_dispositivo_por_usuario(self, id_usuario):
        dispositivos = self.dispositivo_dao.get_device_by_user(id_usuario)
        for dispositivo in dispositivos:
            print(dispositivo)

    def actualizar_dispositivo(self, id, nombre, marca, tipo):
        if not id or not nombre or not marca or not tipo:
            return "El nombre, la marca y el tipo son obligatorios."

        nuevo_dispositivo = Dispositivo(id, nombre, marca, tipo)
        self.dispositivo_dao.update(nuevo_dispositivo)
        return "Dispositivo editado exitosamente."

    def eliminar_dispositivo(self, id_dispositivo):
        if not id_dispositivo:
            return "El id es obligatorio para eliminar el dispositivo"
        self.dispositivo_dao.delete(id_dispositivo)
        return "Dispositivo eliminado exitosamente."

```

- Podemos visualizar los métodos implementados en la clase GestionDispositivo, así como los métodos definidos en el Dispositivo DAO.
- El método agregar_dispositivo, con algunas validaciones sencillas, crea una instancia de la clase Dispositivo de nuestro dominio, respetando los principios de la POO, y utiliza el método create_device del Dispositivo DAO para guardar el dispositivo en la base de datos.
- Los métodos listar_dispositivos y listar_dispositivo_por_usuario funcionan dependiendo del tipo de usuario: un usuario estándar solo puede listar todos los dispositivos de la aplicación, mientras que un admin puede listar todos los dispositivos y también los dispositivos que él mismo creó en la base de datos.
- El método actualizar_dispositivo permite al admin modificar un dispositivo que haya sido ingresado de manera incorrecta, actualizando los datos vinculados a un ID específico.
- El método eliminar_dispositivo permite al admin borrar un dispositivo de la base de datos, utilizando el método delete implementado en el Dispositivo DAO.

---

### Conclusion

El desarrollo de este proyecto de gestión de dispositivos inteligentes y automatizaciones nos permitió aplicar de manera práctica los conocimientos adquiridos en programación orientada a objetos, manejo de bases de datos y diseño de aplicaciones con distintos niveles de acceso según roles de usuario. Durante el trabajo, se implementaron funcionalidades clave como el registro y autenticación de usuarios, la gestión completa de dispositivos, la asignación de estos a diferentes usuarios y la creación de automatizaciones programadas que permiten encender o apagar dispositivos en horarios específicos.

El proyecto se desarrolló teniendo en cuenta la persistencia de datos mediante MySQL y la separación de responsabilidades mediante el patrón DAO, asegurando así la mantenibilidad y escalabilidad de la aplicación. Además, se buscó ofrecer una experiencia cercana a un sistema de smart home real, donde los usuarios pueden controlar y monitorear los dispositivos de forma centralizada y los administradores tienen la capacidad de gestionar recursos de manera eficiente.

En este contexto, los autores Gadiel y Facundo asumimos la planificación, diseño y desarrollo integral de la aplicación, enfrentando desafíos relacionados con la sincronización de estados entre la base de datos y la lógica de automatización, así como la correcta gestión de permisos según roles de usuario. La realización de este proyecto consolidó nuestras habilidades técnicas y de trabajo en equipo, demostrando nuestra capacidad de llevar un proyecto desde la conceptualización hasta su implementación funcional.