import os
from time import sleep

bandera = True

while bandera:
    print("===== CALCULADORA =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado}")

    elif opcion == 2:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado}")

    elif opcion == 3:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicación es: {resultado}")

    elif opcion == 4:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("No se puede dividir entre 0")

    elif opcion == 5:
        print("Gracias por usar la calculadora!")
        break

    else:
        print("Opción no válida, intenta nuevamente")

    sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

    bandera = input("¿Desea continuar? (si/no): ").lower() == "si"