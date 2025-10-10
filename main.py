import time
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
        accion = input("Iniciar Sesión (1) o Registrar Usuario (2) o salir (3): ")
        if accion == "1":
            nombre = input("Ingresar nombre de usuario: ")
            contraseña = input("Ingresar contraseña: ")

            usuario_logueado = gestion_usuario.iniciar_sesion(nombre, contraseña)

            if usuario_logueado:
                rol = usuario_logueado.rol
                if rol == "usuario":
                    while True:
                        accion = input(
                            "Desea consultar datos personales (1), Consultar dispositivos (2) o salir (3): "
                        )
                        if accion == "1":
                            print(usuario_logueado.mostrar_datos())
                        if accion == "2":
                            gestion_dispositivo.listar_dispositivos()
                        if accion == "3":
                            time.sleep(1.5)
                            print("Cerrando Sesion...")
                            break
                elif rol == "admin":
                    while True:
                        accion = input(
                            "Desea Gestionar dispositivos (1), Modificar rol de un usuario (2) o salir (3): "
                        )
                        if accion == "1":
                            while True:
                                accion = input(
                                    "Desea agregar dispositivo (1), Consultar todos los dispositivos (2), Consultar mis dispositivos (3), Editar dispositivo (4), eliminar dispositivo(5), o salir (6): "
                                )
                                if accion == "1":
                                    nombre = input("Ingresar nombre de dispositivo: ")
                                    marca = input("Ingresar marca del dispositivo: ")
                                    tipo = input("Ingresar tipo de dispositivo: ")
                                    mensaje = gestion_dispositivo.agregar_dispositivo(
                                        nombre, marca, tipo, usuario_logueado.id
                                    )
                                    print(mensaje)

                                if accion == "2":
                                    gestion_dispositivo.listar_dispositivos()

                                if accion == "3":
                                    gestion_dispositivo.listar_dispositivo_por_usuario(
                                        usuario_logueado.id
                                    )

                                if accion == "4":
                                    id = int(input("Ingresar id del dispositivo: "))
                                    nombre = input("Ingresar nombre de dispositivo: ")
                                    marca = input("Ingresar marca del dispositivo: ")
                                    tipo = input("Ingresar tipo de dispositivo: ")
                                    mensaje = (
                                        gestion_dispositivo.actualizar_dispositivo(
                                            id, nombre, marca, tipo
                                        )
                                    )
                                    print(mensaje)

                                if accion == "5":
                                    id = int(input("Ingresar id del dispositivo: "))
                                    mensaje = gestion_dispositivo.eliminar_dispositivo(
                                        id
                                    )
                                    print(mensaje)
                                if accion == "6":
                                    break
                        elif accion == "2":
                            gestion_usuario.listar_usuarios()

                            id = int(
                                input(
                                    "Ingresar id del usuario para asignar su nuevo rol: "
                                )
                            )
                            nuevo_rol = input("Ingresar nuevo rol - Admin o Usuario: ")
                            mensaje = gestion_usuario.modificar_rol_usuario(
                                id, nuevo_rol
                            )
                            print(mensaje)

                        elif accion == "3":
                            time.sleep(1.5)
                            print("Cerrando Sesion...")
                            break

            else:
                print("Usuario o contraseña incorrectos.")

        elif accion == "2":
            nombre = input("Ingresar nombre de usuario: ")
            email = input("Ingresar email: ")
            telefono = input("Ingresar telefono: ")
            contraseña = input("Ingresar contraseña: ")

            mensaje = gestion_usuario.registrar_usuario(
                nombre, email, telefono, contraseña
            )
            print(mensaje)

        elif accion == "3":
            time.sleep(1.5)
            print("Saliendo del programa.")
            break


if __name__ == "__main__":
    main()
