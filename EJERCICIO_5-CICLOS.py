# Programa de Conteo Regresivo

# Solicitar al usuario que ingrese un número
Ln_Numero = int(input("Ingrese un número: "));

# Verificar si el número es positivo
if Ln_Numero > 0:
    # Iniciar el contador
    Ln_Contador = Ln_Numero;

    # Realizar el conteo regresivo utilizando el bucle while
    while Ln_Contador > 0:
        # Imprimir el número actual
        print(Ln_Contador);

        # Disminuir el contador en 1
        Ln_Contador -= 1;

    # Utilizar la sentencia for para imprimir "¡Feliz Año Nuevo!" 3 veces
    for _ in range(3):
        print("¡Feliz Año Nuevo!");

else:
    print("El número ingresado debe ser positivo.");
