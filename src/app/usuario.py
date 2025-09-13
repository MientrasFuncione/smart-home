class Usuario:
    def __init__(
        self, id, nombre, email, telefono=None, contraseña=None, rol="usuario"
    ):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.__contraseña = contraseña  # Atributo privado
        self._rol = rol

    def __str__(self):
        return f"Usuario(id={self.id}, nombre={self.nombre}, email={self.email}, telefono={self.telefono}, rol={self._rol})"

    # getter de la contraseña, mala practica, pero lo pide para armar el setter
    @property
    def contraseña(self):
        return self.__contraseña

    # setter de la contraseña
    @contraseña.setter
    def contraseña(self, nueva_contraseña):
        if not nueva_contraseña or len(nueva_contraseña) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres.")

        self.__contraseña = nueva_contraseña

    # validación de contraseña
    def validar_contraseña(self, contraseña):
        return self.__contraseña == contraseña

    # getter del rol
    @property
    def rol(self):
        return self._rol

    # setter del rol
    @rol.setter
    def rol(self, nuevo_rol):
        if nuevo_rol not in ["usuario", "admin"]:
            raise ValueError("El rol debe ser 'usuario' o 'admin'.")
        self._rol = nuevo_rol
