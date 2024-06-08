import csv, json, random, datetime, os
from Inputs import *
from os import system

class Pacientes:
    def __init__(self, iden: int, nombre: str, apellido: str, edad: int, altura: int, peso: float, dni: int, grupo_sanguineo: str):
        self.iden = iden
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.dni = dni
        self.grupo_sanguineo = grupo_sanguineo
        
    def __str__(self):
        return f"{self.iden} {self.nombre} {self.apellido} {self.edad} {self.altura} {self.peso} {self.dni} {self.grupo_sanguineo}"
    
    
class Enfermero:
    def __init__(self):
        self.lista_pacientes = []

    def ingreso_pacientes(self):
        
        iden = iden_valido("Ingrese el identificador del paciente: ")
        if not iden:
            print("Identificador inválido. Operación cancelada.")
            return
        
        nombre = nombre_apellido_valido("Ingrese el nombre del paciente: ", 3, 20)
        if not nombre:
            print("Nombre inválido. Operación cancelada.")
            return

        apellido = nombre_apellido_valido("Ingrese el apellido del paciente: ", 3, 20)
        if not apellido:
            print("Apellido inválido. Operación cancelada.")
            return

        edad = edad_valido("Ingrese la edad del paciente: ")
        if not edad:
            print("Edad inválida. Operación cancelada.")
            return

        altura = altura_valido("Ingrese la altura del paciente: ")
        if not altura:
            print("Altura inválida. Operación cancelada.")
            return

        peso = peso_valido("Ingrese el peso del paciente: ")
        if not peso:
            print("Peso inválido. Operación cancelada.")
            return

        dni = dni_valido("Ingrese el dni del paciente: ")
        if not dni:
            print("DNI inválido. Operación cancelada.")
            return
        if self.buscar_DNI(dni):
            print("El DNI ya está registrado. Operación cancelada.")
            return

        grupo_sanguineo = grupo_sanguineo_valido("Ingrese el grupo sanguíneo del paciente: ")
        if not grupo_sanguineo:
            print("Grupo sanguíneo inválido. Operación cancelada.")
            return

        paciente = Pacientes(iden, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
        self.lista_pacientes.append(paciente)
        print("Paciente ingresado correctamente.")

    def generar_identificador(self) -> int:
        id_autoincremental = 0
        for paciente in self.lista_pacientes:
            if paciente.iden > id_autoincremental:
                id_autoincremental = paciente.iden
        return id_autoincremental + 1

    def buscar_DNI(self, dni):
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                return paciente
        return None
        
#1. Dar de alta. Pedira los datos necesarios y dará de alta a un nuevo paciente, asignando un ID autoincremental.
    def dar_alta(self) -> bool:
        id_autoincremental = self.generar_identificador()
        
        dni = dni_valido("Ingrese el DNI del paciente: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("El paciente ya está registrado.")
                return False
        
        alta()
        
        match input("Opción: ").strip():
            case "1":
                self.ingreso_pacientes(id_autoincremental)
                return True
            case "2":
                print("No se realizó el alta del paciente.")
                return False
            case _:
                print("Opción inválida.")
                return False
#2. Modificar. Permitira alterar cualquier dato del paciente excepto su ID. Se usará el DNI para identificar al paciente a modificar
    def modificar_paciente(self):
        dni = dni_valido("Ingrese el DNI del paciente a modificar: ")

        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("Datos actuales del paciente:")
                print(paciente)
                
                if seguro():
                    datos_anteriores = paciente.__dict__.copy()
                    self.ingreso_pacientes()
                    print("Paciente modificado correctamente.")
                    
                    if seguro():
                        paciente.__dict__ = datos_anteriores
                        print("Modificación deshecha. Datos restaurados.")
                    else:
                        print("Modificación confirmada.")
                else:
                    print("Modificación cancelada.")
                return
        
        print("No se encontró ningún paciente con el DNI proporcionado.")
#3. Eliminar. Eliminará permanentemente a un paciente del listado original. Se pedira el DNI del paciente a eliminar.            
    def eliminar_paciente(self):
        dni = dni_valido("Ingrese el DNI del paciente a eliminar: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                paciente_temporal = paciente

                self.lista_pacientes.remove(paciente)
                print("Paciente eliminado correctamente.")
                
                if seguro():
                    print("Paciente eliminado correctamente.")
                    return
                else:
                    self.lista_pacientes.append(paciente_temporal)
                    print("Eliminación cancelada. El paciente ha sido restaurado.")
                    return
        print("Paciente no encontrado.")
        
#4. Mostrar todos los pacientes.            
#Aca lee el CSV
    def leer_CSV(self, path: str = "Pacientes.csv") -> list:
        ruta_absoluta = os.path.join(os.path.dirname(__file__), path)
        lista_pacientes = []
        try:
            with open(ruta_absoluta, "r", encoding="utf8") as archivo:
                lector = csv.reader(archivo)
                next(lector)
                for campos in lector:
                    try:
                        paciente = Pacientes(
                            iden=int(campos[0]),
                            nombre=campos[1],
                            apellido=campos[2],
                            edad=int(campos[3]),
                            altura=int(campos[4]),
                            peso=float(campos[5]),
                            dni=int(campos[6]),
                            grupo_sanguineo=campos[7]
                        )
                        lista_pacientes.append(paciente)
                    except (IndexError, ValueError) as e:
                        print(f"Error al procesar la línea {lector.line_num}: {e}")
        except FileNotFoundError:
            print(f"No se encontró el archivo: {ruta_absoluta}")
        except csv.Error as e:
            print(f"Error al leer el archivo CSV: {e}")
        return lista_pacientes
    
    def mostrar_todosLos_pacientes(self):
        pacientes = self.leer_CSV("Pacientes.csv")
        if not pacientes:
            print("No hay pacientes para mostrar")
            return
        print("*****************************************************************************************")
        print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
        print("—------------------------------------------------------------------------------------------------")
        for paciente in pacientes:
            print(f"| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
        print("*****************************************************************************************")
        
#5. Ordenar pacientes. Ofrecer la opción de ordenar y mostrar la lista de pacientes de forma ascendente o descendente por: 
    def Ordenar(self):
        def bubble_sort(arr, key, ascendente=True):
            n = len(arr)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if ascendente:
                        if arr[j].__dict__[key] > arr[j + 1].__dict__[key]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    else:
                        if arr[j].__dict__[key] < arr[j + 1].__dict__[key]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]

        def ordenar_por(tipo: str, ascendente: bool = True):
            match tipo:
                case "nombre", "apellido", "altura", "grupo_sanguineo":
                    try:
                        bubble_sort(self.lista_pacientes, tipo, ascendente)
                    except AttributeError as e:
                        print(f"Error en la ordenación: {e}")
                case _:
                    print("Opción no válida")

        orden = menu_ordenar()
        asc = input("Orden ascendente (s/n): ").strip().capitalize() == 'S'
        des = input("Orden descendente (s/n): ").strip().capitalize() == 'S'
        if asc and des:
            print("No se puede seleccionar ascendente y descendente al mismo tiempo.")
            return
        if asc:
            ascendente = True
            descendente = False
        elif des:
            ascendente = False
            descendente = True
        else:
            print("Debes seleccionar ascendente o descendente.")
            return

        match orden:
            case "1":
                ordenar_por("nombre", ascendente=ascendente)
            case "2":
                ordenar_por("apellido", ascendente=ascendente)
            case "3":
                ordenar_por("altura", ascendente=ascendente)
            case "4":
                ordenar_por("grupo_sanguineo", ascendente=ascendente)
            case _:
                print("Opción no válida")
                
    
#6. Buscar paciente por DNI: Permitir al usuario buscar y mostrar la información de un paciente específico ingresando su DNI.
    def buscar_DNI(self, dni: int):
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("*****************************************************************************************")
                print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
                print("—------------------------------------------------------------------------------------------------")
                print(f"| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
                print("*****************************************************************************************")
                if seguro():
                    return paciente
                else:
                    print("Búsqueda cancelada.")
                    return None
        print("Paciente no encontrado.")
        return None
    
#7 calcular promedio: Mostrar un submenú que permita calcular y mostrar el promedio de:
    def promedio(self, tipo: str):
        if not self.lista_pacientes:
            print("No hay pacientes en la lista para calcular el promedio.")
            return None

        total = 0
        enfermos = len(self.lista_pacientes)

        try:
            if tipo == "edad":
                for paciente in self.lista_pacientes:
                    total += paciente.edad
            elif tipo == "altura":
                for paciente in self.lista_pacientes:
                    total += paciente.altura
            elif tipo == "peso":
                for paciente in self.lista_pacientes:
                    total += paciente.peso
            else:
                print("Criterio no válido")
                return None

            return total / enfermos
        except AttributeError as e:
            print(f"Error al acceder a los atributos de los pacientes: {e}")
            return None
        
        
#8. Salir. Terminará la ejecución del programa.
    def salir(self):
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        return
        
#Guarda la lista de objetos en el CSV
    def guardar_CSV(self, path: str = "Pacientes.csv"):
        ruta_absoluta = os.path.join(os.path.dirname(__file__), path)
        try:
            with open(ruta_absoluta, "w", newline='', encoding="utf8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["ID", "Nombre", "Apellido", "Edad", "Altura", "Peso", "DNI", "Grupo_sanguineo"])
                for paciente in self.lista_pacientes:
                    escritor.writerow([
                        paciente.id, paciente.nombre, paciente.apellido,
                        paciente.edad, paciente.altura, paciente.peso,
                        paciente.dni, paciente.grupo_sanguineo])
        except FileNotFoundError:
            print(f"No se encontró el archivo: {ruta_absoluta}")
        except csv.Error as e:
            print(f"Error al escribir en el archivo: {e}")
                
#Escribe la lista de objetos en el CSV
    def escribir_CSV(self, path: str, paciente: Pacientes):
        ruta_absoluta = os.path.join(os.path.dirname(__file__), path)
        try:
            with open(ruta_absoluta, "a", newline='', encoding="utf8") as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([paciente.iden, paciente.nombre, paciente.apellido, paciente.edad, paciente.altura, paciente.peso, paciente.dni, 
                                    paciente.grupo_sanguineo])
        except FileNotFoundError:
            print(f"No se encontró el archivo: {ruta_absoluta}")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")