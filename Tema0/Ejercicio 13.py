import random; #Importamos la libreria random

numeros = [];
for x in range(0, 10):
    numeros.append(random.randint(1, 50));
    #Añadimos a la lista un numero random usando el metodo randint de
    #la libreria random y le ponemos los valores 1 y 50 que indican que
    #el numero aleatorio estará entre estos dos valores
    
num = int(input("Adivina un numero de la lista: "));

if num in numeros:
    print("Bingo!!");
    print(numeros);
else:
    print("\nEl numero no esta en la lista\n");
    print(numeros);
