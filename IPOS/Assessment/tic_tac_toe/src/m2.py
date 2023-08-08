
class Test:
    def __init__(self):
        self.board = None

    def check_for_win(self, board):
        win_conditions = [(0, 1, 2), (3, 4, 5),
                          (6, 7, 8), (0, 3, 6),
                          (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        for wc in win_conditions:
            if board[wc[0] // 3][wc[0] % 3] == board[wc[1] // 3][wc[1] % 3] == board[wc[2] // 3][wc[2] % 3] != "?":
                print("Player", board[wc[0] // 3][wc[0] % 3], "wins!")
                exit(0)

    def check_for_tie(self, board, empty):
        for row in board:
            if empty in row:
                return False
        print("It's a tie!")
        return True