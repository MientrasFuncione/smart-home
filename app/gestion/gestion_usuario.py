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
