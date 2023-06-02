# Programa de Adivinar un Número

# Imprimir encabezado
print("***** Adivinar un Número *****");

# Declarar y asignar valor inicial a la variable local
Ln_NumeroSecreto = 0;
adivinado = False;

# Generar un número aleatorio entre 1 y 100
import random;
Ln_NumeroSecreto = random.randint(1, 10);

# Solicitar al usuario que adivine el número
print("Adivina el número secreto entre 1 y 10:");

while not adivinado:
    # Leer el intento del usuario
    Ln_Intento = int(input());
    
    # Verificar si el número es igual, mayor o menor al número secreto
    if Ln_Intento == Ln_NumeroSecreto:
        print("¡Felicidades! ¡Adivinaste el número!");
        adivinado = True;
    elif Ln_Intento < Ln_NumeroSecreto:
        print("El número secreto es mayor. Intenta nuevamente:");
    else:
        print("El número secreto es menor. Intenta nuevamente:");
