#Inicio
# Bienvenida al programa e inicio de simulacion para un sistema de captación pluvial
print(f"\nBienvenid@, nuestro sistema busca transformar el reciclaje de PET y HDPE como una propuesta sustentable y\n"
    f"sostenible para captar y reutilizar el agua de la lluvia dentro de la Universidad Nacional Rosario Castellanos.\n")
print(f"Pasos para la captación de agua pluvial.")
print(f"Requerimos recoleccion de plasticos que seran reutilizados para armados de modulos de almacenamiento\n"
    f"y contruir el sistema de captación con demas materiales necesarios.\n")

# Declaracion de variables y funciones
print("Materiales requeridos\n")
material =(f"1.-PET suficiente\n"   #Lista de materiales que se requieren guardado en una variable
    f"2.-Canaletas\n"
    f"3.-Filtro primario (malla o tela)\n"
    f"4.-Tubo de bajada\n"
    f"5.-Filtro secundario (arena, grava, carbón)\n"
    f"6.-Depósito para almacenamiento\n"
    f"7.-Llave de salida\n"
    f"8.-Tornillos, alambre, cinta\n"
    f"9.-Manguera\n")
print(material) # Se llama la variable material con uso de print

creacion =(f"1.-Colocar una canaleta en el borde del techo para recolectar el agua de la lluvia\n"  # Serie de pasos a seguir guardado en una variable
    f"2.-Conectar la canaleta a un tubo o embudo inicial que dirija el agua hacia la pared\n"
    f"3.-Fijar botellas PET cortadas (en forma de canal o media caña) a lo largo de la pared, formando una bajada continua\n"
    f"4.-Unir las botellas con cinta resistente, tornillos o alambre, sobre una estructura de soporte (rejilla, madera reciclada\n"
    f"5.-Al final del canal, instalar un filtro casero con capas de grava, arena y carbón activado dentro de una botella cortada\n"
    f"6.-El agua filtrada cae directamente en un tinaco o depósito reciclado con tapa y válvula de salida.\n")

# Datos obtenidos para calcular el area, volumen en en la UNRC Chalco para una simulación mas especifica
medida_enfrente = 44.33 # m
medida_atras = 46.7 # m
medida_lado_izquierdo = 94.37 # m
medida_lado_derecho = 94.48 # m
area = (((medida_enfrente + medida_atras) / 2) * ((medida_lado_izquierdo + medida_lado_derecho) / 2)) # m2
lluvia_anual_chalco = 583.3 # mm anual historico de lluvia en Chalco
lluvia_anual = lluvia_anual_chalco / 1000 # Convertir mm a m3
coeficiente = 0.9 # ks
volumen = area * lluvia_anual * coeficiente # m3 volumen anual utilizable de agua pluvial sin descarte
descarte_mm_valor = 5 / 1000  # Descarte de 5 mm en metros

# Función para la verificación de material reunido para contruir el sistema de captación
print("Verificar si contamos con los materiales para captación de agua pluvial...")
def verificar_material():
    while True:
        material_respuesta = input(f"¿Tienes todos los materiales? (Si/No)\n") 
        if material_respuesta == 'si' or material_respuesta == 'si':
            print("\n¡Genial! ¡Tienes todos los materiales necesarios!\n")
            print("Como siguiente paso es crear el sistema de captación de agua pluvial con los materiales reunidos.")
            print("Pasos a seguir:\n")
            print(creacion) # Se llama la variable creacion con uso de print
            verificar_pasos_completados() # Función activada e inicio de esta
            break #Termina el bucle actual
        elif material_respuesta == 'no':
            print(f"\n¡Revisa que materiales requeridos te hacen falta para crear el sistema!\n")
            print(f'"Sin materiales no hay sistema de captacion pluvial"')            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual 

# Función para la verificacion de contrucción del sistema de captación de agua conforme a los pasos dados
def verificar_pasos_completados():
    while True:
        pasos_completados = input(f"¿Se completo con exito la pasos para creación del sistema de captación de agua pluvial? (Si/No)\n")
        if pasos_completados == 'si' or pasos_completados == 'si':
            print("\n¡Genial! ¡Tienes un sistema de captación de agua pluvia listo para funcionar!\n")
            calcular_volumen_area() # Función activada e inicio de esta
            break #Termina el bucle actual
        elif pasos_completados == 'no':
            print(f"\nSistema de captacion de agua pluvial no contruido.")
            print(f'"Sin infraestructura no hay sistema de captacion pluvial"')            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual


# Funcion para el calcular un porcentaje del area y volumen de agua pluvial que se puede captar de la UNRC Chalco      
def calcular_volumen_area():
    print("\nAhora veremos el area y volumen de agua pluvial que se puede captar en la UNRC Chalco.")
    print(f"   Area total de superficie de la UNRC Chalco es de: {area: .2f} m²") # se llama la variable de area m2 de la unidad UNRC
    print(f"   Volumen total que se puede captar es de: {volumen: .2f} M³\n") # se llama la variable del volumen calculado 
    
    while True:
        print("Ahora ingrese el porcentaje de area de superficie a captar.") 
        area_seleccionado = float(input("Ingrese el porcentaje de área de superficie a captar (ej. 5 para 5%): "))
        # Operacion de calculo de area y volumen con el porcentaje ingresado
        if 0 < area_seleccionado <= 100:
            area_captada = area * (area_seleccionado / 100) # m2
            volumen_modificado = area_captada * lluvia_anual * coeficiente # v =a*p*ks
            print(f"\nUtilizando un {area_seleccionado}% del area de la UNRC obtendriamos: {area_captada:.2f} m² = {volumen_modificado:.2f} m³ de agua captada\n")
            # Función activada e inicio de esta ademas de llamar variables
            calcular_capacidad_pet(area_captada=area_captada, volumen_piloto=volumen_modificado, porcentaje_piloto=area_seleccionado)
            break
        else:
            print("Porcentaje debe estar entre 0 y 100.")
            continue # Vuelve a iniciar el ciclo actual

# Funcion para el calculo aproximado de almacenamiento de agua pluvial y lladmado de variables de otra funcion
def calcular_capacidad_pet(area_captada, volumen_piloto, porcentaje_piloto):
    print("Ahora veremos cuantos litros de capacidad obtendremos de acuerdo al tamaño de botella utilizado y parte del area de la UNRC Chalco, ingrese los datos.")   
    print("\nOpciones de módulos para almacenamiento con PET:\n")
    print("1. Botellas de 2.5 Litros.")
    print("2. Botellas de 3 Litros.")   
    while True:       # Bucle para seleccionar tamaño de botella y numero de modulos
        tamaño_botella = input("Seleccione el tipo de botella usado (1 o 2): ")
        num_modulos = int(input("Ingrese el número total de botellas interconectados: "))
        if tamaño_botella == '1' or tamaño_botella =='1':  # Botellas de 2.75 litros por botella PET
            capacidad_litros = 0.0
            capacidad_litros = num_modulos * 2.75
        elif tamaño_botella == '2':  # Botellas de 3 litros por botella PET
            capacidad_litros = 0.0
            capacidad_litros = num_modulos * 3
        else:
            print("\nOpción inválida.\nSolo ingresa 1 o 2.")
            continue # Vuelve a iniciar el ciclo actual      
        capacidad_final = capacidad_litros 
        capacidad_m3 = capacidad_final / 1000  # Convertir litros a m3
        volumen_estimado = volumen_piloto /( capacidad_final/100)        
        print(f"\nDatos de Capacidad del Sistema de captación de agua pluvial:")
        print(f"   Botellas utilizados: {num_modulos}") 
        print(f"   Capacidad total estimado: {capacidad_final} litros.")
        print(f"\n¡Genial! ¡Tienes un sistema con una capacidad de {capacidad_final} litros ({capacidad_m3} m³) para almacenamiento de agua pluvial!\n")
        print(f'**Como recomendación del sistema de captación construido y el porcentaje de area seleccionado y aprovechar los {volumen_piloto:.2f}m³ que se puede captar se necesitan aproximadamente de {volumen_estimado: .0f} modulos para ese {porcentaje_piloto: .0f}% de superficie disponible.**\n')
        
        verificar_descarte(volumen_piloto=volumen_piloto, area_captada=area_captada, capacidad_m3=capacidad_m3)  # Función activada e inicio de esta
        break

#Funcion para verificar primer descarte de lluvia para limpieza del techo
def verificar_descarte(volumen_piloto, area_captada, capacidad_m3):
    while True: 
        area_deseado = area_captada * descarte_mm_valor # m3 calculo modificado para el primer descarte de lluvia
        descarte_lluvia = volumen_piloto - area_deseado # m3 volumen utilizable con descarte de lluvia
         # Calculo del porcentaje de capacidad del sistema construido con respecto al volumen utilizable con descarte
        tienes_pocentaje = capacidad_m3 / descarte_lluvia * 100
        descarte_respuesta = input(f"¿Desea considerar el primer descarte de lluvia de 5 mm para limpieza del techo? (Si/No)\n")
        if descarte_respuesta == 'si' or descarte_respuesta == 'si':
            print(f"\nConsiderando un primer lavado del techo con 5 mm de lluvia, el volumen útil de captación pluvial es de {descarte_lluvia:.2f} m³.")
            print(f"Actualmente, el sistema de almacenamiento construido tiene una capacidad de {capacidad_m3:.2f} m³ para una superficie de {area_captada:.2f}m².\n")
            print(f'"El primer descarte de lluvia ayuda a mantener el sistema limpio y eficiente cada vez que llueve"')
            print(f"      ¡Tienes aproximadamente {tienes_pocentaje:.2f}% del volumen captable.!\n")

        elif descarte_respuesta == 'no':
            print(f"\nNo se considerando un primer lavado del techo con 5 mm de lluvia, el volumen útil de captación pluvial es de {volumen_piloto:.2f} m³\n")
            print(f"Actualmente, el sistema de almacenamiento construido tiene una capacidad de {capacidad_m3:.2f} m³ para una superficie de {area_captada:.2f}m².\n")
            print(f'"El primer descarte de lluvia ayuda a mantener el sistema limpio y eficiente cada vez que llueve"')
            print(f"     ¡Tienes aproximadamente {tienes_pocentaje:.2f}% del volumen captable.!\n")      
            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.") 
            continue # Vuelve a iniciar el ciclo actual
        verificar_lluvia() # Función activada e inicio de esta
        break #Termina el bucle actual

# Funcion para verificar si llueve y el sistema de captación pluvial funciona para monitorear
def verificar_lluvia():
    while True: 
        print("Finalmente para que funcione el sistema de captacion pluvial y empezar a monitorear confirmar si llueve.")
        lluvia = input(f"¿Esta lloviendo en la UNRC? (Si/No)\n")
        if lluvia == 'si' or lluvia == 'si': 
            print(f"\nEl sistema se activa...\n\n"
            f"El agua de lluvia es dirigida desde el techo a través de las canaletas hacia las botellas PET ensambladas en la pared.\n"
            f"El agua pasa por el filtro primario que retiene hojas y residuos grandes.\n"
            f"El agua continúa su camino a través del tubo de bajada hacia el filtro secundario que purifica el agua.\n"      
            f"¡Genial! ¡El agua limpia se almacena en el deposito listo para su uso!\n\n"
            f"El agua recolectada se podria usar para:\n"
            f"Riego de plantas, Limpeza de salones y patio, Uso sanitario\n\n"
            f"Se debe dar mantenimiento al sistema; monitorearlo, limpiarlo, cambiar filtros, etc\n"
            f'"Condicion sana, buena eficiencia"')
                                 
            break #Termina el bucle actual
        elif lluvia == 'no':
            print(f"\nEsperar a que llueva y poder monitorear.\n")
            print(f'"Sin lluvia no hay recolección y monitoreo"')
            break #Termina el bucle actual          
        else:
            print("\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual
verificar_material() # Función activada e inicio de esta
# Fin
