board = [['?' for _ in range(3)] for _ in range(3)]
for row in board:
    for col in row:
        print(col, end=" | ")

    print()
    print("-----------")
