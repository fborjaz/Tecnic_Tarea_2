# Solicitar al usuario la cantidad de números de la secuencia a generar
Ln_CantidadNumeros = int(input("Ingrese la cantidad de números de la secuencia de Fibonacci a generar: "));

# Declarar el arreglo para almacenar los números de la secuencia
Ln_SecuenciaFibonacci = [0, 1];  # Los primeros dos números de la secuencia

# Generar los números de la secuencia utilizando un bucle
for i in range(2, Ln_CantidadNumeros):
    # Calcular el siguiente número sumando los dos anteriores
    num = Ln_SecuenciaFibonacci[i-1] + Ln_SecuenciaFibonacci[i-2];
    Ln_SecuenciaFibonacci.append(num);  # Agregar el número al arreglo

# Mostrar los números de la secuencia de Fibonacci
print("Secuencia de Fibonacci:");
for num in Ln_SecuenciaFibonacci:
    print(num, end=" ");
