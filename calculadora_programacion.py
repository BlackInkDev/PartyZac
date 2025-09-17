import math

def menu():
    print("\nCalculadora de Programación")
    print("1. Operaciones básicas")
    print("2. Operaciones de bits")
    print("3. Conversiones de sistemas numéricos")
    print("4. Salir")

def operaciones_basicas():
    print("\nOperaciones Básicas")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = int(input("Selecciona una operación: "))

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        print(f"Resultado: {a + b}")
    elif opcion == 2:
        print(f"Resultado: {a - b}")
    elif opcion == 3:
        print(f"Resultado: {a * b}")
    elif opcion == 4:
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Error: División por cero")
    else:
        print("Opción no válida")

def operaciones_bits():
    print("\nOperaciones de Bits")
    print("1. AND (&)")
    print("2. OR (|)")
    print("3. XOR (^)")
    print("4. NOT (~)")
    print("5. Desplazamiento a la izquierda (<<)")
    print("6. Desplazamiento a la derecha (>>)")
    opcion = int(input("Selecciona una operación: "))

    a = int(input("Ingresa el primer número (entero): "))

    if opcion in [1, 2, 3, 5, 6]:
        b = int(input("Ingresa el segundo número (entero): "))

    if opcion == 1:
        print(f"Resultado: {a & b}")
    elif opcion == 2:
        print(f"Resultado: {a | b}")
    elif opcion == 3:
        print(f"Resultado: {a ^ b}")
    elif opcion == 4:
        print(f"Resultado: {~a}")
    elif opcion == 5:
        print(f"Resultado: {a << b}")
    elif opcion == 6:
        print(f"Resultado: {a >> b}")
    else:
        print("Opción no válida")

def conversiones_sistemas():
    print("\nConversiones de Sistemas Numéricos")
    print("1. Decimal a Binario")
    print("2. Decimal a Octal")
    print("3. Decimal a Hexadecimal")
    print("4. Binario a Decimal")
    print("5. Octal a Decimal")
    print("6. Hexadecimal a Decimal")
    opcion = int(input("Selecciona una conversión: "))

    if opcion in [1, 2, 3]:
        num = int(input("Ingresa un número decimal: "))
        if opcion == 1:
            print(f"Binario: {bin(num)[2:]}")
        elif opcion == 2:
            print(f"Octal: {oct(num)[2:]}")
        elif opcion == 3:
            print(f"Hexadecimal: {hex(num)[2:]}")
    elif opcion in [4, 5, 6]:
        num = input("Ingresa el número: ")
        if opcion == 4:
            print(f"Decimal: {int(num, 2)}")
        elif opcion == 5:
            print(f"Decimal: {int(num, 8)}")
        elif opcion == 6:
            print(f"Decimal: {int(num, 16)}")
    else:
        print("Opción no válida")

def main():
    while True:
        menu()
        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            operaciones_basicas()
        elif opcion == 2:
            operaciones_bits()
        elif opcion == 3:
            conversiones_sistemas()
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()