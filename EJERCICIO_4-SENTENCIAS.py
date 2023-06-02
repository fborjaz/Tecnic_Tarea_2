# Programa de Suma de Números

# Imprimir encabezado
print("***** Suma de Números *****");

# Declarar y asignar valor inicial a la variable local
Ln_CantidadNumeros = 0;
Ln_SumaTotal = 0;

# Solicitar al usuario que ingrese la cantidad de números a sumar
print("Ingrese la cantidad de números a sumar:");
Ln_CantidadNumeros = int(input());

# Utilizar la sentencia for para iterar y sumar los números
for i in range(Ln_CantidadNumeros):
    numero = float(input("Ingrese el número {}: ".format(i+1)));
    Ln_SumaTotal += numero;

# Imprimir la suma total de los números ingresados
print("La suma total de los números es:", Ln_SumaTotal);
