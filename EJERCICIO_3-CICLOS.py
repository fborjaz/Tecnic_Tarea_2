# Programa de Cálculo de Factorial

# Imprimir encabezado
print("***** Cálculo de Factorial *****");

# Solicitar al usuario que ingrese un número entero positivo
Ln_Numero = int(input("Ingrese un número entero positivo: "));

# Verificar si el número ingresado es válido
if Ln_Numero < 0:
    print("El número ingresado no es válido. Debe ser un número entero positivo.");
else:
    # Calcular el factorial utilizando el bucle while
    Ln_Factorial = 1;
    Ln_Contador = 1;
    
    while Ln_Contador <= Ln_Numero:
        Ln_Factorial *= Ln_Contador;
        Ln_Contador += 1;
    
    # Mostrar el resultado del factorial
    print("El factorial de", Ln_Numero, "es:", Ln_Factorial);


