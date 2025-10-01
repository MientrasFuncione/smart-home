class Usuario:
    def __init__(
        self, id, nombre, email, telefono=None, contraseña=None, rol="usuario"
    ):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__contraseña = contraseña
        self.__rol = rol

    def __str__(self):
        return f"Usuario(id={self.__id}, nombre={self.__nombre}, email={self.__email}, telefono={self.__telefono}, rol={self.__rol})"

    # id
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    # nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nuevo_nombre

    # email
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        if "@" not in nuevo_email or "." not in nuevo_email:
            raise ValueError("El email no es válido.")
        self.__email = nuevo_email

    # telefono
    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono

    # contraseña
    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        if not nueva_contraseña or len(nueva_contraseña) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres.")
        self.__contraseña = nueva_contraseña

    def validar_contraseña(self, contraseña):
        return self.__contraseña == contraseña
