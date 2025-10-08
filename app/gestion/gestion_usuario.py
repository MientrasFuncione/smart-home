from app.dominio.usuario import Usuario


class GestionUsuario:
    def __init__(self, usuario_dao):
        self.usuario_dao = usuario_dao

    def registrar_usuario(self, nombre, email, telefono=None, contraseña=None):
        # instanciando nuevo usuario
        nuevo_usuario = Usuario(nombre, email, telefono, contraseña)
        self.usuario_dao.create(nuevo_usuario)
        return f"Usuario {nombre} registrado exitosamente."

    def iniciar_sesion(self, nombre, contraseña):
        pass

    def verificar_estado(self, nombre):
        pass

    def modificar_rol_usuario(self, nombre):
        pass
