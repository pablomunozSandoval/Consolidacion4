from bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo_bicicleta, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo_bicicleta)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios
