import unittest
from m2 import Test

class TestTicTacToe(unittest.TestCase):
    def test_check_for_win(self):
        board_tester = Test()

        # Test case 1: X wins in the first row
        board = [["X", "X", "X"],
                 ["O", "O", "?"],
                 ["?", "?", "?"]]
        self.assertTrue(board_tester.check_for_win(board))

        # Test case 2: O wins in the first row
        board = [["O", "O", "O"],
                 ["X", "X", "?"],
                 ["?", "?", "?"]]
        self.assertTrue(board_tester.check_for_win(board))

        # Test case 3: No win
        board = [["X", "O", "X"],
                 ["O", "X", "?"],
                 ["?", "?", "?"]]
        self.assertFalse(board_tester.check_for_win(board))

if __name__ == "__main__":
    unittest.main()
