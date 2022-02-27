def gravedad(peso, gravity, planeta):
    resultado = peso / gravity
    resultado = round(resultado, 2)
    resultado = str(resultado)
    print("Tu peso en " + planeta + " es de " + resultado + "kg")


def run():
    print("""
    Bienvenid@ al programa para calcular tu peso en otros planetas 🪐
    1. Mercurio
    2. Venus
    3. Aquí estás
    4. Marte
    5. Júpiter
    6. Saturno
    7. Urano 
    8. Neptuno
    """)
    peso = int(input("¿Cuánto pesas? (En kilogramos terrestres): "))
    eleccion = int(input("Escoge un planeta con su respectivo número (1, 2, 3, 4, 5, 6, 7, 8): "))
    if eleccion == 1:
        gravedad(peso, 2.65, "Mercurio")
    elif eleccion == 2:
        gravedad(peso, 1.1, "Venus")
    elif eleccion == 3:
        gravedad(peso, 1, "Tierra")
    elif eleccion == 4:
        gravedad(peso, 2.6, "Marte")
    elif eleccion == 5:
        gravedad(peso, .39, "Júpiter")
    elif eleccion == 6:
        gravedad(peso, .93, "Saturno")
    elif eleccion == 7:
        gravedad(peso, 1.1, "Urano")
    elif eleccion == 8:
        gravedad(peso, .88, "Neptuno")
    else:
        print("Por favor escribe una opción válida")


if __name__ == '__main__':
    run()