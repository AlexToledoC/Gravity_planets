def choice(peso, gravedad, planeta):
    peso_final = (peso * gravedad) / 9.8
    peso_final = round(peso_final, 2)
    peso_final = str(peso_final)
    print("Tu peso en " + planeta + " es " + peso_final + "kg")

    
def run():
    print("""
    Tu peso cambia de acuerdo a la gravedad.
    Este programa es para calcular tu peso en otros planetas 🪐
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
        choice(peso, 3.7, "Mercurio")
    elif eleccion == 2:
        choice(peso, 8.87, "Venus")
    elif eleccion == 3:
        choice(peso, 9.8, "Tierra")
    elif eleccion == 4:
        choice(peso, 3.7, "Marte")
    elif eleccion == 5:
        choice(peso, 24.8, "Júpiter")
    elif eleccion == 6:
        choice(peso, 10.44, "Saturno")
    elif eleccion == 7:
        choice(peso, 8.87, "Urano")
    elif eleccion == 8:
        choice(peso, 11.15, "Neptuno")
    else:
        print("Por favor escribe una opción válida")
    

if __name__ == '__main__':
    run()

    # gravedad_tiera = 9.8 m/s2
    # gravedad_mercurio = 3.7 m/s2
    # gravedad_venus = 8.87 m/s2
    # gravedad_marte = 3.7 m/s2
    # gravedad_jupiter = 24.8 m/s2
    # gravedad_saturno = 10.44 m/s2
    # gravedad_urano = 8.87 m/s2
    # gravedad_neptuno = 11.15 m/s2