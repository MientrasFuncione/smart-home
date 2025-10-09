from app.dao.usuario_dao import UsuarioDAO
from app.dao.dispositivo_dao import DispositivoDAO
from app.gestion.gestion_usuario import GestionUsuario
from app.gestion.gestion_dispositivo import GestionDispositivo


def main():
    usuario_dao = UsuarioDAO()
    dispositivo_dao = DispositivoDAO()
    gestion_usuario = GestionUsuario(usuario_dao)
    gestion_dispositivo = GestionDispositivo(dispositivo_dao)

    while True:
        accion = input("Iniciar Sesión (1) o Registrar Usuario (2) o salir (3) ")
        if accion == "1":
            nombre = input("Ingresar nombre de usuario: ")
            contraseña = input("Ingresar contraseña: ")

            usuario_logueado = gestion_usuario.iniciar_sesion(nombre, contraseña)

            if usuario_logueado:
                rol = usuario_logueado.rol
                if rol == "usuario":
                    while True:
                        accion = input(
                            "Desea consultar datos personales (1), Consultar dispositivos (2) o salir (3) "
                        )
                        if accion == "1":
                            print(usuario_logueado.mostrar_datos())
                        if accion == "2":
                            gestion_dispositivo.listar_dispositivos_por_usuario(
                                usuario_logueado.id
                            )
                        if accion == "3":
                            break
                elif rol == "admin":
                    print("Funcionalidades de admin")

        if accion == "2":
            nombre = input("Ingresar nombre de usuario: ")
            email = input("Ingresar email: ")
            telefono = input("Ingresar telefono: ")
            contraseña = input("Ingresar contraseña: ")

            gestion_usuario.registrar_usuario(nombre, email, telefono, contraseña)

        if accion == "3":
            break


if __name__ == "__main__":
    main()
