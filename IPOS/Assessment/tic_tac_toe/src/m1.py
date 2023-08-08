

class Make_A_Board:
    def __init__(self):
        self.grid = None


    def board_grid(self, rows, cols, value = '?'):
        self.grid = [[value for _ in range(cols)] for _ in range(rows)]
        return self.grid

    def board_display(self):

        for row in self.grid:
            for elem in row:
                print(elem, end=' | ')
            print()
            print("-----------")
