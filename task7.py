K = int(input())

for x in range(K // 5 + 1):
    if (K - 5 * x) % 7 == 0:
        print("Да")
        break
else:
    print("Нет")