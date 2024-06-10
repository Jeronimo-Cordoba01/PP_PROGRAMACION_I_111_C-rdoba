import csv, json, random, datetime, os
from Inputs import *
from os import system

class Pacientes:
    """
    La clase Pacientes es una representación de un paciente individual y contiene varios atributos que describen su información personal y médica.
    Constructor (__init__):
    •	Parámetros:
        o	iden (int): Identificador único del paciente.
        o	nombre (str): Nombre del paciente.
        o	apellido (str): Apellido del paciente.
        o	edad (int): Edad del paciente.
        o	altura (int): Altura del paciente en centímetros.
        o	peso (float): Peso del paciente en kilogramos.
        o	dni (int): Número de documento nacional de identidad (DNI) del paciente.
        o	grupo_sanguineo (str): Grupo sanguíneo del paciente.
    •	Acciones:
        o	Inicializa los atributos del objeto Pacientes con los valores proporcionados.
    Método __str__:
    •	Descripción:
        o	Devuelve una representación en cadena del objeto Pacientes, que incluye todos sus atributos.
    •	Retorno:
        o	Una cadena que contiene el identificador, nombre, apellido, edad, altura, peso, DNI y grupo sanguíneo del paciente.

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
    La clase Enfermero contiene métodos para administrar pacientes, como ingresar nuevos pacientes, buscar pacientes por DNI, modificar información de pacientes, eliminar pacientes, mostrar información de pacientes y realizar otras operaciones relacionadas con pacientes.
    Constructor (__init__):
    •	Acciones:
        o	Inicializa la lista de pacientes vacía.
        o	Lee el archivo CSV de pacientes (Pacientes.csv) al instanciar un objeto de la clase Enfermero.
    Método ingreso_pacientes:
    •	Descripción:
        o	Permite al usuario ingresar información para un nuevo paciente.
        o	Valida la entrada de datos utilizando funciones de validación proporcionadas por el módulo Inputs.py.
        o	Agrega el nuevo paciente a la lista de pacientes si la entrada es válida.
    •	Acciones:
        o	Solicita al usuario ingresar información para un nuevo paciente, incluyendo identificador, nombre, apellido, edad, altura, peso, DNI y grupo sanguíneo.
        o	Utiliza funciones de validación del módulo Inputs.py para validar la entrada de datos.
        o	Crea un nuevo objeto Pacientes con la información ingresada.
        o	Agrega el nuevo paciente a la lista de pacientes.
        o	Imprime un mensaje indicando si el paciente fue ingresado correctamente.
        o	Llama al método escribir_JSON() para escribir la lista actualizada de pacientes en un archivo JSON.
    Otros Métodos:
    •	buscar_DNI: Busca un paciente por su DNI en la lista de pacientes.
    •	Otros métodos no incluidos en la sección de código proporcionada podrían incluir operaciones como modificar pacientes, eliminar pacientes, mostrar todos los pacientes y realizar otras operaciones relacionadas con pacientes.

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
        
        self.lista_pacientes.append(paciente)
        print("Paciente ingresado correctamente.")
        
        self.escribir_JSON()
        
        """
        Crea un archivo JSON con la lista de Pacientes.
        """

    def generar_identificador(self) -> int:
        """
        •	Descripción:
            o	Este método se encarga de generar un identificador único para un nuevo paciente.
            o	Recorre la lista de pacientes para encontrar el identificador más alto actualmente en uso.
            o	Incrementa este identificador en uno para generar un nuevo identificador único.
        •	Parámetros:
            o	No recibe parámetros explícitos, pero accede a la lista de pacientes almacenada en el objeto Enfermero.
        •	Valor de Retorno:
            o	Retorna un entero que representa el identificador generado para un nuevo paciente.
        """
        id_autoincremental = 0
        for paciente in self.lista_pacientes:
            if paciente.iden > id_autoincremental:
                id_autoincremental = paciente.iden
        return id_autoincremental + 1

    def buscar_DNI(self, dni):
        """
        •	Descripción:
            o	Este método busca un paciente en la lista de pacientes por su número de documento nacional de identidad (DNI).
            o	Recorre la lista de pacientes y compara el DNI de cada paciente con el DNI proporcionado como argumento.
        •	Parámetros:
            o	dni (int): El número de DNI que se utilizará para buscar al paciente.
        •	Valor de Retorno:
            o	Retorna el objeto Pacientes correspondiente al paciente encontrado si se encuentra un paciente con el DNI proporcionado.
            o	Retorna None si no se encuentra ningún paciente con el DNI especificado.

        """
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                return paciente
        return None
#Aca lee el CSV
    def leer_CSV(self, path: str = "Pacientes.csv") -> list:
        """
        •	Descripción:
            o	Este método se encarga de leer un archivo CSV que contiene información de pacientes.
            o	Intenta abrir el archivo especificado en la ruta proporcionada.
            o	Lee cada línea del archivo CSV, crea objetos Pacientes con los datos leídos y los agrega a una lista.
            o	Maneja errores como la falta del archivo, errores de formato CSV o errores al procesar líneas específicas.
        •	Parámetros:
            o	path (str, opcional): Ruta del archivo CSV a leer. Por defecto, el método intentará leer el archivo "Pacientes.csv".
        •	Valor de Retorno:
            o	Retorna una lista de objetos Pacientes que representan a los pacientes leídos del archivo CSV.
            o	Si el archivo no se encuentra, imprime un mensaje de error y retorna una lista vacía.
            o	Si se produce un error al leer el archivo CSV, imprime un mensaje de error específico y retorna una lista vacía.
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
        •	Descripción:
            o	Este método se encarga de dar de alta un nuevo paciente en el sistema.
            o	Primero, genera un identificador único para el nuevo paciente utilizando el método generar_identificador.
            o	Luego, solicita al usuario que ingrese el DNI del paciente.
            o	Verifica si el paciente ya está registrado en la lista de pacientes. Si el DNI ya existe, muestra un mensaje de error y devuelve False.
            o	Invoca la función alta() para solicitar los datos necesarios del paciente y agregarlo al sistema.
            o	Ofrece opciones para confirmar o cancelar el alta del paciente.
            o	Si se confirma el alta, llama al método ingreso_pacientes para agregar al paciente en la lista y devuelve True.
            o	Si se cancela el alta, muestra un mensaje y devuelve False.
            o	Si se ingresa una opción inválida, muestra un mensaje de error y devuelve False.
        •	Valor de Retorno:
            o	Retorna True si se dio de alta correctamente al paciente.
            o	Retorna False si no se pudo dar de alta al paciente, ya sea porque el DNI ya está registrado o se canceló la operación.
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
        •	Descripción:
            o	Este método permite modificar los datos de un paciente existente en el sistema, utilizando su DNI como identificador.
            o	Primero, solicita al usuario que ingrese el DNI del paciente que se desea modificar.
            o	Luego, busca al paciente en la lista de pacientes por su DNI.
            o	Si encuentra al paciente, muestra sus datos actuales y solicita confirmación para proceder con la modificación.
            o	Si se confirma la modificación, solicita los nuevos datos del paciente y los asigna al paciente correspondiente.
            o	Ofrece la opción de confirmar o deshacer la modificación.
            o	Si se cancela la modificación, muestra un mensaje indicando que la modificación ha sido cancelada.
            o	Si no se encuentra ningún paciente con el DNI proporcionado, muestra un mensaje indicando que no se encontró ningún paciente.
        •	Valor de Retorno:
            o	No tiene un valor de retorno explícito. El método interactúa con el usuario para realizar la modificación y mostrar mensajes informativos.
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
        •	Descripción:
            o	Este método permite eliminar permanentemente a un paciente del listado de pacientes.
            o	Solicita al usuario que ingrese el DNI del paciente que se desea eliminar.
            o	Busca al paciente en la lista de pacientes por su DNI.
            o	Si encuentra al paciente, solicita confirmación al usuario antes de proceder con la eliminación.
            o	Si se confirma la eliminación, elimina al paciente de la lista de pacientes.
            o	Además, solicita al usuario que confirme si desea eliminar al paciente del archivo JSON correspondiente.
            o	Si se cancela la eliminación, muestra un mensaje indicando que la eliminación ha sido cancelada.
            o	Si el paciente no es encontrado en la lista de pacientes, muestra un mensaje indicando que el paciente no ha sido encontrado.
        •	Valor de Retorno:
            o	No tiene un valor de retorno explícito. El método interactúa con el usuario para realizar la eliminación y mostrar mensajes informativos.
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
        •	Descripción:
            o	Este método muestra todos los pacientes almacenados en la lista de pacientes, leyendo los datos desde el archivo CSV.
            o	Si no hay pacientes para mostrar, imprime un mensaje indicando que no hay pacientes registrados.
            o	Si hay pacientes, imprime una tabla con la información de cada paciente, incluyendo su nombre, apellido, edad, altura, peso, DNI y grupo sanguíneo.
        •	Valor de Retorno:
            o	No tiene un valor de retorno explícito. El método interactúa con el usuario para mostrar los pacientes y mensajes informativos.

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
        •	Descripción:
            o	Este método permite al usuario ordenar y mostrar la lista de pacientes de forma ascendente o descendente según un criterio específico.
            o	Los criterios de ordenamiento disponibles son: nombre, apellido, altura y grupo sanguíneo.
            o	Utiliza el algoritmo de ordenamiento de burbuja para realizar la ordenación de la lista de pacientes.
            o	El método contiene subfunciones internas para realizar el ordenamiento y mostrar un menú de opciones al usuario.
        •	Parámetros:
            o	No recibe parámetros explícitos. Interactúa con el usuario para solicitar el tipo de ordenamiento y la dirección (ascendente o descendente).
        •	Valor de Retorno:
            o	No tiene un valor de retorno explícito. El método interactúa con el usuario para mostrar los pacientes ordenados según el criterio seleccionado.

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
        •	Descripción:
            o	Este método permite al usuario buscar y mostrar la información de un paciente específico ingresando su número de DNI.
            o	Utiliza una iteración sobre la lista de pacientes para buscar aquel cuyo DNI coincida con el proporcionado por el usuario.
            o	Si encuentra al paciente, muestra sus detalles en un formato tabular.
            o	Proporciona al usuario la opción de continuar o cancelar la búsqueda.
        •	Parámetros:
            o	dni (int): El número de DNI del paciente que se desea buscar.
        •	Valor de Retorno:
            o	Pacientes o None: Retorna el objeto del paciente encontrado si se encuentra en la lista, de lo contrario, retorna None.
        """
        for paciente in self.lista_pacientes:
            if paciente.dni == dni:
                print("*****************************************************************************************")
                print("| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |")
                print("—------------------------------------------------------------------------------------------------")
                print(f"|{paciente.iden}| {paciente.nombre} | {paciente.apellido} | {paciente.edad} | {paciente.altura} cm | {paciente.peso} kg | {paciente.dni} | {paciente.grupo_sanguineo} |")
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
        •	Descripción:
            o	Este método permite calcular y mostrar el promedio de una variable específica para todos los pacientes en la lista.
            o	Utiliza una iteración sobre la lista de pacientes y suma los valores de la variable especificada.
            o	Calcula el promedio dividiendo la suma total por el número de pacientes.
            o	Muestra el resultado del cálculo del promedio.
        •	Parámetros:
            o	tipo (str): Indica la variable para la cual se desea calcular el promedio. Puede ser "edad", "altura" o "peso".
        •	Valor de Retorno:
            o	float o None: Retorna el valor del promedio calculado si se puede calcular con éxito, de lo contrario, retorna None.

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
        •	Descripción:
            o	Este método terminará la ejecución del programa.
            o	Simplemente muestra un mensaje de despedida y finaliza la ejecución del programa.
        •	Valor de Retorno:
            o	None: No hay valor de retorno explícito, ya que este método simplemente termina la ejecución del programa.

        """
        
        print("Gracias por usar el sistema. ¡Hasta pronto!")
        return
        
#Guarda la lista de objetos en el CSV
    def guardar_CSV(self, path: str = "Pacientes.csv"):
        """
        •	Descripción:
            o	Este método guarda la lista de objetos en un archivo CSV.
            o	Recibe como argumento la ruta del archivo CSV donde se guardará la información.
            o	Utiliza la biblioteca csv de Python para escribir en el archivo CSV.
            o	Crea el archivo CSV si no existe y escribe los datos de los pacientes en él.
        •	Argumentos:
            o	path (str): Ruta del archivo CSV donde se guardará la información.
        •	Acciones:
            1.	Obtiene la ruta absoluta del archivo CSV utilizando os.path.join(os.path.dirname(__file__), path). Esto asegura que se use la ruta completa del archivo, independientemente de dónde se ejecute el programa.
            2.	Abre el archivo CSV en modo escritura ("w") con la opción newline='' para evitar que se agreguen líneas en blanco entre las filas y con la codificación "utf8".
            3.	Utiliza un objeto csv.writer para escribir en el archivo CSV.
            4.	Escribe la fila de encabezado con los nombres de las columnas.
            5.	Itera sobre la lista de pacientes y escribe cada uno de ellos en una fila del archivo CSV.
            6.	Maneja excepciones como FileNotFoundError y csv.Error en caso de que ocurran errores durante la escritura en el archivo.
        •	Valor de Retorno:
            o	No hay un valor de retorno explícito, ya que este método simplemente guarda la lista de objetos en el archivo CSV.

        """
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
        """
        •	Descripción:
            o	Este método escribe un objeto de paciente en un archivo CSV.
            o	Recibe como argumentos la ruta del archivo CSV donde se escribirá la información y el objeto de paciente que se escribirá en el archivo.
        •	Argumentos:
            o	path (str): Ruta del archivo CSV donde se escribirá la información.
            o	paciente (Pacientes): Objeto de paciente que se escribirá en el archivo CSV.
        •	Acciones:
            1.	Obtiene la ruta absoluta del archivo CSV utilizando os.path.join(os.path.dirname(__file__), path). Esto asegura que se use la ruta completa del archivo, independientemente de dónde se ejecute el programa.
            2.	Abre el archivo CSV en modo de agregado ("a") con la opción newline='' para evitar que se agreguen líneas en blanco entre las filas y con la codificación "utf8".
            3.	Utiliza un objeto csv.writer para escribir en el archivo CSV.
            4.	Escribe una nueva fila en el archivo CSV con los atributos del objeto de paciente.
            5.	Maneja excepciones como FileNotFoundError y IOError en caso de que ocurran errores durante la escritura en el archivo.
        •	Valor de Retorno:
            o	No hay un valor de retorno explícito, ya que este método simplemente escribe un objeto de paciente en el archivo CSV.
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
        •	Descripción:
            o	Este método escribe la lista de objetos de pacientes en un archivo JSON llamado "Alta.json".
        •	Acciones:
            1.	Itera sobre la lista de pacientes (self.lista_pacientes).
            2.	Para cada paciente, crea un diccionario paciente_info que contiene los atributos del paciente con sus respectivos nombres de clave.
            3.	Agrega este diccionario a la lista pacientes_alta.
            4.	Abre el archivo "Alta.json" en modo de escritura ("w").
            5.	Utiliza json.dump para escribir la lista pacientes_alta en el archivo JSON.
            6.	Utiliza indent=4 para que el JSON resultante tenga una indentación de 4 espacios, lo que lo hace más legible.
        •	Valor de Retorno:
            o	No hay un valor de retorno explícito, ya que este método simplemente escribe la lista de pacientes en un archivo JSON.
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
            
#Eliminar en JSON
    def eliminar_JSON(self, iden: int):
        """
        •	Descripción:
            o	Este método elimina un objeto del archivo JSON "Eliminados.json" basado en su identificador.
        •	Acciones:
            1.	Itera sobre la lista de pacientes (self.lista_pacientes).
            2.	Si el identificador del paciente no coincide con el identificador proporcionado, se agrega la información del paciente a la lista pacientes_muertos.
            3.	Abre el archivo "Eliminados.json" en modo de escritura ("w").
            4.	Utiliza json.dump para escribir la lista pacientes_muertos en el archivo JSON.
            5.	Utiliza indent=4 para que el JSON resultante tenga una indentación de 4 espacios, lo que lo hace más legible.
        •	Valor de Retorno:
            o	No hay un valor de retorno explícito, ya que este método simplemente elimina el objeto del archivo JSON.
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