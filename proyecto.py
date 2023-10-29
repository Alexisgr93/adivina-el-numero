import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)

    print("¡Bienvenido a Adivina el Número!")
    num_jugadores = int(input("¿Cuántos jugadores van a participar? "))
    intentos_maximos = int(input("¿Cuántos intentos desean por participante? "))

    jugadores = []

    for i in range(num_jugadores):
        nombre_jugador = input(f"Jugador {i + 1}, por favor introduce tu nombre: ")
        jugadores.append({"nombre": nombre_jugador, "intentos": 0, "intentos_maximos": intentos_maximos, "puntuacion": 0, "agotado": False})

    puntuaciones_altas = {}  # Diccionario para mantener un registro de las puntuaciones más altas

    print("Estoy pensando en un número entre 1 y 100.")

    adivinaron = False  # Variable para rastrear si alguien adivinó

    while not adivinaron:
        for jugador in jugadores:
            if not jugador['agotado'] and jugador['intentos'] < jugador['intentos_maximos']:
                intento = input(f"{jugador['nombre']}, intento {jugador['intentos']+1}, ¿Cuál es tu adivinanza? ")
                jugador['intentos'] += 1

                try:
                    intento = int(intento)
                except ValueError:
                    print("Por favor, ingresa un número válido.")
                    continue

                if intento < numero_secreto:
                    print(f"{jugador['nombre']}, mi número es mayor que {intento}")
                elif intento > numero_secreto:
                    print(f"{jugador['nombre']}, mi número es menor que {intento}")
                else:
                    if jugador['puntuacion'] == 0:  # Evitar sobrescribir la puntuación si un jugador ya adivinó
                        if jugador['intentos'] == 1:
                            puntos = 100
                        else:
                            puntos = 100 + jugador['intentos']
                        jugador['puntuacion'] = puntos
                    print(f"¡Felicidades, {jugador['nombre']}! ¡Adivinaste el número en {jugador['intentos']} intentos y obtuviste {jugador['puntuacion']} puntos!")
                    adivinaron = True  # Cambiamos adivinaron a True
                    break  # Salimos del bucle for cuando alguien adivina
            elif not jugador['agotado']:
                jugador['agotado'] = True  # Establecemos el estado "agotado" del jugador
                if jugador['intentos'] == jugador['intentos_maximos']:
                    jugador['puntuacion'] = jugador['intentos']  # Asignar puntos igual a la cantidad de intentos
                adivinaron = True  # Terminamos el juego si un jugador agotó sus intentos

    # Verificar si algún jugador adivinó
    if adivinaron:
        puntuaciones_totales = sum(jugador['puntuacion'] for jugador in jugadores)
        
        print("Puntuaciones finales para", num_jugadores, "jugadores:")
        for jugador in jugadores:
            if jugador['puntuacion'] == 0:  # Evitar que los perdedores tengan 0 puntos
                jugador['puntuacion'] = jugador['intentos']
            print(f"{jugador['nombre']} - Puntuación: {jugador['puntuacion']} puntos - Intentos: {jugador['intentos']} de {jugador['intentos_maximos']}")
            
            # Actualizar registro de puntuaciones altas
            if jugador['nombre'] not in puntuaciones_altas or puntuaciones_altas[jugador['nombre']] < jugador['puntuacion']:
                puntuaciones_altas[jugador['nombre']] = jugador['puntuacion']

        print("Puntuación total de todos los jugadores: ", puntuaciones_totales)
        
        print("Puntuaciones más altas:")
        for nombre, puntuacion in puntuaciones_altas.items():
            print(f"{nombre} - Puntuación más alta: {puntuacion} puntos")

if __name__ == "__main__":
    adivina_el_numero()

