from automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga_kg):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga_kg = carga_kg
