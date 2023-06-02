# Programa de Generación de Números Pares

# Imprimir encabezado
print("***** Generación de Números Pares *****");

# Declarar y asignar valor inicial a la variable local
Ln_LimiteSuperior = 0;

# Solicitar al usuario que ingrese el límite superior
print("Ingrese el límite superior:");
Ln_LimiteSuperior = int(input());

# Utilizar la sentencia if para verificar si el límite superior es mayor que 0
if Ln_LimiteSuperior > 0:
    print("Números pares del 1 al", Ln_LimiteSuperior, ":");

    # Utilizar la sentencia while para generar los números pares
    contador = 1;
    while contador <= Ln_LimiteSuperior:
        if contador % 2 == 0:
            print(contador);
        contador += 1;

    # Utilizar la sentencia for para generar los números pares de forma alternativa
    print("Números pares (alternativa):");
    for i in range(2, Ln_LimiteSuperior + 1, 2):
        print(i);
else:
    print("El límite superior debe ser mayor que 0.");
