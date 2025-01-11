import random


def adivina_el_numero(x):
    
    print("=====================")
    print(" Bienvenido al juego!")
    print("=====================")
    print("Tenes que adivinar el numero generado por la PC.")
    
    numero_random = random.randint(1, x) # Numero aleatorio entre 1 y x inclusive.
    
    prediccion = 0
    
    while prediccion != numero_random:
        # El usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))
        
        if prediccion < numero_random:
            print("Intenta otra vez. Este numero es muy pequeño.")
        elif prediccion > numero_random:
            print("Intenta otra vez. Este numero es muy grande.")
            
    print(f"Felicitaciones. Adivinaste el numero {numero_random} correctamente")
        
        
adivina_el_numero(10)