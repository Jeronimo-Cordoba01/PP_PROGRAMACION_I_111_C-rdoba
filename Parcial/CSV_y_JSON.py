import csv, json, random, datetime, os, re
from Inputs import *
from Pacientes import *
from os import system

# Función para leer el archivo CSV
def leer_CSV(path: str = "Pacientes.csv") -> list:
    lista_pacientes = []
    try:
        with open(path, 'r', encoding='utf-8') as archivo_pacientes:
            lineas = archivo_pacientes.readlines()
            encabezados = re.split(",|\n", lineas[0].strip())
            for linea in lineas[1:]:
                registro = re.split(",|\n", linea.strip())
                diccionario = {}
                for i, encabezado in enumerate(encabezados):
                    diccionario[encabezado] = registro[i]
                lista_pacientes.append(diccionario)
    except FileNotFoundError:
        print(f"No se encontró el archivo: {path}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    return lista_pacientes

# Función para guardar en el archivo CSV sin usar csv.DictWriter
def guardar_CSV(pacientes: list, archivo: str = "Pacientes.csv"):
    try:
        with open(archivo, 'w', encoding='utf-8', newline='') as archivo_pacientes:
            if pacientes:
                encabezados = list(pacientes[0].keys())
                archivo_pacientes.write(','.join(encabezados) + '\n')
                for paciente in pacientes:
                    linea = []
                    for encabezado in encabezados:
                        linea.append(str(paciente[encabezado]))
                    archivo_pacientes.write(','.join(linea) + '\n')
            print("Datos guardados correctamente en el archivo CSV.")
    except IOError:
        print(f"No se pudo guardar el archivo {archivo}.")

# Función para guardar en el archivo JSON
def escribir_JSON(pacientes: list, archivo: str = "Alta.json"):
    try:
        with open(archivo, "w", encoding="utf-8", newline='') as archivo_alta:
            json.dump(pacientes, archivo_alta, indent=4)
        print("Datos guardados correctamente en el archivo JSON.")
    except IOError:
        print("No se pudo guardar el archivo Alta.json.")

# Función para eliminar y registrar en JSON
def eliminar_JSON(pacientes: list, dni: int, archivo_eliminados: str = "Muertos.json"):
    try:
        with open(archivo_eliminados, "r", encoding='utf-8') as archivo_muertos:
            pacientes_eliminados = json.load(archivo_muertos)
    except FileNotFoundError:
        pacientes_eliminados = []

    paciente_eliminado = None
    for paciente in pacientes:
        if int(paciente["DNI"]) == dni:
            paciente_eliminado = paciente
            pacientes.remove(paciente)
            break

    if paciente_eliminado:
        pacientes_eliminados.append(paciente_eliminado)
        try:
            with open(archivo_eliminados, "w", encoding='utf-8') as archivo_muertos:
                json.dump(pacientes_eliminados, archivo_muertos, indent=4)
        except IOError:
            print("Error al guardar los datos en el archivo JSON de pacientes eliminados.")
    return pacientes
