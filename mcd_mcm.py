# Programa principal para calcular MCD y MCM
# Usa una libreria de verificacion

from verificacion import leer_entero_positivo

def mcd(a, b):
    """Calcula el Maximo Comun Divisor"""
    while b != 0:
        a, b = b, a % b
    return a

def mcm(a, b):
    """Calcula el Minimo Comun Multiplo"""
    return (a * b) // mcd(a, b)

def menu():
    print("\n==============================")
    print("   CALCULO DE MCD Y MCM")
    print("==============================")
    print("1. Calcular MCD y MCM")
    print("2. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            n1 = leer_entero_positivo("Ingrese el primer numero: ")
            n2 = leer_entero_positivo("Ingrese el segundo numero: ")

            print("\nRESULTADOS")
            print("MCD =", mcd(n1, n2))
            print("MCM =", mcm(n1, n2))

        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida.")

