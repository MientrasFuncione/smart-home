from app.dispositivo import Dispositivo


class DispositivoService:
    def __init__(self):
        self.dispositivos = []
        self.id_contar = 1

    def nuevo_dispositivo(self, id, nombre, marca, tipo):
        nuevo_dispositivo = Dispositivo(
            id, nombre.capitalize(), marca.capitalize(), tipo.capitalize()
        )
        return nuevo_dispositivo

    def agregar_dispositivo(self, nombre, marca, tipo):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre.lower() == nombre.lower():
                print("El dispositivo ingresado ya está registrado.")
                return

        id_dispositivo = str(self.id_contar)
        self.id_contar += 1

        nuevo_dispositivo = self.nuevo_dispositivo(id_dispositivo, nombre, marca, tipo)

        self.dispositivos.append(nuevo_dispositivo)
        print(f"Dispositivo {nombre} agregado exitosamente.")

    def listar_dispositivos(self):
        if not self.dispositivos:
            print("No hay dispositivos agregados.")
            return

        for dispositivo in self.dispositivos:
            print(
                f"Dispositivo ID: {dispositivo.id}, Nombre: {dispositivo.nombre}, Marca: {dispositivo.marca}, Tipo: {dispositivo.tipo}, Estado: {dispositivo.estado}"
            )

    def buscar_dispositivo(self, nombre):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre.lower() == nombre.lower():
                print(
                    f"Dispositivo ID: {dispositivo.id}, Nombre: {dispositivo.nombre}, Marca: {dispositivo.marca}, Tipo: {dispositivo.tipo}, Estado: {dispositivo.estado}"
                )
                return
        print("El dispositivo no fue encontrado.")

    def eliminar_dispositivo(self, nombre):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre.lower() == nombre.lower():
                self.dispositivos.remove(dispositivo)
                print("El dispositivo fue eliminado exitosamente.")
                return
        print("El dispositivo no fue encontrado.")

    def encender_dispositivo(self, nombre):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre.lower() == nombre.lower():
                dispositivo.encender_dispositivo()
                return
        print("El dispositivo no fue encontrado.")

    def apagar_dispositivo(self, nombre):
        for dispositivo in self.dispositivos:
            if dispositivo.nombre.lower() == nombre.lower():
                dispositivo.apagar_dispositivo()
                return
        print("El dispositivo no fue encontrado.")


if __name__ == "__main__":
    servicio = DispositivoService()
    servicio.agregar_dispositivo("Aspiradora", "Samsung", "Limpieza")
    servicio.agregar_dispositivo("Televisor", "LG", "Entretenimiento")
    servicio.listar_dispositivos()

    servicio.encender_dispositivo("Aspiradora")
    servicio.encender_dispositivo("Televisor")
    servicio.listar_dispositivos()

    servicio.apagar_dispositivo("Aspiradora")
    servicio.listar_dispositivos()

