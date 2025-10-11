from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
    @abstractmethod
    def create_device(self, dispositivo, id_usuario):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, dispositivo):
        pass

    @abstractmethod
    def get_device_by_user(self, id_usuario):
        pass

    @abstractmethod
    def delete(self, id_dispositivo):
        pass
