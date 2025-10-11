from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
    @abstractmethod
    def create_device(self, dispositivo, id_usuario):
        """Crea un nuevo dispositivo y lo asocia a un usuario"""
        pass

    @abstractmethod
    def get_all(self):
        """Devuelve todos los dispositivos"""
        pass

    @abstractmethod
    def update(self, dispositivo):
        """Actualiza los datos de un dispositivo existente"""
        pass

    @abstractmethod
    def get_device_by_user(self, id_usuario):
        """Devuelve todos los dispositivos asociados a un usuario"""
        pass

    @abstractmethod
    def delete(self, id_dispositivo):
        """Elimina un dispositivo y su relación con el usuario"""
        pass
