"""
Jerónimo Facundo Lucas Córdoba - 1° Parcial 
Enunciado:
Se necesita realizar un programa para la administración de pacientes en una clínica privada que permita interactuar únicamente a través de la consola. 
El mismo deberá realizarse utilizando Python 3, aplicando los contenidos y reglas de estilo dados en esta cátedra.
Datos correspondientes de cada paciente:
- ID (int)
- Nombre (str)
- Apellido (str)
- Edad (int)
- Altura (int) (en centímetros)
- Peso (float) (en kilogramos)
- DNI (int)
- Grupo sanguíneo (str)

1) El programa debe contar con un menú como el siguiente:
1. Dar de alta. Pedirá los datos necesarios y dará de alta a un nuevo paciente, asignando un ID único autoincremental. 
2. Modificar. Permitirá alterar cualquier dato del paciente excepto su ID. Se usará el DNI para identificar al paciente a modificar. 
Mostrará un submenú para seleccionar qué datos modificar. Deberá indicarse si se realizaron modificaciones (y cuáles) o no.
3. Eliminar. Eliminará permanentemente a un paciente del listado original. Se pedirá el DNI del paciente a eliminar.
4. Mostrar todos. Imprimirá por consola la información de todos los pacientes en formato de tabla:
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
8. Determinar compartibilidad: la misma pedirá el ingreso del dni de un paciente y se encargará de mostrar cuáles son los grupos a los que un paciente puede donar 
y de los cuáles el paciente puede recibir sangre (Ver tabla de compatibilidad). Por otro lado esta opción mostrará una lista con los primeros 3 donantes 
(si es que existen) que podrán donar sangre para el paciente en cuestión. Compatibilidad Sanguínea:
    A+:
    Puede donar a: A+, AB+
    Puede recibir de: O+, O-, A+, A-
    
    A-:
    Puede donar a: A+, A-, AB+, AB-
    Puede recibir de: A-, O-
    
    B+:
    Puede donar a: B+, AB+
    Puede recibir de: O+, O-, B+, B-
    
    B-:
    Puede donar a: B+, B-, AB+, AB-
    Puede recibir de: B-, O-
    
    AB+:
    Puede donar a: AB+
    Puede recibir de: TODOS

    AB-:
    Puede donar a: AB+, AB-
    Puede recibir de: AB-, O-, A-, B-
    
    O+:
    Puede donar a: A+, B+, AB+, O+
    Puede recibir de: O+, O-

    O-:
    Puede donar a: TODOS
    Puede recibir de: O-
9. Salir. Terminará la ejecución del programa.

2)Validaciones:
Todos los ingresos de datos por consola deberán estar validados.
● El nombre y el apellido deberán estar compuestos únicamente por caracteres alfabéticos comenzando en mayúscula y no podrán exceder los 20 caracteres cada uno.
● La edad y la altura deberán estar compuestas únicamente por caracteres numéricos.La edad no podrá ser menor a 1 ni mayor a 120. 
La altura no podrá ser menor a 30 ni mayor a 230.
● El peso deberá estar compuesto únicamente por valores numéricos y puntos, al tratarse de un flotante. No podrá ser menor a 10 ni mayor a 300.
● El DNI deberá estar compuesto exactamente por 8 caracteres numéricos.(Ej: Si se ingresa el DNI 345, deberá guardarse 00000345.) 
No podrá ser menor a 4000000 ni mayor a 99999999. ¿La consigna no se contradice?
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

Deberán cumplirse todas las condiciones establecidas en la parte 1.
2° Parte - Agregar:
    1. Al iniciarse el programa deberá cargarse automáticamente la información en memoria a partir del archivo “pacientes.csv” 
    (Ud creará dicho archivo).
    2. Al ingresar a la opción salir el programa deberá guardar automáticamente el listado de pacientes en el mismo archivo 
    csv con los cambios que se hayan realizado. Si se realizó un ordenamiento a lo largo de la ejecución del programa, 
    al salir, deberá guardar el listado con el último ordenamiento que se haya aplicado.
Grabar un video (máximo 15 minutos) mostrando y explicando el código del parcial. Podrán seguir el siguiente guión a 
efectos de organizar la defensa y el tiempo presupuestado del video:
a. Mostrar el programa en tiempo de ejecución (3 min): ejecutar cada una de las opciones del CRUD y un ordenamiento. 
Evidenciar que al momento de ingresar datos, el programa no rompe, ni tiene un comportamiento indebido (por ejemplo,
si pedimos un número e ingresamos letras, el programa tiene que controlar ese comportamiento). 
La demostración deberá evidenciar la lectura y escritura en archivos (punto 1 y 2 segunda parte) y determinar la compatibilidad de un
paciente (punto 3 segunda parte).
b. Mostrar y explicar las funciones del CRUD (7 min): deberán explicar (sin leer código, pero si mostrándolo) las funciones 
principales del CRUD. Incluir en la explicación algunas funciones de validaciones, como por ejemplo la validación de
un DNI, un nombre, etc. Hacer hincapié en la modularización de funciones, en cómo se comunican entre ellas 
y la reutilización de las mismas.
c. Mostrar y explicar las funciones de la segunda parte (5 min): lecto escritura de archivos y la lógica que pensaron 
para el punto 3 (más allá que funcione o no).
"""

from os import system
from Pacientes import Enfermero
from Inputs import *

def mostrar_opciones_pacientes():
    """
    Muestra las opciones del menú de gestión de pacientes.  
    """
    return (
        "\nMenú de gestión de Pacientes: \n"
        "1. Dar de alta paciente. \n"
        "2. Modificar paciente. \n"
        "3. Eliminar pacientes. \n"
        "4. Mostrar todos los pacientes. \n"
        "5. Ordenar pacientes. \n"
        "6. Buscar paciente por el DNI. \n"
        "7. Calcular promedio. \n"
        "8. Determinar compatibilidad. \n"
        "9. Salir. \n"
        "0. Mostrar Matriz. \n"
    )

def menu_principal(enfermero):
    while True:
        system("cls")
        print(mostrar_opciones_pacientes())
        opcion = input("Selecciona una opción: ")
        match opcion:
            case "1":
                enfermero.dar_alta()
            case "2":
                enfermero.modificar_paciente()
            case "3":
                enfermero.eliminar_paciente()
            case "4":
                enfermero.mostrar_todosLos_pacientes()
            case "5":
                enfermero.Ordenar()
            case "6":
                enfermero.mostrar_paciente_por_DNI()
            case "7":
                enfermero.promedio()
            case "8":
                enfermero.determinar_compatibilidad()
            case "9":
                enfermero.salir()
                return
            case "0":
                enfermero.mostrar_matriz()
            case _:
                print("Opción no válida. Inténtalo de nuevo.")
        system("pause")
        system("cls")

if __name__ == "__main__":
    enfermero = Enfermero([])
    menu_principal(enfermero)