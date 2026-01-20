import pandas as pd
import numpy as np
from Calculo_area_perimetro import area, perimetro

#Inicio
print("\nBienvenid@, nuestro sistema busca transformar el reciclaje de PET y HDPE como una propuesta sustentable y\n"
    "sostenible para captar y reutilizar el agua de la lluvia dentro de la Universidad Nacional Rosario Castellanos.\n")
print("Pasos para la captación de agua pluvial.")
print("Requerimos recoleccion de plasticos que seran reutilizados para armados de modulos de almacenamiento\n","y contruir el sistema de captación con demas materiales necesarios.\n")

# Definimos variables y tuplas
materiales = ["PET suficiente", "Canaletas", "Filtro primario (malla o tela)", "Tubo de bajada",
    "Filtro secundario (arena, grava, carbón)", "Depósito para almacenamiento", "Llave de salida", "Tornillos, alambre, cinta", "Manguera"
] # Lista de materiales
pasos_scall = ["Colocar una canaleta en el borde del techo para recolectar el agua de la lluvia", "Conectar la canaleta a un tubo o embudo inicial que dirija el agua hacia la pared", "Fijar botellas PET cortadas (en forma de canal o media caña) a lo largo de la pared, formando una bajada continua",
    "Unir las botellas con cinta resistente, tornillos o alambre, sobre una estructura de soporte (rejilla, madera reciclada", "Al final del canal, instalar un filtro casero con capas de grava, arena y carbón activado dentro de una botella cortada", "El agua filtrada cae directamente en un tinaco o depósito reciclado con tapa y válvula de salida."
] # Pasos a seguir para la construcción del SCALL



df_mt = pd.DataFrame(materiales, columns=["Material"]) # Creamos el DataFrame
df_mt.index = df_mt.index + 1 # Ajustamos el índice para que empiece en 1 y no en 0
list_materiales = df_mt.to_string(justify='left')
df_pasos = pd.DataFrame(pasos_scall, columns=["Pasos a seguir"]) # Creamos el DataFrame
df_pasos.index = df_pasos.index + 1 # Ajustamos el índice para que empiece en 1 y no en 0
pasos_seguir = df_pasos.to_string(justify='left')

print(f"--- Materiales requeridos ---\n {list_materiales}")
print(f"Área: {area:.3f} m \nPerimetro: {perimetro:.2} m²")

# Función para la verificación de material reunido para contruir el sistema de captación
def verificar_material():
    while True:
        material_respuesta = input(f"¿Tienes todos los materiales? (Si/No)\n") 
        if material_respuesta == 'si' or material_respuesta == 'si':
            print("\n¡Genial! ¡Tienes todos los materiales necesarios!\n")
            print("Como siguiente paso es crear el sistema de captación de agua pluvial con los materiales reunidos.")
            print(f"--- Construir SCALL ---\n {pasos_seguir}")            
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
            # Función activada e inicio de esta
            break #Termina el bucle actual
        elif pasos_completados == 'no':
            print(f"\nSistema de captacion de agua pluvial no contruido.")
            print(f'"Sin infraestructura no hay sistema de captacion pluvial"')            
        else:
            print("\n\n¡Respuesta invalida!\n Solo 'si' o 'no'.")
            continue # Vuelve a iniciar el ciclo actual 


verificar_material()


