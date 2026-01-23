import Motor_SCALL_v1

def bienvenida(): #Presentacion del sistema
    print(f"\n{'='*100}")
    print("\nBienvenid@, nuestro sistema busca transformar el reciclaje de PET y HDPE como una propuesta sustentable y\n"
          "sostenible para captar y reutilizar el agua de la lluvia dentro de la Universidad Nacional Rosario Castellanos.\n")
    print(f"{'='*100}\n")
    print(f"Requerimos recoleccion de plasticos que seran reutilizados para armados de modulos de \nalmacenamiento y contruir el sistema de captación con demas materiales necesarios.\n {Motor_SCALL_v1.texto_materiales}")
    print("Verificar si contamos con los materiales para captación de agua pluvial...")

def verificacion(): 
    while True: # Función para la verificación de material reunido para contruir el sistema de captación
        resp_material = input("¿Tienes todos los materiales? (Si/No): ").lower()
        if resp_material == 'si' or resp_material == 'si':
            print("\n¡Genial! ¡Tienes todos los materiales necesarios!\n")
            print(f"Como siguiente paso es crear el sistema de captación de agua pluvial con los materiales reunidos.\n{Motor_SCALL_v1.texto_pasos}") # Se llama la variable creacion con uso de print
            break #Termina el bucle actual
        elif resp_material == 'no':
            print("\n¡Revisa que materiales requeridos te hacen falta para crear el sistema!\n", "Sin materiales no hay sistema de captacion pluvial")          
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")


    while True: # Función para la verificacion de contrucción del sistema de captación de agua conforme a los pasos dados
        exito_pasos = input("\n¿Se completo con exito la construcción del scall? (Si/No): ").lower()
        if exito_pasos == 'si' or exito_pasos == 'si':
            print("\n¡Genial! ¡Tienes un sistema de captación de agua pluvial listo para funcionar!\n")
            return True
        elif exito_pasos == 'no':
            print("\nSistema de captación de agua pluvial no contruido.", "Sin infraestructura no hay sistema de captacion pluvial")
            return False        

def ejecutar_simulacion():
    bienvenida()

    if not verificacion():
        return # Detiene el programa si no hay sistema
    
    print("\nAhora veremos el area y volumen de agua pluvial que se puede captar en la UNRC Chalco.")
    print(f"   Area total de superficie de la UNRC Chalco es de: {Motor_SCALL_v1.area:.2f} m²") # se llama la variable de area m2 de la unidad UNRC
    print(f"   Volumen total que se puede captar es de: {Motor_SCALL_v1.volumen_captable:.2f} M³\n") # se llama la variable del volumen calculado 
    
    while True: # Selección de superficie
        print("Ahora ingrese el porcentaje de area de superficie a captar.") 
        porcentaje = float(input("Ingrese % de área a captar (0-100): "))
        # Operacion de calculo de area y volumen con el porcentaje ingresado
        if 0 < porcentaje <= 100:
            area_c, vol_c = Motor_SCALL_v1.calcular_volumen_captable(porcentaje) # v =a*p*ks
            print(f"\nUtilizando un {porcentaje}% del area de la UNRC obtendriamos: {area_c:.2f} m² = {vol_c:.2f} m³ de agua captada\n")
            break
        else:
            print("Porcentaje debe estar entre 0 y 100.")
            continue # Vuelve a iniciar el ciclo actual

    print("Ahora veremos cuantos litros de capacidad obtendremos de acuerdo al tamaño de botella utilizado y parte del area de la UNRC Chalco, ingrese los datos.")   
    print("\nOpciones de módulos para almacenamiento con PET:\n")
    print("1. Botellas 2.5L | 2. Botellas 3L")
    while True: # Almacenamiento PET
        tipo = input("Seleccione (1/2): ")
        cant = int(input("Cantidad de botellas interconectadas: "))
        if tipo == '1' or tipo =='1':  # Botellas de 2.75 litros por botella PET
            capacidad_litros = 0.0
            capacidad_litros = cant * 2.5
        elif tipo == '2':  # Botellas de 3 litros por botella PET
            capacidad_litros = 0.0
            capacidad_litros = cant * 3
        else:
            print("\nOpción inválida.\nSolo ingresa 1 o 2.")
            continue # Vuelve a iniciar el ciclo actual  
        capacidad_final = capacidad_litros
        litros, m3_almacen = Motor_SCALL_v1.calcular_capacidad_almacenamiento(tipo, cant)
        num_modulos = vol_c /( capacidad_final/100) # Aproximación de modulos necesarios para scall de acuerdo al area     
        print(f"\nDatos de Capacidad del Sistema de captación de agua pluvial:")
        print(f"   Botellas utilizados: {cant}")
        print(f"   Capacidad total estimado: {litros} litros.")
        print(f"\n¡Genial! ¡Tienes un sistema con una capacidad de {litros:.0f} litros ({m3_almacen} m³) para almacenamiento de agua pluvial!\n")
        print(f'**Como recomendación del sistema de captación construido y el porcentaje de area seleccionado y aprovechar los {vol_c:.2f}m³ que se puede captar se necesitan aproximadamente de {num_modulos: .0f} modulos para ese {porcentaje: .0f}% de superficie disponible.**\n')
        break

    while True: # Descarte de lluvia para limpieza del techo
        descarte_sn = input("\n¿Considerar descarte de 5mm para limpieza? (Si/No): ").lower()
        util = Motor_SCALL_v1.calcular_descarte(area_c, vol_c)
        tienes_porcentaje = m3_almacen / util * 100 # Calculo del porcentaje de capacidad del sistema construido con respecto al volumen utilizable con descarte
        if descarte_sn == 'si' or descarte_sn == 'si':
            print(f"\nConsiderando un primer lavado del techo con 5 mm de lluvia, el volumen útil de captación pluvial es de {util:.2f} m³.")
            print(f"Actualmente, el sistema de almacenamiento construido tiene una capacidad de {m3_almacen:.2f} m³ para una superficie de {area_c:.2f}m².\n")
            print(f'"El primer descarte de lluvia ayuda a mantener el sistema limpio y eficiente cada vez que llueve"')
            print(f"      ¡Tienes aproximadamente {tienes_porcentaje:.0f} % del volumen captable.!\n")
            print(f"Volumen útil post-limpieza: {util:.2f} m³")
        elif descarte_sn == 'no':
            print(f"\nNo se considerando un primer lavado del techo con 5 mm de lluvia, el volumen útil de captación pluvial es de {vol_c:.2f} m³\n")
            print(f"Actualmente, el sistema de almacenamiento construido tiene una capacidad de {m3_almacen:.2f} m³ para una superficie de {area_c:.2f}m².\n")
            print(f'"El primer descarte de lluvia ayuda a mantener el sistema limpio y eficiente cada vez que llueve"')
            print(f"     ¡Tienes aproximadamente {tienes_porcentaje:.2f}% del volumen captable.!\n")      
            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual
        break #Termina el bucle actual

    while True: # Simulación Final
        print("Finalmente para que funcione el sistema de captacion pluvial y empezar a monitorear confirmar si llueve.")
        lluvia = input(f"¿Esta lloviendo en la UNRC? (Si/No): ").lower()
        if lluvia == 'si' or lluvia == 'si':
            print(f"\nEl sistema se activa...\n\n{Motor_SCALL_v1.activado}")        
            break #Termina el bucle actual
        elif lluvia == 'no':
            print(f"\nEsperar a que llueva y poder monitorear.\n")
            print(f'"Sin lluvia no hay recolección y monitoreo"')
            break #Termina el bucle actual          
        else:
            print("\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual
if __name__ == "__main__":
    ejecutar_simulacion()