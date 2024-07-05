import csv, json, re, os
from Inputs import *

class Paciente:
    def __init__(self, iden, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo):
        self.id = iden
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.dni = dni
        self.grupo_sanguineo = grupo_sanguineo

    def __str__(self):
        return f"{self.nombre} {self.apellido}, DNI: {self.dni}, Edad: {self.edad}, Altura: {self.altura} cm, Peso: {self.peso} kg, Grupo Sanguíneo: {self.grupo_sanguineo}"

class Doctores:
    def __init__(self):
        self.lista_pacientes = []
        self.cargar_pacientes()
        
    def ingreso_pacientes(self):
        iden = self.generar_identificador()
        
        nombre = nombre_apellido_valida("Ingrese el nombre del paciente: ", 3, 20).capitalize()
        if not nombre:
            print("Nombre inválido. Operación cancelada.")
            return

        apellido = nombre_apellido_valida("Ingrese el apellido del paciente: ", 3, 20).capitalize()
        if not apellido:
            print("Apellido inválido. Operación cancelada.")
            return

        edad = edad_valida("Ingrese la edad del paciente: ")
        if not edad:
            print("Edad inválida. Operación cancelada.")
            return

        altura = altura_valida("Ingrese la altura del paciente: ")
        if not altura:
            print("Altura inválida. Operación cancelada.")
            return
        
        peso = peso_valida("Ingrese el peso del paciente: ")
        if not peso:
            print("Peso inválido. Operación cancelada.")
            return

        dni = dni_valida("Ingrese el dni del paciente: ")
        if not dni:
            print("DNI inválido. Operación cancelada.")
            return

        grupo_sanguineo = grupo_sanguineo_valida("Ingrese el grupo sanguíneo del paciente: ")
        if not grupo_sanguineo:
            print("Grupo sanguíneo inválido. Operación cancelada.")
            return

        paciente = Doctores(iden, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
        self.lista_pacientes.append(paciente)
        self.guardar_pacientes()

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

    def cargar_pacientes(self):
        try:
            self.lista_pacientes = leer_pacientes_csv("Pacientes.csv")
        except FileNotFoundError:
            self.lista_pacientes = []
        except Exception as e:
            print(f"Error al cargar pacientes: {e}")

    def guardar_pacientes(self):
        try:
            guardar_pacientes_csv('Pacientes.csv', self.lista_pacientes)
        except Exception as e:
            print(f"Error al guardar pacientes: {e}")

#1. Dar de alta. Pedirá los datos necesarios y dará de alta a un nuevo paciente, asignando un ID único autoincremental. 
    def dar_de_alta(self):
        id_autoincremental = self.generar_identificador()
        
        dni = dni_valida("Ingrese el DNI del paciente: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("El paciente ya está registrado.")
                return False
        
        alta()
        
        opcion = input("Opción: ").strip()
        if opcion == "1":
            self.ingreso_pacientes(id_autoincremental)
            return True
        elif opcion == "2":
            print("No se realizó el alta del paciente.")
            return False
        else:
            print("Opción inválida.")
            return False

#2. Modificar. Permitirá alterar cualquier dato del paciente excepto su ID. Se usará el DNI para identificar al paciente a modificar
    def modificar(self):
        dni = dni_valida("Ingrese el DNI del paciente a modificar: ")
        paciente = self.buscar_DNI(dni)
        if paciente:
            print(f"Paciente encontrado: {paciente}")
            print("Seleccione el dato a modificar:")
            print("1. Nombre")
            print("2. Apellido")
            print("3. Edad")
            print("4. Altura")
            print("5. Peso")
            print("6. Grupo sanguíneo")
            opcion = input("Opción: ").strip()

            if opcion == "1":
                paciente.nombre = nombre_apellido_valida("Ingrese el nuevo nombre: ")
            elif opcion == "2":
                paciente.apellido = nombre_apellido_valida("Ingrese el nuevo apellido: ")
            elif opcion == "3":
                paciente.edad = edad_valida("Ingrese la nueva edad: ")
            elif opcion == "4":
                paciente.altura = altura_valida("Ingrese la nueva altura en cm: ")
            elif opcion == "5":
                paciente.peso = peso_valida("Ingrese el nuevo peso en kg: ")
            elif opcion == "6":
                paciente.grupo_sanguineo = grupo_sanguineo_valida("Ingrese el nuevo grupo sanguíneo: ")
            else:
                print("Opción inválida.")
                return

            self.guardar_pacientes()
            print("Datos del paciente actualizados.")
            return
    print("Paciente no encontrado.")

#3. Eliminar. Eliminará permanentemente a un paciente del listado original. Se pedirá el DNI del paciente a eliminar.
    def eliminar(self):
        dni = dni_valida("Ingrese el DNI del paciente a eliminar: ")
        paciente = self.buscar_DNI(dni)
        if paciente:
            self.lista_pacientes.remove(paciente)
            self.guardar_pacientes()
            print("Paciente eliminado.")
            return
        print("Paciente no encontrado.")

#4. Mostrar todos. Imprimirá por consola la información de todos los pacientes
    def mostrar_todos(self):
        print("*****************************************************************************************")
        print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
        print("—------------------------------------------------------------------------------------------------")
        for paciente in self.lista_pacientes:
            print(f"| {paciente['nombre']} | {paciente['apellido']} | {paciente['edad']} | {paciente['altura']} cm | {paciente['peso']} kg | {paciente['dni']} | {paciente['grupo_sanguineo']} |")
        print("*****************************************************************************************")

#5. Ordenar pacientes. Ofrecer la opción de ordenar y mostrar la lista de pacientes de forma ascendente o descendente por:
    def bubble_sort(self, lista_pacientes:list[Paciente], campo:str, ascendente: bool = True):
        for i in range(0, len(lista_pacientes)-1):
            for j in range(i+1, len(lista_pacientes)):
                
                    if campo == "nombre":
                        a, b = lista_pacientes[i].nombre , lista_pacientes[j].nombre
                    elif campo == "apellido":
                        a, b = lista_pacientes[i].apellido , lista_pacientes[j].apellido
                    elif campo == "altura":
                        a, b = lista_pacientes[i].altura , lista_pacientes[j].altura
                    elif campo == "grupo_sanguineo":
                        a, b = lista_pacientes[i].grupo_sanguineo , lista_pacientes[j].grupo_sanguineo
                    if ascendente:
                        if a < b:
                            lista_pacientes[i], lista_pacientes[j] = lista_pacientes[j],lista_pacientes[i]
                    else:
                        if a > b:
                            lista_pacientes[i], lista_pacientes[j] = lista_pacientes[j], lista_pacientes[i]
                            
    def ordenar_pacientes(self):
        if not self.lista_pacientes:
            print("No hay pacientes registrados.")
            return

        print("Seleccione el criterio de ordenamiento:")
        print("1. Nombre")
        print("2. Apellido")
        print("3. Altura")
        print("4. Grupo sanguíneo")
        opcion = input("Opción: ").strip()

        match opcion:
            case "1":
                campo = "nombre"
            case "2":
                campo = "apellido"
            case "3":
                campo = "altura"
            case "4":
                campo = "grupo_sanguineo"
            case _:
                print("Opción inválida.")
                return

        orden = menu_ordenar_tipo()
        if orden == "1":
            self.bubble_sort(self.lista_pacientes, campo, ascendente=True)
        elif orden == "2":
            self.bubble_sort(self.lista_pacientes, campo, ascendente=False)
        else:
            print("Opción de orden inválida.")
            return

        self.guardar_pacientes()
        self.mostrar_todos()

#6. Buscar paciente por DNI: Permitir al usuario buscar y mostrar la información de un paciente específico ingresando su DNI.
    def buscar_paciente_por_dni(self):
        dni = dni_valida("Ingrese el DNI del paciente a buscar: ")
        paciente = self.buscar_DNI(dni)
        if paciente:
            print(paciente)
        else:
            print("Paciente no encontrado.")

#7. Calcular promedio:
    def calcular_promedio(self):
        if not self.lista_pacientes:
            print("No hay pacientes registrados.")
            return

        print("Seleccione el promedio a calcular:")
        print("1. Edad")
        print("2. Altura")
        print("3. Peso")
        opcion = input("Opción: ").strip()

        total = 0

        match opcion:
            case "1":
                for paciente in self.lista_pacientes:
                    total += paciente.edad
                promedio = total / len(self.lista_pacientes)
                print(f"El promedio de edad es: {promedio:.2f} años")
            case "2":
                for paciente in self.lista_pacientes:
                    total += paciente.altura
                promedio = total / len(self.lista_pacientes)
                print(f"El promedio de altura es: {promedio:.2f} cm")
            case "3":
                for paciente in self.lista_pacientes:
                    total += paciente.peso
                promedio = total / len(self.lista_pacientes)
                print(f"El promedio de peso es: {promedio:.2f} kg")
            case _:
                print("Opción inválida.")

#8. Determinar compatibilidad:
    def determinar_compatibilidad(self):
        dni = dni_valida("Ingrese el DNI del paciente: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                compatibilidad = {
                    "A+": {"Donar": ["A+", "AB+"], "Recibir": ["O+", "O-", "A+", "A-"]},
                    "A-": {"Donar": ["A+", "A-", "AB+", "AB-"], "Recibir": ["A-", "O-"]},
                    "B+": {"Donar": ["B+", "AB+"], "Recibir": ["O+", "O-", "B+", "B-"]},
                    "B-": {"Donar": ["B+", "B-", "AB+", "AB-"], "Recibir": ["B-", "O-"]},
                    "AB+": {"Donar": ["AB+"], "Recibir": ["TODOS"]},
                    "AB-": {"Donar": ["AB+", "AB-"], "Recibir": ["AB-", "O-", "A-", "B-"]},
                    "O+": {"Donar": ["A+", "B+", "AB+", "O+"], "Recibir": ["O+", "O-"]},
                    "O-": {"Donar": ["TODOS"], "Recibir": ["O-"]}
                }
                grupo_sanguineo = paciente.grupo_sanguineo
                if grupo_sanguineo in compatibilidad:
                    puede_donar = compatibilidad[grupo_sanguineo]["Donar"]
                    puede_recibir = compatibilidad[grupo_sanguineo]["Recibir"]

                    print(f"El paciente {paciente} puede donar a: {', '.join(puede_donar)}")
                    print(f"El paciente {paciente} puede recibir de: {', '.join(puede_recibir)}")

                    posibles_donantes = []
                    for donante in self.lista_pacientes:
                        if donante.grupo_sanguineo in puede_recibir:
                            posibles_donantes.append(donante)

                    if posibles_donantes:
                        print("Posibles donantes:")
                        for donante in posibles_donantes[:3]:
                            print(donante)
                    else:
                        print("No hay donantes compatibles.")
                else:
                    print("Grupo sanguíneo no reconocido.")
                return
        print("Paciente no encontrado.")

#9. Salir. Terminar la ejecución del programa.
    def salir(self):
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        self.guardar_pacientes()
        return
#########################################################################################################################################################
#CSV Y JSON
def leer_pacientes_csv(self, path):
        ruta_archivo = r'Parcial\Pacientes.csv'
        pacientes = []
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                next(file)  
                for lineas in file:
                    data = lineas.strip().split(',')
                    print(f"Línea leída: {data}") 
                    if len(data) == 8:  
                        paciente = {
                            "id": int(data[0]),
                            "nombre": data[1],
                            "apellido": data[2],
                            "edad": int(data[3]),
                            "altura": int(data[4]),
                            "peso": float(data[5]),
                            "dni": data[6],
                            "grupo_sanguineo": data[7]
                        }
                        pacientes.append(paciente)
                        print(f"Paciente cargado: {paciente}")  
                    else:
                        print(f"Formato incorrecto en la línea: {lineas}")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")
        self.lista_pacientes = pacientes

def guardar_pacientes_csv(path, pacientes):
    ruta_archivo = r'Parcial\Pacientes.csv'
    try:
        with open(path, 'w', encoding='utf-8') as file:
            for paciente in pacientes:
                lineas = f'{paciente["id"]},{paciente["nombre"]},{paciente["apellido"]},{paciente["edad"]},{paciente["altura"]},{paciente["peso"]},{paciente["dni"]},{paciente["grupo_sanguineo"]}\n'
                file.write(lineas)
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")

def leer_pacientes_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []

def altas_pacientes(path, pacientes):
    ruta = r'Parcial\Alta.json'
    try:
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(pacientes, file, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")
