def iden_valido(mensaje):
    while True:
        iden = input(mensaje).strip()
        if iden.isdigit() and 1 <= int(iden) <= 9999:
            return int(iden)
        print("Identificador inválido. Por favor, ingrese un número entre 1 y 9999.")

def nombre_valido(mensaje, minimo, maximo):
    while True:
        nombre = input(mensaje).strip()
        if minimo <= len(nombre) <= maximo and nombre.isalpha():
            return nombre
        print(f"Opción inválida. Por favor, ingrese un texto alfabésico entre {minimo} y {maximo} caracteres.")

def apellido_valido(mensaje, minimo, maximo):
    while True:
        apellido = input(mensaje).strip()
        if minimo <= len(apellido) <= maximo and apellido.isalpha():
            return apellido
        print(f"Opción inválida. Por favor, ingrese un texto alfabésico entre {minimo} y {maximo} caracteres.")

def edad_valido(mensaje):
    while True:
        edad = input(mensaje).strip()
        if edad.isdigit() and 1 <= int(edad) <= 120:
            return int(edad)
        print("Edad inválida. Por favor, ingrese un número entre 1 y 120.")

def altura_valido(mensaje):
    while True:
        altura = input(mensaje).strip()
        if altura.isdigit() and 30 <= int(altura) <= 230:
            return int(altura)
        print("Altura inválida. Por favor, ingrese un número entre 30 y 230 cm.")

def peso_valido(mensaje):
    while True:
        kilos = input(mensaje).strip()
        if kilos.isdigit() and 10 <= int(kilos) <= 300:
            return float(kilos)
        print("Peso inválido. Por favor, ingrese un número entre 10 y 300 kg.")

def dni_valido(mensaje):
    while True:
        dni = input(mensaje).strip()
        if dni.isdigit() and len(dni) == 8 and 4000000 <= int(dni) <= 99999999:
            return int(dni)
        print("DNI inválido. Por favor, ingrese un número de 8 cifras.")

def grupo_sanguineo_valido(mensaje):
    grupo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    while True:
        if valor in grupo_sanguineo:
            break
        print("Grupo sanguineo inválido. Por favor, ingrese A+, A-, B+, B-, AB+, AB-, O+, O-.")
        valor = input(mensaje).strip()
    return valor

def menu_ordenar():
    print("1. Nombre")
    print("2. Apellido")
    print("3. Altura")
    print("4. Grupo sanguineo")
    print("5. Salir")
    
def menu_promedio():
    print("1. Edad")
    print("2. Altura")
    print("3. Peso")
    print("4. Salir")
    