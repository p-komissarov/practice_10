cell = input().strip()
column = cell[0]
row = int(cell[1])

if (ord(column) - ord('a') + row) % 2 == 0:
    print("Белый")
else:
    print("Черный")