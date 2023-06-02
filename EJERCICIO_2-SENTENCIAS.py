# Programa de Verificación de Números Pares e Impares

# Imprimir encabezado
print("***** Verificación de Números Pares e Impares *****");

# Declarar y asignar valor inicial a la variable local
Ln_Numero = 0;

# Solicitar al usuario que ingrese un número
print("Ingrese un número:");
Ln_Numero = int(input());

# Verificar si el número es par o impar utilizando la sentencia if
if Ln_Numero % 2 == 0:
    print("El número ingresado es par.");
else:
    print("El número ingresado es impar.");



