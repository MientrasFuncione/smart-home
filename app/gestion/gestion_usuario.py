from app.dominio.usuario import Usuario


class GestionUsuario:
    def __init__(self, usuario_dao):
        self.usuario_dao = usuario_dao

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

    def modificar_rol_usuario(self, nombre):
        pass
