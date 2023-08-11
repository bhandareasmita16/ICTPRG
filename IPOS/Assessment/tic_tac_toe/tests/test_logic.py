import unittest
from logic import Test
from board import Board
class Test_logic(unittest.TestCase):
    # def setUp(self):
    #     self.board_tester = Test()
    # def test_check_for_win(self):
    #     game1 = Test()
    #     board1 = [
    #     ['X', 'X', 'X'],
    #     ['O', 'O', '?'],
    #     ['?', '?', '?']
    #      ]
    #
    #     self.assertTrue(game1.check_for_win(board1))
        # assert game1.check_for_win(board1) == True
    def test_board(self):
        b2 = Board(3,3)

        b1 = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]
        self.assertEqual(b2.grid, b1)
