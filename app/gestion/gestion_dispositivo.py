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
        if not dispositivos:
            print("El usuario no tiene registrado ningún dispositivo.")
            return
        for dispositivo in dispositivos:
            print(dispositivo)

    def listar_dispositivo_por_usuario(self, id_usuario):
        dispositivos = self.dispositivo_dao.get_device_by_user(id_usuario)
        for dispositivo in dispositivos:
            print(dispositivo)

    def actualizar_dispositivo(self, id, nombre, marca, tipo):
        if not id or not nombre or not marca or not tipo:
            return "El nombre, la marca y el tipo son obligatorios."

        nuevo_dispositivo = Dispositivo(id, nombre, marca, tipo)
        self.dispositivo_dao.update(nuevo_dispositivo)
        return "Dispositivo editado exitosamente."

    def eliminar_dispositivo(self, id_dispositivo):
        if not id_dispositivo:
            return "El id es obligatorio para eliminar el dispositivo"
        self.dispositivo_dao.delete(id_dispositivo)
        return "Dispositivo eliminado exitosamente."
