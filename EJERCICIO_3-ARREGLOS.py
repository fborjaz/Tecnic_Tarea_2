# Solicitar al usuario ingresar una cadena de texto
Lv_Cadena = input("Ingrese una cadena de texto: ");

# Solicitar al usuario ingresar un carácter a buscar
Lv_CaracterBuscar = input("Ingrese un carácter a buscar: ");

# Inicializar el contador
Ln_Cantidad = 0;

# Recorrer la cadena de texto
for char in Lv_Cadena:
    # Verificar si el carácter coincide con el carácter buscado
    if char == Lv_CaracterBuscar:
        Ln_Cantidad += 1;

# Imprimir la cantidad de veces que aparece el carácter
print("El carácter", Lv_CaracterBuscar, "aparece", Ln_Cantidad, "veces en la cadena.");
