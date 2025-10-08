from app.dao.usuario_dao import UsuarioDAO
from app.gestion.gestion_usuario import GestionUsuario


def main():
    usuario_dao = UsuarioDAO()
    usuario = GestionUsuario(usuario_dao)

    while True:
        accion = input("Registrar Usuario (1) o salir (3) ")
        if accion == "1":
            nombre = input("Ingresar nombre de usuario: ")
            email = input("Ingresar email: ")
            telefono = input("Ingresar telefono: ")
            contraseña = input("Ingresar contraseña: ")
            usuario.registrar_usuario(nombre, email, telefono, contraseña)


if __name__ == "__main__":
    main()
