#AHORACADO
import random
#Palabra a adivinar posiblemente
palabras = ["perro", "gato", "loro", "lobo", "gallina", "tigre", "leon", "aguila", "raton", "mosca"]
#Palabra a adivinar
palabra_generada = random.choice(palabras)
#Palabra que se estará formando por partes
palabra_por_partes = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
palabra_unida = ""

vida = 5
letra = ""
palabra_a_formarse = [len(palabra_generada)]
respuesta_definitiva = ""

print("¡Bienvenido al juego de AHORACADOS!")
print("Temática: Animales")
print("Recuerda que tienes 5 vidas")

repetir = 1

while repetir == 1:
    palabra_generada = random.choice(palabras)
    palabra_por_partes = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]
    palabra_unida = ""

    vida = 5
    letra = ""
    palabra_a_formarse = [len(palabra_generada)]
    respuesta_definitiva = ""

    while respuesta_definitiva != palabra_generada:
        letra = input("Insertar letra...")
        if letra in palabra_generada:
            for elemento in range(len(palabra_generada)):
                if palabra_generada[elemento] == letra:
                    palabra_por_partes[elemento] = letra
                else:
                    palabra_por_partes[elemento] == "@"
            for elemento in palabra_por_partes:
                if len(palabra_unida) >= len(palabra_generada):
                    palabra_unida += ""
                else:
                    palabra_unida += elemento
            if palabra_generada in palabra_unida:
                print("FELICIDADES! LA PALABRA ERA:", palabra_generada)
                break
            print("Palabra formada en juego: ", palabra_unida)
            palabra_unida = ""
        else:
            vida -= 1
            print("¡ERROR! ", vida, " vidas")
            if vida == 0:
                print("PERDISTE...")
                print("La palabra era:", palabra_generada)
                break
    repetir = int(input("¿Deseas empezar nuevamente la partida? | 1. Sí | 2. No |"))
    if(repetir == 2):
        print("GRACIAS POR JUGAR :D")