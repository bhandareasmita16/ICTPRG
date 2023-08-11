

class Board:
    def __init__(self, rows, cols, value = '?'):

        self.grid = [[value for _ in range(cols)] for _ in range(rows)]


    def display_board(self):

        for row in self.grid:
            for elem in row:
                print(elem, end=' | ')
            print()
            print("-----------")
