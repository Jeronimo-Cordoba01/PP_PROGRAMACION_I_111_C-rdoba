def iden_valida(mensaje):
    """
    Esta función valida un identificador ingresado por el usuario. El identificador debe ser un número entre 1 y 9999.
    Si se cumplen los 3 intentos fallidos, la función retorna None.
    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar el identificador.
    Returns:
        int or None: El identificador validado como un entero si es válido, None si se excedieron los intentos.
    """
    reintentos = 0
    while reintentos < 3:
        iden = input(mensaje).strip()
        if iden.isdigit() and 1 <= int(iden) <= 9999:
            return int(iden)
        print("Identificador inválido. Por favor, ingrese un número entre 1 y 9999.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def nombre_apellido_valida(mensaje, minimo, maximo):
    """
    Esta función valida un nombre o apellido ingresado por el usuario. Verifica que se ingrese un texto alfabético.
    Si se cumplen los 3 intentos fallidos, la función retorna None.
    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar el nombre o apellido.
        minimo (int): El número mínimo de caracteres permitidos.
        maximo (int): El número máximo de caracteres permitidos.
    Returns:
        str or None: El nombre o apellido validado como una cadena si es válida, None si se excedieron los intentos.
    """
    reintentos = 0
    while reintentos < 3:
        nombre = input(mensaje).strip()
        if minimo <= len(nombre) <= maximo and nombre.isalpha():
            return nombre
        print(f"Nombre inválido. Por favor, ingrese un texto alfabético entre {minimo} y {maximo} caracteres.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def edad_valida(mensaje):
    """
    Esta función valida una edad ingresada por el usuario. Verifica que se ingrese un número entre 1 y 120.
    Si se cumplen los 3 intentos fallidos, la función retorna None.
    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar la edad.
    Returns:
        int or None: La edad validada como un entero si es válida, None si se excedieron los intentos.
    """
    reintentos = 0
    while reintentos < 3:
        edad = input(mensaje).strip()
        if edad.isdigit() and 1 <= int(edad) <= 120:
            return int(edad)
        print("Edad inválida. Por favor, ingrese un número entre 1 y 120.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def altura_valida(mensaje):
    """
    Esta función valida una altura ingresada por el usuario. Verifica que se ingrese un número entre 30 y 230 centímetros.
    Si se cumplen los 3 intentos fallidos, la función retorna None.
    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar la altura.
    Returns:
        int or None: La altura validada como un entero si es válida, None si se excedieron los intentos.
    """
    reintentos = 0
    while reintentos < 3:
        altura = input(mensaje).strip()
        if altura.isdigit() and 30 <= int(altura) <= 230:
            return int(altura)
        print("Altura inválida. Por favor, ingrese un número entre 30 y 230 cm.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def peso_valida(mensaje):
    """
    Esta función valida un peso ingresado por el usuario. Verifica que se ingrese un número entre 10 y 300 kilogramos.
    Si se cumplen los 3 intentos fallidos, la función retorna None.
    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar el peso.
    Returns:
        float or None: El peso validado como un flotante si es válido, None si se excedieron los intentos.
    """
    reintentos = 0
    while reintentos < 3:
        kilos = input(mensaje).strip()
        if kilos.replace('.', '', 1).isdigit() and 10 <= float(kilos) <= 300:
            return float(kilos)
        print("Peso inválido. Por favor, ingrese un número entre 10 y 300 kg.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def dni_valida(mensaje):
    """
    Esta función valida un DNI ingresado por el usuario. Verifica que se ingrese un número de 8 cifras.
    Si se cumplen los 3 intentos fallidos, la función retorna None.
    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar el DNI.
    Returns:
        int or None: El DNI validado como un entero si es válido, None si se excedieron los intentos.
    """
    reintentos = 0
    while reintentos < 3:
        dni = input(mensaje).strip()
        if dni.isdigit() and len(dni) == 8 and 4000000 <= int(dni) <= 99999999:
            return int(dni)
        print("DNI inválido. Por favor, ingrese un número de 8 cifras.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def grupo_sanguineo_valida(mensaje):
    """
    Esta función valida un grupo sanguíneo ingresado por el usuario. Verifica que se ingrese uno de los siguientes valores: A+, A-, B+, B-, AB+, AB-, O+, O-.
    Si se cumplen los 3 intentos fallidos, la función retorna None.
    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar el grupo sanguíneo.
    Returns:
        str or None: El grupo sanguíneo validado como una cadena si es válido, None si se excedieron los intentos.
    """
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

def alta(): #Para usar en la consigna 1
    """
    Este es un submenú para dar de alta un paciente.
    """
    print("¿Quiere dar de alta un paciente?")
    print("1. Sí")
    print("2. No")
    
def seguro(): #Para usar en la consigna 1
    """
    Este es un submenú para confirmar una acción.
    """
    print("¿Seguro?")
    print("1. Sí")
    print("2. No")
    
def menu_ordenar(): #Para usar en la consigna 5
    """
    Este es un submenú para ordenar los datos de un paciente.
    """
    print("En qué campo desea ordenar:")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Altura")
    print("4. Grupo sanguíneo")
    print("5. Salir")
    
def menu_ordenar_tipo(): #Para usar en la consigna 5
    print("En qué campo desea ordenar:")
    print("Ascendente")
    print("Descendente")
    
def menu_promedio(): #Para usar en la consigna 7
    """
    Este es un submenú para calcular el promedio de los datos de los pacientes.
    """
    print("1. Edad")
    print("2. Altura")
    print("3. Peso")
    print("4. Salir")