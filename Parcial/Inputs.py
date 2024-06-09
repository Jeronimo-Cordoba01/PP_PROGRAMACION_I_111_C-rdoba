def iden_valido(mensaje):
    """
    Identificador valido.
    •	La función iden_valido valida un identificador numérico ingresado por el usuario.
    •	Se permite un máximo de 3 intentos para ingresar un número válido entre 1 y 9999.
    •	Utiliza el método input para capturar la entrada del usuario y strip para eliminar espacios en blanco.
    •	Verifica que la entrada sea un dígito (isdigit) y esté dentro del rango permitido.
    •	Si el usuario ingresa un identificador válido, la función retorna el valor como un entero.
    •	Si se exceden los 3 intentos, se imprime un mensaje de error y se retorna None.

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
    Nombre y Apellido valido.
    •	La función nombre_apellido_valido valida un nombre o apellido ingresado por el usuario.
    •	Permite un máximo de 3 intentos para ingresar un texto alfabético con una longitud entre minimo y maximo.
    •	Usa input para capturar la entrada y strip para eliminar espacios en blanco.
    •	Verifica que la longitud del texto esté dentro del rango permitido y que sea alfabético (isalpha).
    •	Si el usuario ingresa un nombre o apellido válido, la función retorna el texto.
    •	Si se exceden los 3 intentos, se imprime un mensaje de error y se retorna None.

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
    Validación de una edad.
    •	La función edad_valido valida una edad ingresada por el usuario.
    •	Permite un máximo de 3 intentos para ingresar un número entre 1 y 120.
    •	Usa input para capturar la entrada y strip para eliminar espacios en blanco.
    •	Verifica que la entrada sea un dígito (isdigit) y esté dentro del rango permitido.
    •	Si el usuario ingresa una edad válida, la función retorna el valor como un entero.
    •	Si se exceden los 3 intentos, se imprime un mensaje de error y se retorna None.
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
    Validación de una altura.
    •	La función altura_valido valida una altura ingresada por el usuario.
    •	Permite un máximo de 3 intentos para ingresar un número entre 30 y 230 centímetros.
    •	Usa input para capturar la entrada y strip para eliminar espacios en blanco.
    •	Verifica que la entrada sea un dígito (isdigit) y esté dentro del rango permitido.
    •	Si el usuario ingresa una altura válida, la función retorna el valor como un entero.
    •	Si se exceden los 3 intentos, se imprime un mensaje de error y se retorna None.
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
    Validación de un peso.
    •	La función peso_valido valida un peso ingresado por el usuario.
    •	Permite un máximo de 3 intentos para ingresar un número entre 10 y 300 kilogramos.
    •	Usa input para capturar la entrada y strip para eliminar espacios en blanco.
    •	Verifica que la entrada sea un dígito (isdigit) y esté dentro del rango permitido.
    •	Si el usuario ingresa un peso válido, la función retorna el valor como un flotante.
    •	Si se exceden los 3 intentos, se imprime un mensaje de error y se retorna None.
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
    Validación de un DNI.
    •	La función dni_valido valida un DNI ingresado por el usuario.
    •	Permite un máximo de 3 intentos para ingresar un número de 8 dígitos entre 4000000 y 99999999.
    •	Usa input para capturar la entrada y strip para eliminar espacios en blanco.
    •	Verifica que la entrada sea un dígito (isdigit), que tenga 8 caracteres y esté dentro del rango permitido.
    •	Si el usuario ingresa un DNI válido, la función retorna el valor como un entero.
    •	Si se exceden los 3 intentos, se imprime un mensaje de error y se retorna None.

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
    Validación de un grupo sanguíneo.
    •	La función grupo_sanguineo_valido valida un grupo sanguíneo ingresado por el usuario.
    •	Permite un máximo de 3 intentos para ingresar uno de los valores válidos: A+, A-, B+, B-, AB+, AB-, O+, O-.
    •	Usa input para capturar la entrada y strip para eliminar espacios en blanco, convirtiendo la entrada a mayúsculas (upper).
    •	Verifica que la entrada esté dentro de la lista de valores válidos.
    •	Si el usuario ingresa un grupo sanguíneo válido, la función retorna el valor.
    •	Si se exceden los 3 intentos, se imprime un mensaje de error y se retorna None.
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
    