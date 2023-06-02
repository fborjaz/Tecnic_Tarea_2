# Solicitar al usuario ingresar los elementos del primer arreglo
Lv_CadenaNumeros1 = input("Ingrese los elementos del primer arreglo separados por espacios: ");

# Convertir la cadena de números en una lista de enteros
Ln_Arreglo1 = list(map(int, Lv_CadenaNumeros1.split()));

# Solicitar al usuario ingresar los elementos del segundo arreglo
Lv_CadenaNumeros2 = input("Ingrese los elementos del segundo arreglo separados por espacios: ");

# Convertir la cadena de números en una lista de enteros
Ln_Arreglo2 = list(map(int, Lv_CadenaNumeros2.split()));

# Verificar si los arreglos tienen la misma longitud
if len(Ln_Arreglo1) != len(Ln_Arreglo2):
    print("Los arreglos deben tener la misma longitud para realizar la suma.");
else:
    # Declarar un arreglo para almacenar la suma
    Ln_Suma = [];

    # Realizar la suma de los elementos correspondientes de ambos arreglos
    for i in range(len(Ln_Arreglo1)):
        suma = Ln_Arreglo1[i] + Ln_Arreglo2[i];
        Ln_Suma.append(suma);

    # Mostrar el resultado de la suma
    print("Resultado de la suma:", Ln_Suma);
