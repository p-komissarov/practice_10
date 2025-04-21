A = float(input("Введите высоту отверстия (в дм): "))
B = float(input("Введите ширину отверстия (в дм): "))

C = float(input("Введите первую сторону кирпича (в дм): "))
D = float(input("Введите вторую сторону кирпича (в дм): "))
E = float(input("Введите третью сторону кирпича (в дм): "))

can_pass = (
    (C <= A and D <= B) or (C <= B and D <= A) or
    (C <= A and E <= B) or (C <= B and E <= A) or
    (D <= A and E <= B) or (D <= B and E <= A)
)

if can_pass:
    print("Бармалей может выбрасывать кирпичи через отверстие.")
else:
    print("Кирпичи не пролезают.")