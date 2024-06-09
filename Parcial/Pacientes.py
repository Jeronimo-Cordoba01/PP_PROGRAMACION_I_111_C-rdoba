import csv, json, random, datetime, os
from Inputs import *
from os import system

class Pacientes:
    """
    Clase Paciente. Cada instancia de esta clase representa un paciente. Y tiene los siguientes atributos:
    identificador (Iden = Entero), nombre (Nombre = String), apellido (Apellido = String), edad (Edad = Entero), altura (Altura = Entero), 
    peso (Peso = Flotante), dni (DNI = Entero), grupo_sanguineo (Grupo_sanguineo = String)
    """
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
    """
    Creo la clase Enfermero donde esta todas la funciones que el programa solicita al usuario. Llamando las validaciones de Inputs.py. 
    Luego, crea una lista vacía de Pacientes. Y lee el archivo CSV de Pacientes. Y luego genera un identificador para un nuevo paciente.
    Luego, agrega el paciente a la lista de Pacientes. Y despues cumplen el resto de las consignas 
    """
    def __init__(self):
        self.lista_pacientes = []
        self.leer_CSV("Pacientes.csv")

    def ingreso_pacientes(self):
        """
        Ingresa un nuevo paciente. Valida que los datos sean correctos llamando desde "Inputs.py" a las funciones correspondientes. 
        Luego, agrega el paciente a la lista de Pacientes. Si el paciente ya existe, imprime un mensaje de error. 
        """
        
        iden = iden_valido("Ingrese el identificador del paciente: ")
        if not iden:
            print("Identificador inválido. Operación cancelada.")
            return
        
        nombre = nombre_apellido_valido("Ingrese el nombre del paciente: ", 3, 20).capitalize()
        if not nombre:
            print("Nombre inválido. Operación cancelada.")
            return

        apellido = nombre_apellido_valido("Ingrese el apellido del paciente: ", 3, 20).capitalize()
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
        """
        Crea un nuevo Paciente con los datos ingresados. Luego, agrega el Paciente a la lista de Pacientes. 
        """
        
        self.lista_pacientes.append(paciente)
        print("Paciente ingresado correctamente.")
        
        self.escribir_JSON()
        """
        Crea un archivo JSON con la lista de Pacientes.
        """

    def generar_identificador(self) -> int:
        """
        Genera un identificador para un nuevo paciente.

        Returns:
            int: El identificador generado.
        """
        id_autoincremental = 0
        for paciente in self.lista_pacientes:
            if paciente.iden > id_autoincremental:
                id_autoincremental = paciente.iden
        return id_autoincremental + 1

    def buscar_DNI(self, dni):
        """
        Busca un paciente por su DNI.

        Args:
            dni (int): El DNI a buscar.

        Returns:
            Pacientes: El paciente encontrado o None si no se encuentra.
        """
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                return paciente
        return None
#Aca lee el CSV
    def leer_CSV(self, path: str = "Pacientes.csv") -> list:
        """
        Lee el archivo CSV de Pacientes. Intenta abrir el archivo. Si no se encuentra, imprime un mensaje de error.

        Args:
            path (str, optional): Ruta del archivo CSV. Defaults to "Pacientes.csv".

        Returns:
            list: Lista de objetos Pacientes.
        """
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
        
#1. Dar de alta. Pedira los datos necesarios y dará de alta a un nuevo paciente, asignando un ID autoincremental.
    def dar_alta(self) -> bool:
        """
        Dar de alta un nuevo paciente.

        Returns:
            bool: True si se dio de alta o False si no se dio de alta.
        """
        id_autoincremental = self.generar_identificador()
        
        dni = dni_valido("Ingrese el DNI del paciente: ")
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("El paciente ya está registrado.")
                return False
        
        alta()
        
        match input("Opción: ").strip(".", "-", " "):
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
        """
        Busca el paciente por su DNI para modificarlo.
        """

        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("Datos actuales del paciente:")
                print(paciente)
                
                if seguro():
                    print("Ingrese los nuevos datos del paciente:")
                    nombre = nombre_apellido_valido("Ingrese el nombre del paciente: ", 3, 20)
                    apellido = nombre_apellido_valido("Ingrese el apellido del paciente: ", 3, 20)
                    edad = edad_valido("Ingrese la edad del paciente: ")
                    altura = altura_valido("Ingrese la altura del paciente: ")
                    peso = peso_valido("Ingrese el peso del paciente: ")
                    grupo_sanguineo = grupo_sanguineo_valido("Ingrese el grupo sanguíneo del paciente: ")
                    
                    paciente.nombre = nombre
                    paciente.apellido = apellido
                    paciente.edad = edad
                    paciente.altura = altura
                    paciente.peso = peso
                    paciente.grupo_sanguineo = grupo_sanguineo
                    
                    print("Paciente modificado correctamente.")
                    
                    if seguro():
                        print("Modificación confirmada.")
                    else:
                        print("Modificación deshecha. Datos restaurados.")
                else:
                    print("Modificación cancelada.")
                return
            
        print("No se encontró ningún paciente con el DNI proporcionado.")
#3. Eliminar. Eliminará permanentemente a un paciente del listado original. Se pedira el DNI del paciente a eliminar.            
    def eliminar_paciente(self):
        """
        Elimina un paciente por su DNI. Sino lo encuentra, muestra un mensaje de error. Y ingresa al archivo JSON
        """
        dni = dni_valido("Ingrese el DNI del paciente a eliminar: ")
        paciente_encontrado = False
        
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                paciente_encontrado = True
                confirmacion = seguro("¿Está seguro que desea eliminar al paciente? (s/n): ")
                if confirmacion:
                    self.lista_pacientes.remove(paciente)
                    print("Paciente eliminado correctamente.")
                    self.eliminar_JSON(paciente.iden) 
                    break
                else:
                    print("Eliminación cancelada. El paciente no se ha eliminado.")
                break
        
        if not paciente_encontrado:
            print("Paciente no encontrado.")
        
#4. Mostrar todos los pacientes.                
    def mostrar_todosLos_pacientes(self):
        """
        Muestra todos los pacientes de la lista. Lleyendo el archivo CSV.
        """
        pacientes = self.leer_CSV("Pacientes.csv")
        if not pacientes:
            print("No hay pacientes para mostrar")
            return
        print("*****************************************************************************************")
        print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
        print("—------------------------------------------------------------------------------------------------")
        for paciente in pacientes:
            print(f"|{paciente.iden}| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
        print("*****************************************************************************************")
        
#5. Ordenar pacientes. Ofrecer la opción de ordenar y mostrar la lista de pacientes de forma ascendente o descendente por: 
    def Ordenar(self):
        """
        Ofrecer la opción de ordenar y mostrar la lista de pacientes de forma ascendente o descendente por
        nombre, apellido, altura, o grupo sanguíneo.
        """

        def bubble_sort(pacientes, key, ascendente=True):
            n = len(pacientes)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if ascendente:
                        if pacientes[j].__dict__[key] > pacientes[j + 1].__dict__[key]:
                            orden = pacientes[j]
                            pacientes[j] = pacientes[j + 1]
                            pacientes[j + 1] = orden
                    else:
                        if pacientes[j].__dict__[key] < pacientes[j + 1].__dict__[key]:
                            orden = pacientes[j]
                            pacientes[j] = pacientes[j + 1]
                            pacientes[j + 1] = orden

        def ordenar_por(tipo: str, ascendente: bool = True):
            match tipo:
                case "nombre" | "apellido" | "altura" | "grupo_sanguineo":
                    try:
                        bubble_sort(self.lista_pacientes, tipo, ascendente)
                        print(f"Pacientes ordenados por {tipo} de forma {'ascendente' if ascendente else 'descendente'}.")
                    except AttributeError as e:
                        print(f"Error en la ordenación: {e}")
                case _:
                    print("Opción no válida")

        def menu_ordenar():
            print("Opciones de ordenamiento:")
            print("1. Ordenar por nombre")
            print("2. Ordenar por apellido")
            print("3. Ordenar por altura")
            print("4. Ordenar por grupo sanguíneo")
            return input("Selecciona una opción de ordenamiento: ")

        orden = menu_ordenar()
        asc = input("Orden ascendente (s/n): ").strip().lower() == 's'
        desc = input("Orden descendente (s/n): ").strip().lower() == 's'

        if asc and desc:
            print("No se puede seleccionar ascendente y descendente al mismo tiempo.")
            return
        if asc:
            ascendente = True
        elif desc:
            ascendente = False
        else:
            print("Debes seleccionar ascendente o descendente.")
            return

        match orden:
            case "1":
                ordenar_por("nombre", ascendente)
            case "2":
                ordenar_por("apellido", ascendente)
            case "3":
                ordenar_por("altura", ascendente)
            case "4":
                ordenar_por("grupo_sanguineo", ascendente)
            case _:
                print("Opción no válida")
    
#6. Buscar paciente por DNI: Permitir al usuario buscar y mostrar la información de un paciente específico ingresando su DNI.
    def buscar_DNI(self, dni: int):
        """
        Busca un paciente por su DNI. Leyendo el archivo CSV. 

        Args:
            dni (int): DNI del paciente. 

        Returns:
            Pacientes: El paciente encontrado o None si no se encuentra.
        """
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("*****************************************************************************************")
                print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
                print("—------------------------------------------------------------------------------------------------")
                print(f"| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
                print("*****************************************************************************************")
                if seguro("¿Desea continuar con esta búsqueda? (s/n): "):
                    return paciente
                else:
                    print("Búsqueda cancelada.")
                    return None
        print("Paciente no encontrado.")
        return None
    
#7 calcular promedio: Mostrar un submenú que permita calcular y mostrar el promedio de:
    def promedio(self, tipo: str):
        """
        Calcula el promedio de una variable. Usando la clase Paciente. Y llenando el archivo CSV. 
        Intenta la variable. Si no se encuentra, imprime un mensaje de error.

        Args:
            tipo (str): Verifico que la variable sea la correcta. Y hace la operación correspondiente.

        Returns:
            El promedio de la variable.
        """
        self.leer_CSV("Pacientes.csv")
        if not self.lista_pacientes:
            print("No hay pacientes en la lista para calcular el promedio.")
            return None

        total = 0
        enfermos = len(self.lista_pacientes)

        try:
            match tipo:
                case "edad":
                    for paciente in self.lista_pacientes:
                        total += paciente.edad
                case "altura":
                    for paciente in self.lista_pacientes:
                        total += paciente.altura
                case "peso":
                    for paciente in self.lista_pacientes:
                        total += paciente.peso
                case _:
                    print("Criterio no válido")
                    return None

            resultado = total / enfermos
            print(f"El promedio de {tipo} es: {resultado}")

        except AttributeError as e:
            print(f"Error al acceder a los atributos de los pacientes: {e}")
            return None
        
        
#8. Salir. Terminará la ejecución del programa.
    def salir(self):
        """
        Terminará la ejecución del programa. Usando la clase Paciente. Y llenando el archivo CSV.
        """
        
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        return
        
#Guarda la lista de objetos en el CSV
    def guardar_CSV(self, path: str = "Pacientes.csv"):
        """
        Guarda la lista de objetos en el archivo CSV.

        Args:
            Usa el path para guardar el archivo CSV. Y revisa linea por linea.
        """
        ruta_absoluta = os.path.join(os.path.dirname(__file__), path)
        """
        En la "ruta_absoluta" uso el "os" para concatenar. Con el "join" para concatenar. 
        Y con el "os.path.dirname(__file__)" para que me traiga la ruta del archivo. 
        Con el "path" para que me traiga la ruta del archivo.
        """
        try:
            with open(ruta_absoluta, "w", newline='', encoding="utf8") as archivo:
                """
                El "w" es para escribir. El "newline" es para que no me genere un salto de linea. 
                El "encoding" es para que me acepte caracteres especiales.
                """
                escritor = csv.writer(archivo)
                """
                El "writer" es para escribir. El "writerow" es para escribir una sola vez.
                """
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
        """
        Escribe la lista de objetos en el archivo CSV.

        Args:
            path (str): Ruta del archivo CSV. Usando "join" para concatenar. Y direname para crear el archivo.
            paciente (Pacientes): Objeto Paciente.
        """
        ruta_absoluta = os.path.join(os.path.dirname(__file__), path)
        try:
            with open(ruta_absoluta, "a", newline='', encoding="utf8") as archivo:
                """
                El "a" es para agregar. El "newline" es para que no me genere un salto de linea. 
                El "encoding" es para que me acepte caracteres especiales.
                """
                escritor = csv.writer(archivo)
                escritor.writerow([paciente.iden, paciente.nombre, paciente.apellido, paciente.edad, paciente.altura, paciente.peso, paciente.dni, 
                                    paciente.grupo_sanguineo])
        except FileNotFoundError:
            print(f"No se encontró el archivo: {ruta_absoluta}")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")
            
#Dar de alta en JSON
    def escribir_JSON(self):
        """
        Escribe la lista de objetos en el archivo JSON.
        """
        pacientes_alta = []
        for paciente in self.lista_pacientes:
            paciente_info = {
                "ID": paciente.iden,
                "Nombre": paciente.nombre,
                "Apellido": paciente.apellido,
                "Edad": paciente.edad,
                "Altura": paciente.altura,
                "Peso": paciente.peso,
                "DNI": paciente.dni,
                "Grupo_sanguineo": paciente.grupo_sanguineo
            }
            pacientes_alta.append(paciente_info)

        with open("Alta.json", "w") as json_file:
            json.dump(pacientes_alta, json_file, indent=4)
            
        """
        El "w" es para escribir. El "json.dump" es para escribir. Y el indent=4 es para que me genere una identación.
        """
            
#Eliminar en JSON
    def eliminar_JSON(self, iden: int):
        """
        Elimina el objeto del archivo JSON.

        Args:
            iden (int): Se busca el ID para eliminar al paciente
        """
        pacientes_muertos = []
        for paciente in self.lista_pacientes:
            if paciente.iden != iden:
                paciente_info = {
                    "ID": paciente.iden,
                    "Nombre": paciente.nombre,
                    "Apellido": paciente.apellido,
                    "Edad": paciente.edad,
                    "Altura": paciente.altura,
                    "Peso": paciente.peso,
                    "DNI": paciente.dni,
                    "Grupo_sanguineo": paciente.grupo_sanguineo
                }
                pacientes_muertos.append(paciente_info)

        with open("Eliminados.json", "w") as json_file:
            json.dump(pacientes_muertos, json_file, indent=4)