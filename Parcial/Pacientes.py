import csv, json, re, os
from Inputs import *

class Paciente:
    def __init__(self, id, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo):
        self.id = id
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
        id = len(self.lista_pacientes) + 1
        prompts = [
            ("Ingrese el nombre: ", nombre_apellido_valida),
            ("Ingrese el apellido: ", nombre_apellido_valida),
            ("Ingrese la edad: ", edad_valida),
            ("Ingrese la altura en cm: ", altura_valida),
            ("Ingrese el peso en kg: ", peso_valida),
            ("Ingrese el DNI: ", dni_valida),
            ("Ingrese el grupo sanguíneo: ", grupo_sanguineo_valida)
        ]

        datos = []
        for prompt, funcion in prompts:
            dato = funcion(prompt)
            if dato is None:
                print("Error al ingresar los datos del paciente. Por favor, intente nuevamente.")
                return
            datos.append(dato)

        nombre, apellido, edad, altura, peso, dni, grupo_sanguineo = datos
        paciente = Paciente(id, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
        self.lista_pacientes.append(paciente)
        self.guardar_pacientes()
        print("Paciente dado de alta exitosamente.")

#2. Modificar. Permitirá alterar cualquier dato del paciente excepto su ID. Se usará el DNI para identificar al paciente a modificar
    def modificar(self):
        dni = dni_valida("Ingrese el DNI del paciente a modificar: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
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
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                self.lista_pacientes.remove(paciente)
                self.guardar_pacientes()
                print("Paciente eliminado.")
                return

        print("Paciente no encontrado.")

#4. Mostrar todos. Imprimirá por consola la información de todos los pacientes
    def mostrar_todos(self):
        if not self.lista_pacientes:
            print("No hay pacientes registrados.")
            return

        print("*****************************************************************************************")
        print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
        print("—------------------------------------------------------------------------------------------------")
        for paciente in self.lista_pacientes:
            print(f"| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
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
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print(paciente)
                return

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
def leer_pacientes_csv(file_path):
    pacientes = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
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
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return pacientes

def guardar_pacientes_csv(file_path, pacientes):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for paciente in pacientes:
                line = f'{paciente["id"]},{paciente["nombre"]},{paciente["apellido"]},{paciente["edad"]},{paciente["altura"]},{paciente["peso"]},{paciente["dni"]},{paciente["grupo_sanguineo"]}\n'
                file.write(line)
    except Exception as e:
        print(f"Error al guardar el archivo CSV: {e}")

def leer_pacientes_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error al leer el archivo JSON: {e}")
        return []

def guardar_pacientes_json(file_path, pacientes):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(pacientes, file, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")
