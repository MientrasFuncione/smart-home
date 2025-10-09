from app.dominio.dispositivo import Dispositivo


class GestionDispositivo:
    def __init__(self, dispositivo_dao):
        self.dispositivo_dao = dispositivo_dao

    def agregar_dispositivo(self, nombre, marca, tipo, id_usuario):
        if not nombre or not marca or not tipo:
            return "El nombre, la marca y el tipo son obligatorios."
        nuevo_dispositivo = Dispositivo(id, nombre, marca, tipo)
        self.dispositivo_dao.create_device(nuevo_dispositivo, id_usuario)
        return "Dispositivo agregado exitosamente."

    def listar_dispositivos(self):
        dispositivos = self.dispositivo_dao.get_all()
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
