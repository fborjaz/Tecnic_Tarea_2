# Imprimir encabezado
print("***** Comparación de Números *****");

# Declarar y asignar valor inicial a las variables locales
Ln_Valor1 = 0;
Ln_Valor2 = 0;

# Solicitar al usuario que ingrese el primer valor
print("Ingrese el primer valor:");
Ln_Valor1 = int(input());

# Solicitar al usuario que ingrese el segundo valor
print("Ingrese el segundo valor:");
Ln_Valor2 = int(input());

# Comparar los valores utilizando la sentencia if
if Ln_Valor1 > Ln_Valor2:
    print("El primer valor es mayor que el segundo valor.");
elif Ln_Valor1 < Ln_Valor2:
    print("El segundo valor es mayor que el primer valor.");
else:
    print("Ambos valores son iguales.");



