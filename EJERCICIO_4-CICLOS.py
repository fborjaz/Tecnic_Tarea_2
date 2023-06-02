# Programa de Tablas de Multiplicar

# Imprimir encabezado
print("***** Tablas de Multiplicar *****");

# Solicitar al usuario que ingrese un número entero positivo
Ln_Numero = int(input("Ingrese un número entero positivo: "));

# Verificar si el número ingresado es válido
if Ln_Numero < 1:
    print("El número ingresado no es válido. Debe ser un número entero positivo.");
else:
    # Mostrar las tablas de multiplicar utilizando los bucles for y while
    for i in range(1, Ln_Numero + 1):
        print("Tabla de multiplicar del", i);
        print("------------------------");
        
        contador = 1;
        while contador <= 12:
            resultado = i * contador;
            print(i, "x", contador, "=", resultado);
            contador += 1;
        
        print();  # Línea en blanco entre las tablas de multiplicar

