move = input()
start, end = move.split('-')
start_col = ord(start[0]) - ord('a')
start_row = int(start[1])
end_col = ord(end[0]) - ord('a')
end_row = int(end[1])

if (abs(start_col - end_col) == 2 and abs(start_row - end_row) == 1) or (abs(start_col - end_col) == 1 and abs(start_row - end_row) == 2):
    print("Верно")
else:
    print("Неверно")