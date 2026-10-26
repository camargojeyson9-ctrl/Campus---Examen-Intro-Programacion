# Realizo las funciones con las cuales hago el retiro, deposito y consulta de saldo.

def consultar_saldo (balance):
    balance= saldo
    return balance

def depositar (ingreso):
    ingreso = saldo + ingreso
    return ingreso

def retirar (retiro):
    retiro = saldo - retiro
    return retiro

# Realizo las variables con las cuales voy a operar

saldo = 1000
ingreso = 0
retiro  = 0

print("\n---BIENVENIDO AL CAJERO AUTOMATICO---")

# Realizo bucle que me va a permitir interactuar en los menus y colocar las funciones creadas.

while True:
    print("\nEscoge una opcion del siguiente menu: ")
    print("\n 1. Consultar Saldo")
    print(" 2. Depositar dinero")
    print(" 3. Retirar dinero")
    print(" 4. Digita el numero 4 o 0 para salir del cajero")

    opcion = int(input("\nEscoge una opcion del 1 al 4: "))

    if opcion == 1:
        # Este print me imprime el saldo actual.
        print("El saldo actual es: ", consultar_saldo(saldo))
        print("---------------------------------------------\n")

    elif opcion == 2:
        ingreso = int(input("Ingresa el monto que deseas depositar: "))
        # Si el ingreso es menor a 0 da error y repite el bucle.
        if ingreso > 0:
            saldo = depositar(ingreso)
            print("\n!Felicitaciones tu deposito se ha guardado satisfactoriamente!")

            # Actualiza el saldo e imprime confirmacion de deposito y nuevo saldo
            print("Tu nuevo saldo es:",consultar_saldo(saldo))
            print("----------------------------------------------------------------\n")
        else:
            print("\n[!]El ingreso debe ser mayor a 0")
            print("---------------------------------\n")

    elif opcion == 3:
        retiro = int(input("Ingresa el monto que deseas retirar: "))
        # Si el retiro es menor a 0 o mayor que el saldo da error y repite el bucle.
        if retiro > 0 and retiro < saldo:

            # Actualiza el saldo e imprime confirmacion de retiro y nuevo saldo
            saldo = retirar(retiro)
            print("\nRetiro realizado exitosamente")
            print("Tu nuevo saldo es:",consultar_saldo(saldo))
            print("-------------------------------\n")

        else:
            print("\nEl retiro debe ser mayor a 0 y menor que el saldo disponible")
            print("Si desconoces cuanto saldo tienes escoge en el menu la opcion 1.")
            print("---------------------------------------------------------------\n")

    # Estos condicionales cierran el programa.
    elif opcion == 4:
        print("\nGracias por visitar tu cajero de confianza")
        print("             !NOS VEMOS PRONTO!             \n")
        break

    elif opcion == 0:
            print("\nGracias por visitar tu cajero de confianza")
            print("             !NOS VEMOS PRONTO!             \n")
            break

    # Si ingresa un numero invalido repite el bucle.
    else:
        print("\nERROR")
        print("[!]Escoge una opcion valida del (1 al 4)")
        print("-----------------------------------------\n")


