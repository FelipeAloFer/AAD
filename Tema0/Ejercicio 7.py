num = int(input("Escribe un número del 1 al 7: "))
while num < 1 or num > 7:
    num = int(input("Escribe un número del 1 al 7: "))

if num == 1:
    print("Lunes");
elif num == 2:
    print("Martes");
elif num == 3:
    print("Miércoles");
elif num == 4:
    print("Jueves");
elif num == 5:
    print("Viernes");
elif num == 6:
    print("Sábado");
else:
    print("Domingo");
