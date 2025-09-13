class Dispositivo:
    def __init__(self, id, nombre, marca, tipo, estado="apagado"):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.estado = estado  # "encendido" o "apagado"

    def __str__(self):
        return f"Dispositivo(id={self.id}, nombre={self.nombre}, tipo={self.tipo}, estado={self.estado})"

    def encender_dispositivo(self):
        if self.estado == "encendido":
            print(f"El dispositivo {self.nombre} ya está encendido.")
        else:
            self.estado = "encendido"
            print(f"El dispositivo {self.nombre} ha sido encendido.")

    def apagar_dispositivo(self):
        if self.estado == "apagado":
            print(f"El dispositivo {self.nombre} ya está apagado.")
        else:
            self.estado = "apagado"
            print(f"El dispositivo {self.nombre} ha sido apagado.")