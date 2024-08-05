import random


def juego_adivinanza():
    # Generar un numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    # Primeras líneas del juego donde se da la bienvenida
    print("¡Bienvenido al juego de adivinanza de número.!")
    print("Debes adivinar un número entre el 1 al 100.")
    print("¡Intenta adivinar.!")

    while not adivinado:
        # Solicitar un numero del 1 al 100
        adivinanza = input("Introduzca un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)  # Lo estamos pasando de string a numero entero
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(
                    f"¡Felicitaciones, has ganado! El número {adivinanza} es el número secreto, y lo has logrado en {intentos} intentos."
                )
        else:
            print("Por favor introduzca un número válido entre el 1 y el 100.")


juego_adivinanza()
