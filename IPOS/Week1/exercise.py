p1 = "X"
p2 = "O"
empty = " "
board = [empty] * 9

while True:
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]
    for wc in win_conditions:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != empty:
            print("Player " + player + " wins!")
            exit()

        if empty not in board:
            print("It's a tie!")
            exit()
    player = p1 if board.count(empty) % 2 == 1 else p2
    move = input("Next move for player "+player+"(0-8):")
    if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == empty:
        board[int(move)] = player

    else:
        print("Invalid move, try again.")

