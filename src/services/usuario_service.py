from app.usuario import Usuario


class UsuarioService:
    def __init__(self):
        self.usuarios = []
        self.id_contar = 1

    def registrar_usuario(
        self, nombre, email, telefono=None, contraseña=None, rol="usuario"
    ):
        for usuario in self.usuarios:
            if usuario.nombre == nombre or usuario.email == email:
                raise ValueError("El nombre o email ya existe.")

        if not self.usuarios:
            rol = "admin"  # El primer usuario registrado es admin

        nuevo_usuario = Usuario(
            self.id_contar, nombre, email, telefono, contraseña, rol
        )
        self.id_contar += 1

        self.usuarios.append(nuevo_usuario)
        print(f"Usuario {nombre} registrado correctamente.")

    def iniciar_sesion(self, nombre, contraseña):
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.validar_contraseña(contraseña):
                print(f"Bienvenido, {nombre}!")
                return usuario
        raise ValueError("Nombre o contraseña incorrectos.")

    def verificar_estado(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                return usuario.rol

    def modificar_rol_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                usuario.rol = "admin"
                print(f"El usuario {nombre} ahora es admin")
                return
        raise ValueError("El usuario no existe.")


if __name__ == "__main__":
    servicio = UsuarioService()
    servicio.registrar_usuario("Gadiel", "correo@correo.com", "3518053537", "123456789")

    print(servicio.usuarios[0])
    print(servicio.usuarios[0].nombre)
    print(servicio.usuarios[0].email)

    servicio.iniciar_sesion("Gadiel", "123456789")
    # servicio.iniciar_sesion("Gadiel", "12345678") # error

