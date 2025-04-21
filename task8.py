N = int(input())

if N == 1:
    print(0)
else:
    N -= 1

    if N <= 9:
        print(N)
    elif N <= 9 + 90 * 2:
        N -= 9
        print((N - 1) % 10)
    elif N <= 9 + 90 * 2 + 100 * 3:
        N -= 9 + 90 * 2
        print((N - 1) // 3)