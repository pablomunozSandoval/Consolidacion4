# registro_vehiculos.py

from automovil import Automovil  # Asegúrate de importar la clase adecuada

def registrar_vehiculos():
    vehiculos = []

    for i in range(1, 4):
        print(f"\nDatos del automóvil {i}")
        try:
            marca = input("Inserte la marca del automóvil: ")
            modelo = input("Inserte el modelo: ")
            nro_ruedas = int(input("Inserte el número de ruedas: "))
            velocidad = int(input("Inserte la velocidad en km/h: "))
            cilindrada = int(input("Inserte el cilindraje en cc: "))

            automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
            vehiculos.append(automovil)
        except ValueError:
            print("Error: Por favor, ingrese un valor numérico válido para el número de ruedas, velocidad, y cilindraje.")
            return

    for i, auto in enumerate(vehiculos, start=1):
        print(f"Datos del automóvil {i} : Marca {auto.marca}, Modelo {auto.modelo}, {auto.nro_ruedas} ruedas, {auto.velocidad} Km/h, {auto.cilindraje} cc")

    return vehiculos
