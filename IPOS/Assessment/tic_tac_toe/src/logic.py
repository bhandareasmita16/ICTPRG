
class Test:
    def __init__(self):
        self.board = None

    def check_for_win(self, board):
        rev_board = list(zip(*board))
        for row in board:
            unique = set(row)
            if len(unique) == 1 and '?' not in unique:
                # print("Player", unique.pop(), "wins!")
                return unique.pop()
        for row in rev_board:
            rev_unique = set(row)
            if len(rev_unique) == 1 and '?' not in rev_unique:
                # print("Player", rev_unique.pop(), "wins!")
                return rev_unique.pop()
        main_diag = [board[i][i] for i in range(len(board))]
        unique_main_diag = set(main_diag)
        if len(unique_main_diag) == 1 and '?' not in unique_main_diag:
            # print("Player", unique_main_diag.pop(), "wins!")
            return unique_main_diag.pop()
        # Check anti-diagonal (top-right to bottom-left)
        anti_diag = [board[i][len(board) - 1 - i] for i in range(len(board))]
        unique_anti_diag = set(anti_diag)
        if len(unique_anti_diag) == 1 and '?' not in unique_anti_diag:
            # print("Player", unique_anti_diag.pop(), "wins!")
            return unique_anti_diag.pop()
        return False

    def check_for_tie(self, board, empty):
        for row in board:
            if empty in row:
                return False
        # print("It's a tie!")
        return True