# Programa de Contador de Caracteres

# Imprimir encabezado
print("***** Contador de Caracteres *****");

# Declarar y asignar valor inicial a la variable local
Lv_Cadena = '';

# Solicitar al usuario que ingrese una cadena de texto
print("Ingrese una cadena de texto:");
Lv_Cadena = input();

# Inicializar contador de caracteres
Ln_Contador = 0;

# Recorrer la cadena de texto y contar los caracteres
Ln_Indice = 0;
while Ln_Indice < len(Lv_Cadena):
    if Lv_Cadena[Ln_Indice] != ' ':
        Ln_Contador += 1;
    Ln_Indice += 1;

# Mostrar el resultado
print("La cadena de texto tiene", Ln_Contador, "caracteres (sin contar los espacios).");


