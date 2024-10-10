def areaRectangulo (base, altura):
    area = base * altura;
    return area;

base = float(input("Introduce la base del rectangulo: "));
altura = float(input("Introduce la altura del rectangulo: "));

print("El area del rectangulo es: ", areaRectangulo(base, altura));
