import math

A = float(input("Введите длину покрытия (в метрах): "))
B = float(input("Введите ширину покрытия (в метрах): "))

radius = 6.5
diameter = 2 * radius

diagonal = math.hypot(A, B)

if diagonal <= diameter:
    print("Покрытие можно разместить на арене без обрезки или подгибов.")
else:
    print("Покрытие не помещается на арене целиком.")