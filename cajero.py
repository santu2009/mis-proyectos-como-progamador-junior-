import random
import time
import os

def pausa(segundos=1.5):
    time.sleep(segundos)

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_linea():
    print("-" * 40)

# INICIO
limpiar()
print("Bienvenido a tu cajero automático")
pausa()
print("Por favor, inicia sesión...")
pausa()
imprimir_linea()

edad = int(input("Ingresa tu edad: "))
if edad < 18:
    print("Eres menor de edad, vuelve cuando tengas 18 años.")
    exit()
print("Puedes continuar.")
pausa()

# REGISTRO
print("\nRegistro de usuario")
imprimir_linea()
nombre = input("Nombre: ")
contraseña = input("Crea una contraseña: ")
contraseña1 = input("Repite la contraseña: ")
if contraseña1 != contraseña:
    print("Las contraseñas no coinciden. Intenta nuevamente.")
    exit()
print("Registro exitoso.")
pausa()

# INICIO DE SESIÓN
imprimir_linea()
usu = input("Ingresa tu nombre de usuario: ")
if usu != nombre:
    print("Usuario incorrecto.")
    exit()
contra = input("Ingresa tu contraseña: ")
if contra != contraseña:
    print("Contraseña incorrecta.")
    exit()
print("Inicio de sesión exitoso.")
pausa()

# SALDO
saldo = random.randint(1000, 2000000)

# MENÚ
opcion = 0
while opcion != 6:
    limpiar()
    imprimir_linea()
    print("MENÚ PRINCIPAL")
    imprimir_linea()
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Consignar dinero")
    print("4. Cambiar contraseña")
    print("5. Imprimir recibo")
    print("6. Salir")
    imprimir_linea()
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("Ingresa un número válido.")
        pausa()
        continue
    pausa()

    if opcion == 1:
        print(f"Tu saldo actual es: {saldo:,} col\n")
        pausa(2)

    elif opcion == 2:
        retiro = int(input("¿Cuánto deseas retirar?: "))
        if retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Has retirado {retiro:,} col exitosamente.")
        pausa(2)

    elif opcion == 3:
        deposito = int(input("¿Cuánto deseas consignar?: "))
        if deposito <= 0:
            print("Monto no válido.")
        else:
            saldo += deposito
            print(f"Se consignaron {deposito:,} col a tu cuenta.")
        pausa(2)

    elif opcion == 4:
        actual = input("Ingresa tu contraseña actual: ")
        if actual == contraseña:
            nueva = input("Nueva contraseña: ")
            repetir = input("Repite la nueva contraseña: ")
            if nueva == repetir:
                contraseña = nueva
                print("Contraseña actualizada exitosamente.")
            else:
                print("Las nuevas contraseñas no coinciden.")
        else:
            print("Contraseña actual incorrecta.")
        pausa(2)

    elif opcion == 5:
        print("\nImprimiendo recibo...")
        pausa(2)
        print("------ RECIBO BANCARIO ------")
        print(f"Usuario: {nombre}")
        print(f"Saldo actual: {saldo:,} col")
        print("Gracias por usar nuestro servicio.")
        print("-----------------------------")
        pausa(3)

    elif opcion == 6:
        print("Gracias por usar el cajero. Hasta luego.")
        pausa(2)
    else:
        print("Opción inválida. Intenta nuevamente.")
        pausa(2)





    

