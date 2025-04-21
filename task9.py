import math

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if d > r1 + r2:
    print("Окружности лежат одна вне другой, не касаясь")
elif d == r1 + r2:
    print("Окружности имеют внешнее касание")
elif r1 - r2 < d < r1 + r2:
    print("Окружности пересекаются")
elif d == abs(r1 - r2):
    print("Окружности имеют внутреннее касание")
elif d < abs(r1 - r2):
    print("Одна окружность лежит внутри другой, не касаясь")