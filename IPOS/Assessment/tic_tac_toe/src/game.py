from board import Board
from logic import Test

def game_loop():

    p1 = "X"
    p2 = "O"
    empty = "?"
    # row, column = map(int, input("Enter the size of your board(row,column): ").split(","))
    # board = board_grid(row, column)
    board_maker = Board(3,3)
    board_tester = Test()
    # board = board_maker.board_grid(3,3)
    board_maker.display_board()
    while True:
        player = p1 if sum(row.count(empty) for row in board_maker.grid) % 2 == 1 else p2
        move = input("Next move for player " + player + " (0-8): ")
        if move.isdigit() and 0 <= int(move) <= 8:
            row = int(move) // 3
            col = int(move) % 3
            if board_maker.grid[row][col] == empty:
                board_maker.grid[row][col] = player
            else:
                print("Invalid move, try again.")
                continue
        else:
            print("Invalid move, try again.")
            board_maker.display_board()
            continue

        # board[rw][cl] = player
        board_maker.display_board()
        winner = board_tester.check_for_win(board_maker.grid)
        if winner:
            print("Player", winner, "wins!")
            break
        if board_tester.check_for_tie(board_maker.grid, empty):

            break

if __name__ == "__main__":
    game_loop()


