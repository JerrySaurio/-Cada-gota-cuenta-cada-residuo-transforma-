# -------------------------------------------------------------
# Sistema optimizado de captación pluvial con PET (SIN LIBRERÍAS)
# Versión A: totalmente funcional, robusta y 100% Python puro.
# -------------------------------------------------------------

# ---------- Utilidades ----------
def pedir_si_no(texto):
    """Pide una respuesta 'si' o 'no' y la valida."""
    while True:
        r = input(texto + " [Si/No]: ").strip().lower()
        if r in ("si", "s", "sí"):
            return True
        if r in ("no", "n"):
            return False
        print("❌ Respuesta inválida. Por favor escribe 'Si' o 'No'.")

def pedir_float(texto, minimo=None, maximo=None):
    """Pide un número decimal y valida rango."""
    while True:
        val = input(texto + ": ").strip()
        try:
            num = float(val)
        except:
            print("❌ Ingresa un número válido.")
            continue
        if minimo is not None and num < minimo:
            print(f"❌ Debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and num > maximo:
            print(f"❌ Debe ser menor o igual a {maximo}.")
            continue
        return num

def pedir_int(texto, minimo=None, maximo=None):
    """Pide un entero y valida rango."""
    while True:
        val = input(texto + ": ").strip()
        try:
            num = int(val)
        except:
            print("❌ Ingresa un número entero válido.")
            continue
        if minimo is not None and num < minimo:
            print(f"❌ Debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and num > maximo:
            print(f"❌ Debe ser menor o igual a {maximo}.")
            continue
        return num

# ---------- Cálculos ----------
def calcular_area(enfrente, atras, izq, der):
    """Área aproximada usando promedios de lados opuestos."""
    return ((enfrente + atras) / 2) * ((izq + der) / 2)

def calcular_volumen(area_m2, lluvia_mm, coef):
    """Volumen anual capturable en m³."""
    lluvia_m = lluvia_mm / 1000
    return area_m2 * lluvia_m * coef

def primer_descarte(area_m2, mm):
    """Cálculo del volumen del primer descarte en m³."""
    return area_m2 * (mm / 1000)

# ---------- Flujo ----------
def bienvenida():
    print("\nBienvenid@ al sistema de estimación de captación pluvial con PET reciclado.\n")

def mostrar_materiales():
    print("Materiales requeridos:")
    m = [
        "PET suficiente",
        "Canaletas",
        "Filtro primario",
        "Tubo de bajada",
        "Filtro secundario",
        "Depósito o tinaco",
        "Llave de salida",
        "Tornillos / alambre / cinta",
        "Manguera",
    ]
    for i, x in enumerate(m, 1):
        print(f"  {i}. {x}")
    print()

def main():
    bienvenida()
    mostrar_materiales()

    if not pedir_si_no("¿Ya tienes todos los materiales?"):
        print("\nReúne los materiales primero y vuelve a ejecutar el programa.\n")
        return

    # Valores por defecto UNRC Chalco
    usar_def = pedir_si_no("\n¿Deseas usar los valores por defecto de la UNRC Chalco?")
    if usar_def:
        enfrente = 44.33
        atras = 46.70
        izq = 94.37
        der = 94.48
        lluvia_mm = 583.3
        coef = 0.9
    else:
        enfrente = pedir_float("Medida frente (m)", 0.1)
        atras = pedir_float("Medida atrás (m)", 0.1)
        izq = pedir_float("Lado izquierdo (m)", 0.1)
        der = pedir_float("Lado derecho (m)", 0.1)
        lluvia_mm = pedir_float("Lluvia anual (mm)", 0)
        coef = pedir_float("Coeficiente de escorrentía (0-1)", 0, 1)

    area_total = calcular_area(enfrente, atras, izq, der)
    volumen_total = calcular_volumen(area_total, lluvia_mm, coef)

    print(f"\nÁrea total estimada: {area_total:.2f} m²")
    print(f"Volumen anual capturable: {volumen_total:.3f} m³")

    # Porcentaje de área para piloto
    porcentaje = pedir_float("\nIngresa el porcentaje del área que usarás (0-100)", 0.1, 100)
    area_piloto = area_total * (porcentaje / 100)
    volumen_piloto = calcular_volumen(area_piloto, lluvia_mm, coef)

    print(f"\nÁrea utilizada: {area_piloto:.2f} m²")
    print(f"Volumen capturable con esa área: {volumen_piloto:.3f} m³")

    # Elección de botella
    print("\nOpciones de botellas:")
    print("1. 2.5 L")
    print("2. 3.0 L")

    botella_litros = None
    while botella_litros is None:
        op = input("Selecciona (1 o 2): ").strip()
        if op == "1":
            botella_litros = 2.5
        elif op == "2":
            botella_litros = 3.0
        else:
            print("❌ Opción inválida.")

    num = pedir_int("Número de botellas", 1)
    capacidad_l = num * botella_litros
    capacidad_m3 = capacidad_l / 1000

    print(f"\nCapacidad instalada: {capacidad_l:.2f} L ({capacidad_m3:.3f} m³)")

    # Primer descarte
    considerar_descarte = pedir_si_no("\n¿Aplicar primer descarte de 5 mm?")
    if considerar_descarte:
        descarte = primer_descarte(area_piloto, 5)
        print(f"Primer descarte: {descarte:.3f} m³")
    else:
        descarte = 0

    volumen_util = volumen_piloto - descarte
    if volumen_util < 0:
        volumen_util = 0

    print(f"Volumen útil después de descarte: {volumen_util:.3f} m³")

    # % cubierto
    if volumen_util > 0:
        porcentaje_cubierto = (capacidad_m3 / volumen_util) * 100
        print(f"Tu capacidad cubre el {porcentaje_cubierto:.2f}% del volumen útil.")
    else:
        print("No hay volumen útil para almacenar (volumen = 0).")

    # Módulos necesarios sin librerías (calc de 'ceil' manual)
    if botella_litros > 0:
        if volumen_util > 0:
            litros_totales = volumen_util * 1000
            modulos_necesarios = litros_totales // botella_litros
            if litros_totales % botella_litros != 0:
                modulos_necesarios += 1
            print(f"\nMódulos necesarios para almacenar todo el volumen útil: {int(modulos_necesarios)}")
        else:
            print("\nMódulos necesarios: 0")
    else:
        print("\nNo se pudo calcular módulos necesarios.")

    # Simular lluvia
    if pedir_si_no("\n¿Deseas simular si está lloviendo?"):
        if pedir_si_no("¿Está lloviendo ahora en la UNRC?"):
            print("\n🌧️ El sistema se activa y comienza la captación. Agua filtrada → depósito.")
        else:
            print("\n☀️ Sin lluvia. No hay captación en este momento.")

    print("\nFin del proceso. Gracias por usar el sistema.\n")

# Ejecutar programa
main()
