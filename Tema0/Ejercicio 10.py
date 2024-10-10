def mayorEntre2 (num1, num2):
    if num1 > num2:
        return num1;
    elif num1 < num2:
        return num2;
    else:
        return "Ninguno";

num1 = float(input("Introduce el primer numero: "));
num2 = float(input("Introduce el segundo numero: "));

print("El mayor es:", mayorEntre2(num1, num2));
