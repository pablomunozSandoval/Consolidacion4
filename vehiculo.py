import ast
import csv



class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def guardar_datos_csv(self, nombre_archivo):
        with open(nombre_archivo, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"<class '{self.__class__.__module__}.{self.__class__.__name__}'>", str(self.__dict__)])
