"""
nombre: Jerónimo 
apellido: Córdoba
---
1° Parcial
---
Enunciado:
Se necesita realizar un programa para la administración de pacientes en una clínica privada que
permita interactuar únicamente a través de la consola. El mismo deberá realizarse utilizando
Python 3, aplicando los contenidos y reglas de estilo dados en esta cátedra.
Datos correspondientes de cada paciente:
- ID (int)
- Nombre (str)
- Apellido (str)
- Edad (int)
- Altura (int) (en centímetros)

1)
Peso (float) (en kilogramos)
DNI (int)
Grupo sanguíneo (str)

El programa debe contar con un menú como el siguiente:
1. Dar de alta. Pedirá los datos necesarios y dará de alta a un nuevo paciente, asignando un ID único autoincremental. 
2. Modificar. Permitirá alterar cualquier dato del paciente excepto su ID. Se usará el DNI para identificar al paciente a modificar. 
Mostrará un submenú para seleccionar qué datos modificar. Deberá indicarse si se realizaron modificaciones (y cuáles) o no.
3. Eliminar. Eliminará permanentemente a un paciente del listado original. Se pedirá el DNI del paciente a eliminar.
4. Mostrar todos.
Imprimirá por consola la información de todos los pacientes en formato de tabla:
*****************************************************************************************
| Nombre | Apellido | Edad | Altura | Peso | DNI | Grupo sanguíneo |
—------------------------------------------------------------------------------------------------
| Luis | Ruiz | 36 | 181 cm | 75.5 kg | 12345678 | A+ |
| Maria | Gomez | 25 | 170 cm | 65.5 kg | 33555987 | AB- |
*****************************************************************************************
5. Ordenar pacientes. Ofrecer la opción de ordenar y mostrar la lista de pacientes de forma ascendente o descendente por:
    a. Nombre.
    b. Apellido.
    c. Altura.
    d. Grupo sanguíneo.
6. Buscar paciente por DNI: Permitir al usuario buscar y mostrar la información de un paciente específico ingresando su DNI.
7. Calcular promedio: Mostrar un submenú que permita calcular y mostrar el promedio de:
    a. Edad.
    b. Altura.
    c. Peso.
8. Salir. Terminará la ejecución del programa.

2)Validaciones:
Todos los ingresos de datos por consola deberán estar validados.
● El nombre y el apellido deberán estar compuestos únicamente por caracteres alfabéticos comenzando en mayúscula y no podrán exceder los 20 caracteres cada uno.
● La edad y la altura deberán estar compuestas únicamente por caracteres numéricos.La edad no podrá ser menor a 1 ni mayor a 120. 
La altura no podrá ser menor a 30 ni mayor a 230.
● El peso deberá estar compuesto únicamente por valores numéricos y puntos, al tratarse de un flotante. No podrá ser menor a 10 ni mayor a 300.
● El DNI deberá estar compuesto exactamente por 8 caracteres numéricos.(Ej: Si se ingresa el DNI 345, deberá guardarse 00000345.) 
No podrá ser menor a 4000000 ni mayor a 99999999.
● El grupo sanguíneo deberá estar compuesto únicamente por el indicador A, B, AB o 0 con su correspondiente símbolo + o -.
Primera parte:
    El estudiante deberá presentarse el día del parcial con el programa completo y funcionando.
    El código completo deberá ser subido a un repositorio privado de github con el nombre
    “PP_PROGRAMACION_I_111_apellido” (deberán reemplazar la palabra apellido por su verdadero apellido) 
    y deberá agregarse como colaboradores a los usuarios:
● german2017
● GioLucc
Durante esta primera etapa deberá realizar mínimo dos commits: el primero durante la clase de inicio del examen (06/06) y otro durante el desarrollo asincrónico.
Completar el formulario del espacio del parcial en el aula virtual con sus datos .
Todo el código deberá estar programado respetando las reglas de estilo y los conceptos vistos durante el transcurso de la cursada. 
Se tendrá en cuenta la prolijidad del código.
El programa deberá contar al menos con los módulos:
main.py: Donde se encontrará el menú principal y se hará el llamado a las funciones necesarias para su funcionamiento.
inputs.py: Donde se realizarán todas las funciones relacionadas a los ingresos de datos y a las validaciones correspondientes.
pacientes.py: Donde se realizan todas las funciones que permitan interactuar con la entidad paciente.

3) El código deberá ser programado en funciones modularizadas y reutilizables con su correspondiente documentación.
Aclaraciones:
● No se deberá poder ingresar a cualquier opción de la 2 a la 7 sin antes haber dado de alta al menos un paciente.
● Al ordenar la lista de pacientes deberá utilizarse el algoritmo visto y trabajado en clase (Bubble Sort / Burbujeo). 
En caso de utilizar otro algoritmo de ordenamiento (Quick Sort, Merge Sort, etc) el alumno deberá comprender y saber explicar claramente 
la forma en que el mismo trabaja. No se aceptará la utilización del método sort() de listas para realizar los ordenamientos.
● El uso de cualquier herramienta que no se haya visto en clases deberá ser justificado y defendido el día del 
"""

from os import system
from Pacientes import *
from Inputs import *

def __init__(self):
    self.lista_de_pacientes = []

def mostrar_opciones_pacientes():
    return(
        "\nMenú de gestión de Pacientes: \n"
        "1. Dar de alta paciente. \n"
        "2. Modificar paciente. \n"
        "3. Eliminar pacientes. \n"
        "4. Mostrar todos los pacientes. \n"
        "5. Ordenar pacientes. \n"
        "6. Buscar paciente por el DNI. \n"
        "7. Calcular promedio. \n"
        "8. Salir. \n"
    )
    

def menu_principal():
    while True:
        system("cls")
        print(mostrar_opciones_pacientes())
        opcion = ("Silecciona una opción: ")
        match opcion:
            case "1":
                pass
            case "2":
                nombre = nombre_valido("Ingrese el nombre del paciente: ", 3, 20)
                apellido = nombre_valido("Ingrese el apellido del paciente: ", 3, 20)
                edad = edad_valido("Ingrese la edad del paciente: ")
                altura = altura_valido("Ingrese la altura del paciente: ")
                peso = peso_valido("Ingrese el peso del paciente: ")
                dni = dni_valido("Ingrese el dni del paciente: ")
                grupo_sanguineo = grupo_sanguineo_valido("Ingrese el grupo sanguineo del paciente: ")
                Enfermero.modificar_pacientes(nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
            case "3":
                Enfermero.eliminar_pacientes()
            case "4":
                Enfermero.mostrar_todosLos_pacientes()
            case "5":
                Enfermero.Ordenar()
            case "6":
                dni = dni_valido("Ingrese el dni del paciente: ")
                print(Enfermero.buscar_pacientes(dni))
            case "7":
                tipo = input("Ingrese el tipo de promedio a calcular (edad, altura, peso): ")
                print(Enfermero.promedio(tipo))
            case "8":
                print("Saliendo del programa. \n")
                break
            case _:
                print("Opción no valida. Intentalo de nuevo. \n")
                
        system("pause")
        system("cls")
    
menu_principal()