# Programa para calcular MCD y MCM
# Interfaz en texto plano

def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    return (a * b) // calcular_mcd(a, b)

# Interfaz de usuario
print("===================================")
print("   CALCULO DE MCD Y MCM")
print("===================================")

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))

mcd = calcular_mcd(n1, n2)
mcm = calcular_mcm(n1, n2)

print("\nRESULTADOS")
print("MCD =", mcd)
print("MCM =", mcm)
