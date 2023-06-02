# Solicitar al usuario la cantidad de números a ingresar
Ln_CantidadNumeros = int(input("Ingrese la cantidad de números a ingresar: "))

# Definir una lista para almacenar los números
Ln_Numeros = []

# Solicitar al usuario ingresar los números
for i in range(Ln_CantidadNumeros):
    num = float(input("Ingrese el número " + str(i+1) + ": "))
    Ln_Numeros.append(num)

# Inicializar la variable para almacenar el número máximo
Ld_Maximo = Ln_Numeros[0]  # Asignar el primer número como máximo

# Encontrar el número máximo
for num in Ln_Numeros:
    if num > Ld_Maximo:
        Ld_Maximo = num

# Imprimir el número máximo
print("El número máximo es:", Ld_Maximo)
