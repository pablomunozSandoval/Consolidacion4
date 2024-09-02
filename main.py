from vehiculo import Vehiculo 
from particular import Particular
from carga import Carga
from bicicleta import Bicicleta
from motocicleta import Motocicleta
from automovil import Automovil
import csv

def main():

    
    #Ejercicio Parte 1 
    vehiculos  = []
    
    for i in range(1,3 + 1):
        print(f"\nDatos del automóvil {i}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))

        automovil = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(automovil)
        
    for i, auto in enumerate(vehiculos, start=1):
        print(f"Datos del automóvil {i} : Marca {auto.marca}, Modelo {auto.modelo}, {auto.nro_ruedas} ruedas, {auto.velocidad} Km/h, {auto.cilindrada} cc")
       
       
       #Ejercicio Parte 2
        
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    print(f"Marca {particular.marca}, Modelo {particular.modelo}, {particular.nro_ruedas} ruedas {particular.velocidad} Km/h, {particular.cilindrada} cc Puestos: {particular.nro_puestos}")
    print(f"Marca {carga.marca}, Modelo {carga.modelo}, {carga.nro_ruedas} ruedas {carga.velocidad} Km/h, {carga.cilindrada} cc Carga: {carga.carga_kg} Kg")
    print(f"Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.nro_ruedas} ruedas Tipo: {bicicleta.tipo_bicicleta}")
    print(f"Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.nro_ruedas} ruedas Tipo: {motocicleta.tipo_bicicleta} Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}")

    print("Motocicleta es instancia con relación a Vehículo:", isinstance(motocicleta, Vehiculo))
    print("Motocicleta es instancia con relación a Automovil:", isinstance(motocicleta, Automovil))
    print("Motocicleta es instancia con relación a Vehículo particular:", isinstance(motocicleta, Particular))
    print("Motocicleta es instancia con relación a Vehículo de Carga:", isinstance(motocicleta, Carga))
    print("Motocicleta es instancia con relación a Bicicleta:", isinstance(motocicleta, Bicicleta))
    print("Motocicleta es instancia con relación a Motocicleta:", isinstance(motocicleta, Motocicleta))
    
    #Ejercicio Parte 3
    def guardar_datos_csv(self, nombre_archivo):
        
        try:
            with open(nombre_archivo, "a", newline="") as archivo:
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerow([self.__class__, self.__dict__])
            print(f"Datos de {self.__class__.__name__} guardados en {nombre_archivo}")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
    def leer_datos_csv(nombre_archivo):
        try:
            with open(nombre_archivo, "r") as archivo:
                archivo_csv = csv.reader(archivo)
                vehiculos = {
                    "Particular": [],
                    "Carga": [],
                    "Bicicleta": [],
                    "Motocicleta": []
                }

                for fila in archivo_csv:
                    clase, atributos = eval(fila[0]), eval(fila[1])
                    if clase.__name__ == "Particular":
                        vehiculos["Particular"].append(atributos)
                    elif clase.__name__ == "Carga":
                        vehiculos["Carga"].append(atributos)
                    elif clase.__name__ == "Bicicleta":
                        vehiculos["Bicicleta"].append(atributos)
                    elif clase.__name__ == "Motocicleta":
                        vehiculos["Motocicleta"].append(atributos)
        
            for tipo, lista in vehiculos.items():
                print(f"Lista de Vehículos {tipo}")
                for vehiculo in lista:
                    print(vehiculo)
                print()

        except FileNotFoundError:
            print(f"Error: El archivo {nombre_archivo} no existe.")
        except Exception as e:
            print(f"Error al leer los datos: {e}")

    #Ejecucion Ejercicio Parte 3
    nombre_archivo = "vehiculos.csv"
    
    particular.guardar_datos_csv(nombre_archivo)
    carga.guardar_datos_csv(nombre_archivo)
    bicicleta.guardar_datos_csv(nombre_archivo)
    motocicleta.guardar_datos_csv(nombre_archivo)
    
    leer_datos_csv(nombre_archivo)

    
    
if __name__ == "__main__":
    main()
