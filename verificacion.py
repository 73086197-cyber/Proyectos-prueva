# Libreria de verificacion de numeros

def leer_entero_positivo(mensaje):
    """
    Solicita al usuario un numero entero positivo.
    Repite hasta que el valor sea valido.
    """
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("Error: el numero debe ser mayor que cero.")
        except ValueError:
            print("Error: ingrese solo numeros enteros.")
