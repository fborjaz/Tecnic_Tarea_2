# Programa de Contador de Vocales

# Imprimir encabezado
print("***** Contador de Vocales *****");

# Solicitar al usuario que ingrese una palabra
Lv_Palabra = input("Ingrese una palabra: ");

# Inicializar contadores de vocales
Ln_ContadorA = 0;
Ln_ContadorE = 0;
Ln_ContadorI = 0;
Ln_ContadorO = 0;
Ln_ContadorU = 0;

# Iterar sobre cada carácter de la palabra
for letra in Lv_Palabra:
    # Convertir el carácter a minúscula para hacer la comparación
    letra = letra.lower();
    
    # Contar las vocales
    if letra == 'a':
        Ln_ContadorA += 1;
    elif letra == 'e':
        Ln_ContadorE += 1;
    elif letra == 'i':
        Ln_ContadorI += 1;
    elif letra == 'o':
        Ln_ContadorO += 1;
    elif letra == 'u':
        Ln_ContadorU += 1;

# Mostrar los resultados
print("Cantidad de 'a' encontradas:", Ln_ContadorA);
print("Cantidad de 'e' encontradas:", Ln_ContadorE);
print("Cantidad de 'i' encontradas:", Ln_ContadorI);
print("Cantidad de 'o' encontradas:", Ln_ContadorO);
print("Cantidad de 'u' encontradas:", Ln_ContadorU);


