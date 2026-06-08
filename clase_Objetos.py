class Planta: # Clase que representa una planta

    # Constructor: aquí se guardan las características de la planta
    def __init__(self, nombre, tipo, altura=0):
        self.nombre = nombre
        self.tipo = tipo
        self.altura = altura

    # Este método hace que la planta crezca 5 cm
    def crecer(self):
        self.altura += 5

    # Este método muestra la información de la planta
    def mostrar_informacion(self):
        print(f"Planta: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Altura actual: {self.altura} cm")


# Creación del primer objeto
planta1 = Planta("Rosa", "Flor")

# Creación del segundo objeto
planta2 = Planta("Cactus", "Suculenta")


# Mostrar el estado inicial de la primera planta
planta1.mostrar_informacion()

# La planta crece 5 cm
planta1.crecer()

# Mostrar el nuevo estado de la planta
planta1.mostrar_informacion()

print("----------------")

# Mostrar el estado inicial de la segunda planta
planta2.mostrar_informacion()

# La planta crece 5 cm
planta2.crecer()

# Mostrar el nuevo estado de la planta
planta2.mostrar_informacion()