import pandas as pd
import numpy as np
from Calculo_area_perimetro import area, perimetro, texto_materiales, texto_pasos, activado, mm_maxima, volumen_captable, volumen_neto, volumen_descarte, calcular_volumen_captable

#Presentacion del sistema
print("\nBienvenid@, nuestro sistema busca transformar el reciclaje de PET y HDPE como una propuesta sustentable y\n"
    "sostenible para captar y reutilizar el agua de la lluvia dentro de la Universidad Nacional Rosario Castellanos.\n")
print("Pasos para la captación de agua pluvial.")
print("Requerimos recoleccion de plasticos que seran reutilizados para armados de modulos de almacenamiento\n",f"y contruir el sistema de captación con demas materiales necesarios.\n {texto_materiales}")

# Función para la verificación de material reunido para contruir el sistema de captación
print("Verificar si contamos con los materiales para captación de agua pluvial...")
def verificar_material():
    while True:
        resp_material = input(f"¿Tienes todos los materiales? (Si/No)\n").lower()
        if resp_material == 'si' or resp_material == 'si':
            print("\n¡Genial! ¡Tienes todos los materiales necesarios!\n")
            print("Como siguiente paso es crear el sistema de captación de agua pluvial con los materiales reunidos.")
            print(f"Pasos a seguir:\n{texto_pasos}") # Se llama la variable creacion con uso de print
            verificar_pasos_completados() # Función activada e inicio de esta
            break #Termina el bucle actual
        elif resp_material == 'no':
            print(f"\n¡Revisa que materiales requeridos te hacen falta para crear el sistema!\n")
            print(f'"Sin materiales no hay sistema de captacion pluvial"')            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual 

# Función para la verificacion de contrucción del sistema de captación de agua conforme a los pasos dados
def verificar_pasos_completados():
    while True:
        exito_pasos = input(f"¿Se completo con exito la pasos para creación del sistema de captación de agua pluvial? (Si/No)\n").lower()
        if exito_pasos == 'si' or exito_pasos == 'si':
            print("\n¡Genial! ¡Tienes un sistema de captación de agua pluvia listo para funcionar!\n")
            calcular_volumen_area() # Función activada e inicio de esta
            break #Termina el bucle actual
        elif exito_pasos == 'no':
            print(f"\nSistema de captacion de agua pluvial no contruido.")
            print(f'"Sin infraestructura no hay sistema de captacion pluvial"')            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual

# Funcion para el calcular un porcentaje del area y volumen de agua pluvial que se puede captar de la UNRC Chalco      
def calcular_volumen_area():
    print("\nAhora veremos el area y volumen de agua pluvial que se puede captar en la UNRC Chalco.\n", f"   Area total de superficie de la UNRC Chalco es de: {area: .2f} m²")
    print(f"   Volumen total que se puede captar es de: {volumen_captable: .2f} M³\n") # se llama la variable del volumen calculado 
    while True:
        print("Ahora ingrese el porcentaje de area de superficie a captar.") 
        area_seleccionado = float(input("Ingrese % de área a captar (0-100): "))
        area_c, vol_c = calcular_volumen_captable(area_seleccionado)
        # Operacion de calculo de area y volumen con el porcentaje ingresado
        if 0 < area_seleccionado <= 100:
            print(f"\nUtilizando el {area_seleccionado}% ({area_c:.2f} m²) de la UNRC se captaria {vol_c:.2f} m³\n")
            calcular_capacidad_pet(area_captada=area_c, volumen_piloto=vol_c, porcentaje_piloto=area_seleccionado) # Función activada e inicio de esta ademas de llamar variables
            break
        else:
            print("Porcentaje debe estar entre 0 y 100.")
            continue # Vuelve a iniciar el ciclo actual

# Funcion para el calculo aproximado de almacenamiento de agua pluvial y lladmado de variables de otra funcion
def calcular_capacidad_pet(area_captada, volumen_piloto, porcentaje_piloto):
    print("Ahora veremos cuantos litros de capacidad obtendremos de acuerdo al tamaño de botella utilizado y parte del area de la UNRC Chalco, ingrese los datos.")   
    print("\nOpciones de módulos para almacenamiento con PET:\n")
    print("1. Botellas 2.5L | 2. Botellas 3L")
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
        area_deseado = area_captada * mm_maxima # m3 calculo modificado para el primer descarte de lluvia
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
            print(f"\nEl sistema se activa...\n\n {activado}")                                 
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

