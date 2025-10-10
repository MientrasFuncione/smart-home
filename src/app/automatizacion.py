from dispositivo import Dispositivo


class AutomatizacionBase: #Clase base (Abstracción) define la regla.
    def __init__(self, id, nombre, descripcion, estado="inactiva"):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
    
    def activar(self, dispositivos): # (polimórfismo) ejecuta la regla.
        if self.estado != "activa":
            print(f"La automatización '{self.nombre}' no está activada.")
            return
        self.ejecutar_regla(dispositivos) 

    def ejecutar_regla(self, dispositivos): # declaración de contrato
        raise NotImplementedError(f"La regla de ejecución debe ser definida en la subclase {self.__class__.__name__}.")


class EncenderTodos(AutomatizacionBase):
    def __init__(self, id, descripcion = "Enciende todos los dispositivos conectados."):
        super().__init__(id, "Encender todos los dispositivos", descripcion) #llama clase padre

    def ejecutar_regla(self, dispositivos):
        for dispositivo in dispositivos:
            dispositivo.encender_dispositivo()
        print(f"[{self.nombre}] Todos los dispositivos han sido encendidos.")


class ApagarTodos(AutomatizacionBase):
    def __init__(self, id, descripcion="Apaga todos los dispositivos conectados."):
        super().__init__(id, "Apagar todos los dispositivos", descripcion)

    def ejecutar_regla(self, dispositivos):
        for dispositivo in dispositivos:
            dispositivo.apagar_dispositivo()
        print(f"[{self.nombre}] Todos los dispositivos han sido apagados.")


class EncenderLuces(AutomatizacionBase): #sub clase
    def __init__(self, id, descripcion="Enciende solo las luces de la casa."): # se enciende solo de tipo LUZ.
        super().__init__(id, "Encender Luces", descripcion)
        self.TIPO_OBJETIVO = "Luz" # atributo para el filtro

    def ejecutar_regla(self, dispositivos):
        luces_encendidas = 0
        
        for dispositivo in dispositivos:
            # FILTRO POLIMÓRFICO: Solo si el tipo de dispositivo coincide
            #  debe coincidir con cómo se guarda en Dispositivo (ej: "Luz" vs "luz" vs "LUCES")
            if dispositivo.tipo.capitalize() == self.TIPO_OBJETIVO:
                dispositivo.encender_dispositivo()
                luces_encendidas += 1
                
        print(f"[{self.nombre}] Se encendieron {luces_encendidas} luces.")


class ApagarLuces(AutomatizacionBase): #Regla especifica Apaga la Luz
    def __init__(self, id, descripcion="Apaga solo las luces de la casa."):
        super().__init__(id, "Apagar Luces", descripcion)
        self.TIPO_OBJETIVO = "Luz" # atributo para el filtro

    def ejecutar_regla(self, dispositivos):
        luces_apagadas = 0
        
        for dispositivo in dispositivos:
            if dispositivo.tipo.capitalize() == self.TIPO_OBJETIVO:# Polimorfismo
                dispositivo.apagar_dispositivo()
                luces_apagadas += 1
                
        print(f"[{self.nombre}] Se apagaron {luces_apagadas} luces.")


# PRUEBA  AHORA ARMOS LOS el TDD
if __name__ == "__main__":
    # Creamos dispositivos de prueba
    d1 = Dispositivo(1, "Lámpara", "Philips", "Luz")
    d2 = Dispositivo(2, "Aspiradora", "LG", "Electrodoméstico")
    d3 = Dispositivo(3, "Foco", "Xiaomi", "Luz")

    dispositivos = [d1, d2, d3]

    #  automatizaciones
    auto1 = EncenderTodos(1)
    auto1.estado = "activa"
    auto1.activar(dispositivos)

    auto2 = ApagarLuces(2)
    auto2.estado = "activa"
    auto2.activar(dispositivos)