from vehiculo import Vehiculo 
from particular import Particular
from carga import Carga
from bicicleta import Bicicleta
from motocicleta import Motocicleta
from automovil import Automovil
from registro_vehiculos import registrar_vehiculos
import csv

def main():
    # Ejercicio Parte 1 
       
    vehiculos  = registrar_vehiculos()
        
    # Ejercicio Parte 2
    print("\nEjercicio Parte 2 \n")
    
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 2)

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
    
    # Ejercicio Parte 3
    print("\nEjercicio Parte 2 \n")
    def leer_csv(nombre_archivo):
        
        particulares = []
        cargas = []
        bicicletas = []
        motocicletas = []

        with open(nombre_archivo, 'r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                if len(fila) < 2:
                    continue
            
                clase, datos = fila
                datos = eval(datos)  # Evalúa el string como un diccionario

                if clase == "<class 'particular.Particular'>":
                    particulares.append(datos)
                elif clase == "<class 'carga.Carga'>":
                    cargas.append(datos)
                elif clase == "<class 'bicicleta.Bicicleta'>":
                    bicicletas.append(datos)
                elif clase == "<class 'motocicleta.Motocicleta'>":
                    motocicletas.append(datos)
        return particulares, cargas, bicicletas, motocicletas

    nombre_archivo = "vehiculos.csv"
    
    particular.guardar_datos_csv(nombre_archivo)
    carga.guardar_datos_csv(nombre_archivo)
    bicicleta.guardar_datos_csv(nombre_archivo)
    motocicleta.guardar_datos_csv(nombre_archivo)
    
    particulares,cargas,bicicletas,motocicletas=leer_csv(nombre_archivo)
 
    print("Lista de Vehiculos Particular")
    for particular in particulares:
        print(particular)

    print("\nLista de Vehiculos Carga")
    for carga in cargas:
        print(carga)

    print("\nLista de Vehiculos Bicicleta")
    for bicicleta in bicicletas:
        print(bicicleta)

    print("\nLista de Vehiculos Motocicleta")
    for motocicleta in motocicletas:
        print(motocicleta)      
if __name__ == "__main__":
    main()
