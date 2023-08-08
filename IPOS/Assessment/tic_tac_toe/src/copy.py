def board_grid(rows, cols, value="?"):
    grid = [[value for _ in range(cols)] for _ in range(rows)]
    return grid

def board_display(grid):
    for row in grid:
        for elem in row:
            print(elem, end=' | ')
        print()
        print("-----------")

def check_for_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5),
                      (6, 7, 8), (0, 3, 6),
                      (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for wc in win_conditions:
        i, j, k = wc
        if board[i // 3][i % 3] == board[j // 3][j % 3] == board[k // 3][k % 3] != "?":
            print("Player", board[i // 3][i % 3], "wins!")
            return True
    return False

def check_for_tie(board, empty):
    for row in board:
        if empty in row:
            return False
    return True

while True:
    p1 = "X"
    p2 = "O"
    empty = "?"
    board = board_grid(3, 3)
    board_display(board)

    for _ in range(9):  # Maximum 9 moves, the game ends in a tie at most
        player = p1 if sum(row.count(empty) for row in board) % 2 == 1 else p2
        move = input("Next move for player " + player + " (0-8): ")

        if move.isdigit() and 0 <= int(move) <= 8:
            rw = int(move) // 3
            cl = int(move) % 3
            if board[rw][cl] == empty:
                board[rw][cl] = player
            else:
                print("Invalid move, the position is already taken.")
                continue
        else:
            print("Invalid move, try again.")
            continue

        board_display(board)
        if check_for_win(board):
            break

    if check_for_tie(board, empty):
        print("It's a tie!")
    break


def board_grid(rows, cols, value="?"):
    grid = [[value for _ in range(cols)] for _ in range(rows)]
    return grid

def board_display(grid):
    for row in grid:
        for elem in row:
            print(elem, end=' | ')
        print()
        print("-----------")

def check_for_win(board):
    rows = len(board)
    cols = len(board[0])

    win_conditions = []
    # Check rows
    for i in range(rows):
        win_conditions.append(tuple(i * cols + j for j in range(cols)))

    # Check columns
    for j in range(cols):
        win_conditions.append(tuple(i * cols + j for i in range(rows)))

    # Check diagonals
    if rows == cols:
        win_conditions.append(tuple(i * cols + i for i in range(rows)))  # Main diagonal
        win_conditions.append(tuple(i * cols + (cols - i - 1) for i in range(rows)))  # Anti-diagonal

    for wc in win_conditions:
        i, j, k = wc
        if board[i // cols][i % cols] == board[j // cols][j % cols] == board[k // cols][k % cols] != "?":
            print("Player", board[i // cols][i % cols], "wins!")
            return True
    return False

def check_for_tie(board, empty):
    for row in board:
        if empty in row:
            return False
    return True

row, column = map(int, input("Enter the size of your board (row,column): ").split(","))
empty = "?"
board = board_grid(row, column)
board_display(board)

while True:
    player = "X" if sum(row.count(empty) for row in board) % 2 == 1 else "O"
    move = input("Next move for player " + player + " (0-{}): ".format(row*column - 1))

    if move.isdigit() and 0 <= int(move) < row * column:
        rw = int(move) // column
        cl = int(move) % column
        if board[rw][cl] == empty:
            board[rw][cl] = player
        else:
            print("Invalid move, the position is already taken.")
            continue
    else:
        print("Invalid move, try again.")
        board_display(board)
        if check_for_win(board):
            print("Player", player, "wins!")
        continue

    board_display(board)
    if check_for_win(board):
        break

    if check_for_tie(board, empty):
        print("It's a tie!")
        break
