from m1 import Make_A_Board
from m2 import Test

def game_loop():

    p1 = "X"
    p2 = "O"
    empty = "?"
    # row, column = map(int, input("Enter the size of your board(row,column): ").split(","))
    # board = board_grid(row, column)
    board_maker = Make_A_Board()
    board_tester = Test()
    board = board_maker.board_grid(3,3)
    board_maker.board_display()
    while True:
        player = p1 if sum(row.count(empty) for row in board) % 2 == 1 else p2
        move = input("Next move for player " + player + " (0-8): ")
        if move.isdigit() and 0 <= int(move) <= 8:
            row = int(move) // 3
            col = int(move) % 3
            if board[row][col] == empty:
                board[row][col] = player
            else:
                print("Invalid move, try again.")
                continue
        else:
            print("Invalid move, try again.")
            board_maker.board_display()
            continue

        # board[rw][cl] = player
        board_maker.board_display()
        board_tester.check_for_win(board)
        if board_tester.check_for_tie(board, empty):
            board_maker.board_display()
            continue


if __name__ == "__main__":
    game_loop()


