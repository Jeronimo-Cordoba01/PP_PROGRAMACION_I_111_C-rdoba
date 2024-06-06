import csv, json, random, datetime
from Inputs import *
from os import system

archivo_original = "Pacientes.csv"
archivo_nuevo = "Curados.csv"#Creo que voy a borrar esto, no estoy seguro si es necesario, despues me fijo bien

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
    
    
class Enfermero: #Pongo enfermero porque no se me ocurre otro nombre
    def __init__(self):
        self.lista_pacientes = []
        
    def ingreso_pacientes(self):
        iden = iden_valido("Ingrese el identificador del paciente: ")
        nombre = nombre_valido("Ingrese el nombre del paciente: ", 3, 20)
        apellido = nombre_valido("Ingrese el apellido del paciente: ", 3, 20)
        edad = edad_valido("Ingrese la edad del paciente: ")
        altura = altura_valido("Ingrese la altura del paciente: ")
        peso = peso_valido("Ingrese el peso del paciente: ")
        dni = dni_valido("Ingrese el dni del paciente: ")        
        grupo_sanguineo = grupo_sanguineo_valido("Ingrese el grupo sanguineo del paciente: ")
        paciente = Pacientes(iden, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
        self.lista_pacientes.append(paciente)
        
#1. Dar de alta. Pedira los datos necesarios y dará de alta a un nuevo paciente, asignando un ID autoincremental.
#Esto esta mal, despues lo corrijo para que no se repita
    def dada_alta(self, dni: int) -> bool:
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                return True
        return False
#2. Modificar. Permitira alterar cualquier dato del paciente excepto su ID. Se usará el DNI para identificar al paciente a modificar.        
    def modificar_pacientes(self, nombre: str, apellido: str, edad: int, altura: int, peso: float, dni: int, grupo_sanguineo: str):
        dni = dni_valido("Ingrese el dni del paciente: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                paciente.nombre = nombre
                paciente.apellido = apellido
                paciente.edad = edad
                paciente.altura = altura
                paciente.peso = peso
                paciente.grupo_sanguineo = grupo_sanguineo
                print("Pacienteente modificado correctamente")
                return
        print("Pacienteente no encontrado")
#3. Eliminar. Eliminará permanentemente a un paciente del listado original. Se pedira el DNI del paciente a eliminar.            
    def eliminar_pacientes(self, iden: int):
        dni = dni_valido("Ingrese el dni del paciente: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                self.lista_pacientes.remove(paciente)
                print("Pacienteente eliminado correctamente")
                return
        print("Pacienteente no encontrado")
        
#4. Mostrar todos los pacientes.            
    def mostrar_todosLos_pacientes(self):
        if len(self.lista_pacientes) == 0:
            print("No hay pacientes para mostrar")
            return
        print("*****************************************************************************************")
        print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
        print("—------------------------------------------------------------------------------------------------")
        for paciente in self.lista_pacientes:
            print(f"| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
        print("—------------------------------------------------------------------------------------------------")
        
#5. Ordenar pacientes. Metodo Buuble Sort 
    def Ordenar(self):
        menu_orden = menu_ordenar()
        print(menu_orden)
        orden = input("Ordenar por: ")
        match orden:
            case "1":
                self.ordenar_por("nombre")
            case "2":
                self.ordenar_por("apellido")
            case "3":
                self.ordenar_por("altura")
            case "4":
                self.ordenar_por("grupo_sanguineo")
            case _:
                print("Opción no valida")
            
    def ordenar_por(self, tipo: str):
        match tipo:
            case "nombre":
                for i in range(len(self.lista_pacientes)):
                    for j in range(i+1, len(self.lista_pacientes)):
                        if self.lista_pacientes[i].nombre > self.lista_pacientes[j].nombre:
                            self.lista_pacientes[i], self.lista_pacientes[j] = self.lista_pacientes[j], self.lista_pacientes[i]
            case "apellido":
                for i in range(len(self.lista_pacientes)):
                    for j in range(i+1, len(self.lista_pacientes)):
                        if self.lista_pacientes[i].apellido > self.lista_pacientes[j].apellido:
                            self.lista_pacientes[i], self.lista_pacientes[j] = self.lista_pacientes[j], self.lista_pacientes[i]
            case "altura":
                for i in range(len(self.lista_pacientes)):
                    for j in range(i+1, len(self.lista_pacientes)):
                        if self.lista_pacientes[i].altura > self.lista_pacientes[j].altura:
                            self.lista_pacientes[i], self.lista_pacientes[j] = self.lista_pacientes[j], self.lista_pacientes[i]
            case "grupo_sanguineo":
                for i in range(len(self.lista_pacientes)):
                    for j in range(i+1, len(self.lista_pacientes)):
                        if self.lista_pacientes[i].grupo_sanguineo > self.lista_pacientes[j].grupo_sanguineo:
                            self.lista_pacientes[i], self.lista_pacientes[j] = self.lista_pacientes[j], self.lista_pacientes[i]
            case _:
                print("Opción no valida")
                
    
#6. Buscar paciente por DNI: Permitir al usuario buscar y mostrar la información de un paciente específico ingresando su DNI.
    def buscar_DNI(self, dni: int):
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("*****************************************************************************************")
                print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
                print("—------------------------------------------------------------------------------------------------")
                print(f"| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
                print("*****************************************************************************************")
                return paciente
        return "Pacienteente no encontrado"
    
#7 calcular promedio: Mostrar un submenú que permita calcular y mostrar el promedio de:
    def promedio(self, tipo: str):
        total = 0; enfermos = len(self.lista_pacientes)
        
        if tipo == "edad":
            for paciente in self.lista_pacientes:
                total += paciente.edad
            return total / enfermos
        elif tipo == "altura":
            for paciente in self.lista_pacientes:
                total += paciente.altura
            return total / enfermos
        elif tipo == "peso":
            for paciente in self.lista_pacientes:
                total += paciente.peso
            return total / enfermos
        else:
            print("Criterio no valido ")
            return 
        
        
#8. Salir. Terminará la ejecución del programa.
    def salir(self):
        exit()
        
#Aca lee el CSV y lo convierte en una lista de objetos
    def leer_CSV(self, path: str) -> list:
        try:
            with open(path, "r") as archivo:
                lector = csv.reader(archivo)
                next(lector)
                return [Pacientes(*paciente) for paciente in lector]
        except FileNotFoundError:
            print("No se encontro el archivo")
            return []
        