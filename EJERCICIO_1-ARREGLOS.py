# Solicitar al usuario la cantidad de números a registrar
Ln_CantidadNumeros = int(input("Ingrese la cantidad de números a registrar: "));

# Definir una lista para almacenar los números
Ln_Numeros = [];

# Solicitar al usuario ingresar los números
for i in range(Ln_CantidadNumeros):
    num = int(input("Ingrese el número " + str(i+1) + ": "));
    Ln_Numeros.append(num);

# Inicializar contadores
Ln_CantidadPares = 0;
Ln_CantidadImpares = 0;

# Recorrer la lista de números
for num in Ln_Numeros:
    # Verificar si el número es par o impar
    if num % 2 == 0:
        Ln_CantidadPares += 1;
    else:
        Ln_CantidadImpares += 1;

# Imprimir los resultados
print("Cantidad de números pares:", Ln_CantidadPares);
print("Cantidad de números impares:", Ln_CantidadImpares);
