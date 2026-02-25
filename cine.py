import random

# Datos de las películas y requisitos de edad
peliculas = {
    "1": {"titulo": "Avengers: Endgame", "edad_minima": 13},
    "2": {"titulo": "Joker", "edad_minima": 18},
    "3": {"titulo": "Minions: El origen de Gru", "edad_minima": 5}
}

# Precios
precio_base = 24000
precio_descuento = precio_base * 0.5

# Combos
tabla_combos = {
    "1": {"descripcion": "Combo Clásico: 1 Crispetas + 1 Bebida", "precio": 15000, "bebidas": 1},
    "2": {"descripcion": "Combo Pareja: 2 Crispetas + 2 Bebidas", "precio": 25000, "bebidas": 2},
    "3": {"descripcion": "Combo Familiar: 4 Crispetas + 4 Bebidas", "precio": 40000, "bebidas": 4}
}

# Registro
nombre = input("Ingresa tu nombre: ")
print(f"\nHola {nombre}, bienvenido/a a tu cine de Comfiasa!")

# Selección de película
print("\nPelículas disponibles:")
for key, peli in peliculas.items():
    print(f"{key}: {peli['titulo']} (Edad mínima: {peli['edad_minima']} años)")
pelicula_elegida = input("\nElige la película que deseas ver (1, 2, 3): ")

if pelicula_elegida not in peliculas:
    print("Opción no válida. Registro cancelado.")
    exit()

edad_minima_pelicula = peliculas[pelicula_elegida]['edad_minima']
titulo_pelicula = peliculas[pelicula_elegida]['titulo']

# Cantidad de acompañantes
print("\nOpciones de acompañantes:")
print("1: 1 acompañante")
print("2: 2 acompañantes")
print("3: 3 acompañantes")
print("4: Voy a estar solo")

n1 = input("Elige una opción (1, 2, 3, 4): ")

if n1 in ("1", "2", "3", "4"):
    num_personas = int(n1) if n1 != "4" else 0

    # Lista de personas [(nombre, edad)]
    personas = []

    # Registrar usuario principal
    edad_usuario = int(input(f"{nombre}, ¿cuál es tu edad?: "))
    personas.append((nombre, edad_usuario))

    # Registrar acompañantes
    for i in range(num_personas):
        nombre_acomp = input(f"Ingresa el nombre de tu acompañante #{i + 1}: ")
        edad_acomp = int(input(f"{nombre_acomp}, ¿cuál es tu edad?: "))
        personas.append((nombre_acomp, edad_acomp))

    # Verificación de edades
    menores = [persona for persona, edad in personas if edad < edad_minima_pelicula]

    if menores:
        print("\nNo pueden ingresar. Las siguientes personas no cumplen con el requisito de edad para esta película:")
        for persona in menores:
            print(f"- {persona}")
        exit()

    # Elección de asientos (control de asientos ocupados)
    print("\nSelección de asientos (Sala de 20x20):")
    asientos_ocupados = set()
    asientos = []

    for i in range(len(personas)):
        while True:
            try:
                fila = int(input(f"{personas[i][0]}, elige tu fila (1-20): "))
                columna = int(input(f"{personas[i][0]}, elige tu columna (1-20): "))
                if 1 <= fila <= 20 and 1 <= columna <= 20:
                    if (fila, columna) not in asientos_ocupados:
                        asientos.append((fila, columna))
                        asientos_ocupados.add((fila, columna))
                        break
                    else:
                        print("Ese asiento ya está ocupado, elige otro.")
                else:
                    print("Por favor, ingresa un número entre 1 y 20.")
            except ValueError:
                print("Entrada inválida. Ingresa un número.")

    # Consumo de alimentos
    consumir = input("\n¿Deseas consumir algún tipo de alimento? (si/no): ")
    total_combos = 0
    combos_elegidos = []

    if consumir.lower() == "si":
        if num_personas == 3:
            print("\nRecomendación: El Combo Familiar es ideal para grupos de 4 personas.")

        print("\nCarta de Combos:")
        for key, combo in tabla_combos.items():
            print(f"{key}: {combo['descripcion']} - Precio: {combo['precio']} COP")

        while True:
            combo_opcion = input("Elige un combo (1, 2, 3) o escribe (4) para terminar: ")
            if combo_opcion.lower() == "4":
                break
            elif combo_opcion in tabla_combos:
                combos_elegidos.append(combo_opcion)
                total_combos += tabla_combos[combo_opcion]['precio']
            else:
                print("Opción no válida.")

    # Cálculo del total
    # Cálculo del total y registro completo
total_boletos = 0

# Calcular boletos
for persona, edad in personas:
    if edad >= 55:
        total_boletos += precio_descuento
    else:
        total_boletos += precio_base

# Calcular total general
total_general = total_boletos + total_combos

# Crear el registro completo
nrambon = {
    "pelicula": titulo_pelicula,
    "personas": [{"nombre": p, "edad": e} for p, e in personas],
    "asientos": [{"nombre": personas[i][0], "fila": asientos[i][0], "columna": asientos[i][1]} for i in range(len(personas))],
    "combos": [tabla_combos[c]["descripcion"] for c in combos_elegidos],
    "total_boletos": total_boletos,
    "total_combos": total_combos,
    "total_general": total_general
}

# Mostrar resumen de compra
print("\n--- RESUMEN DE COMPRA ---")
print(f"Película: {nrambon['pelicula']}")
print(f"Cantidad de personas: {len(nrambon['personas'])}")
for p in nrambon["personas"]:
    print(f"- {p['nombre']} ({p['edad']} años)")

print("\nAsientos seleccionados:")
for a in nrambon["asientos"]:
    print(f"- {a['nombre']}: Fila {a['fila']}, Columna {a['columna']}")

print("\nCombos adquiridos:")
if nrambon["combos"]:
    for combo in nrambon["combos"]:
        print(f"- {combo}")
else:
    print("- Ninguno")

print(f"\nTotal a pagar: {nrambon['total_general']} COP")

# Dividir el precio
dividir = input("\n¿Deseas dividir el precio entre los asistentes? (si/no): ")
if dividir.lower() == "si":
    por_persona = nrambon["total_general"] / len(personas)
    print(f"Cada persona debe pagar aproximadamente: {round(por_persona, 2)} COP")

# Generar código aleatorio
codigo = str(random.randint(100000, 999999))
print(f"\nTu código de confirmación es: {codigo}")

# Confirmación
confirmacion = input("\nIngresa tu código para revisar tu compra: ")
if confirmacion == codigo:
    print("\n--- REGISTRO COMPLETO ---")
    print(nrambon)
else:
    print("Código incorrecto.")
