from app.dominio.dispositivo import Dispositivo


class GestionDispositivo:
    def __init__(self, dao):
        self.dao = dao

    def agregar_dispositivo(self, nombre, marca, tipo):
        pass

    def listar_dispositivos_por_usuario(self, usuario_id):
        dispositivos = self.dao.get_device_by_user(usuario_id)
        for dispositivo in dispositivos:
            print(dispositivo)

    def buscar_dispositivo(self, nombre):
        pass

    def eliminar_dispositivo(self, nombre):
        pass

    def encender_dispositivo(self, nombre):
        pass

    def apagar_dispositivo(self, nombre):
        pass
