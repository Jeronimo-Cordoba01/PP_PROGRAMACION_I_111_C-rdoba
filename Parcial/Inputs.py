def iden_valido(mensaje):
    """
    Esta función valida un identificador ingresado por el usuario. El identificador debe ser un número entre 1 y 9999.
    Si se cumple los 3 intentos fallidos, la función retorna None. Y regresa al menu principal.

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

def nombre_apellido_valido(mensaje, minimo, maximo):
    """
    Esta función valida un nombre o apellido ingresado por el usuario. Verifica que se ingrese un texto alfabético.
    Si se cumple los 3 intentos fallidos, la función retorna None. Y regresa al menu principal.

    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar el nombre o apellido.
        minimo (int): El número minimo de caracteres permitidos.
        maximo (int): El número maximo de caracteres permitidos.

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

def edad_valido(mensaje):
    """
    Esta función valida una edad ingresada por el usuario. Verifica que se ingrese un número entre 1 y 120.
    Si se cumple los 3 intentos fallidos, la función retorna None. Y regresa al menu principal.

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

def altura_valido(mensaje):
    """
    Esta función valida una altura ingresada por el usuario. Verifica que se ingrese un número entre 30 y 230 centimetros.
    Si se cumple los 3 intentos fallidos, la función retorna None. Y regresa al menu principal.

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

def peso_valido(mensaje):
    """
    Esta función valida un peso ingresado por el usuario. Verifica que se ingrese un número entre 10 y 300 kilogramos.
    Si se cumple los 3 intentos fallidos, la función retorna None. Y regresa al menu principal.

    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar el peso.

    Returns:
        float or None: El peso validado como un entero si es válido, None si se excedieron los intentos.
    """
    reintentos = 0
    while reintentos < 3:
        kilos = input(mensaje).strip()
        if kilos.isdigit() and 10 <= float(kilos) <= 300:
            return float(kilos)
        print("Peso inválido. Por favor, ingrese un número entre 10 y 300 kg.")
        reintentos += 1
    print("Demasiados intentos fallidos.")
    return None

def dni_valido(mensaje):
    """
    Esta función valida un DNI ingresado por el usuario. Verifica que se ingrese un número de 8 cifras.
    Si se cumple los 3 intentos fallidos, la función retorna None. Y regresa al menu principal.

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

def grupo_sanguineo_valido(mensaje):
    """
    Esta función valida un grupo sanguineo ingresado por el usuario.
    Verifica que se ingrese uno de los siguientes valores: A+, A-, B+, B-, AB+, AB-, O+, O-.
    Si se cumple los 3 intentos fallidos, la función retorna None. Y regresa al menu principal.

    Args:
        mensaje (str): El mensaje a mostrar al usuario para solicitar el grupo sanguineo.

    Returns:
        Un mensaje de error o None si el grupo sanguineo es válido.
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


def alta():
    """
    Este es un sub-menu para dar de alta un paciente.
    """
    print("¿Quiere dar de alta un paciente?")
    print("1. Si")
    print("2. No")

def seguro():
    """
    Este es un sub-menu para confirmar una accion.
    """
    print("¿Seguro?")
    print("1. Si")
    print("2. No")

def menu_ordenar():
    """
    Este es un sub-menu para ordenar los datos de un paciente.
    """
    print("En que campo desea ordenar:")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Altura")
    print("4. Grupo sanguineo")
    print("5. Salir")
    
def menu_promedio():
    """
    Este es un sub-menu para promediar los datos de un paciente.
    """
    print("1. Edad")
    print("2. Altura")
    print("3. Peso")
    print("4. Salir")
    