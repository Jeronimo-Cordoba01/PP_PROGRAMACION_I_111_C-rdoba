def iden_valido(mensaje):
    reintentos = 0
    while reintentos < 3:
        iden = input(mensaje).strip()
        if iden.isdigit() and 1 <= int(iden) <= 9999:
            return int(iden)
        print("Identificador inválido. Por favor, ingrese un número entre 1 y 9999.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def nombre_apellido_valido(mensaje, minimo, maximo):
    reintentos = 0
    while reintentos < 3:
        nombre = input(mensaje).strip()
        if minimo <= len(nombre) <= maximo and nombre.isalpha():
            return nombre
        print(f"Nombre inválido. Por favor, ingrese un texto alfabético entre {minimo} y {maximo} caracteres.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def edad_valido(mensaje):
    reintentos = 0
    while reintentos < 3:
        edad = input(mensaje).strip()
        if edad.isdigit() and 1 <= int(edad) <= 120:
            return int(edad)
        print("Edad inválida. Por favor, ingrese un número entre 1 y 120.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def altura_valido(mensaje):
    reintentos = 0
    while reintentos < 3:
        altura = input(mensaje).strip()
        if altura.isdigit() and 30 <= int(altura) <= 230:
            return int(altura)
        print("Altura inválida. Por favor, ingrese un número entre 30 y 230 cm.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def peso_valido(mensaje):
    reintentos = 0
    while reintentos < 3:
        kilos = input(mensaje).strip()
        if kilos.isdigit() and 10 <= int(kilos) <= 300:
            return float(kilos)
        print("Peso inválido. Por favor, ingrese un número entre 10 y 300 kg.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def dni_valido(mensaje):
    reintentos = 0
    while reintentos < 3:
        dni = input(mensaje).strip()
        if dni.isdigit() and len(dni) == 8 and 4000000 <= int(dni) <= 99999999:
            return int(dni)
        print("DNI inválido. Por favor, ingrese un número de 8 cifras.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def grupo_sanguineo_valido(mensaje):
    reintentos = 0
    grupo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    while reintentos < 3:
        valor = input(mensaje).strip().upper()
        if valor in grupo_sanguineo:
            return valor
        print("Grupo sanguíneo inválido. Por favor, ingrese uno de los siguientes valores: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None


def alta():
    print("¿Quiere dar de alta un paciente?")
    print("1. Si")
    print("2. No")

def menu_ordenar():
    print("En que campo desea ordenar:")
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
    