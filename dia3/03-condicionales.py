# programa que realiza operaciones sumas resta multiplicacion division
# entrada
numero1 = int(input("ingrese el primer número entero: "))
numero2 = int(input("ingrese el segundo numero entero: "))
operacion = input("ingrese la operacion(+,-,*,/): ")
# proceso
if(operacion == "+"):
    resultado = numero1 + numero2
elif(operacion == "-"):
     resultado = numero1 - numero2
elif(operacion == "*"):
     resultado = numero1 * numero2
elif(operacion == "/"):
     resultado = numero1 / numero2
else:
     print("operacion no valida")
     exit()

# salida
print(f"el resultado de {numero1} {operacion} {numero2} es {resultado}")