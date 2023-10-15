from main import end_check, win_check
import unittest


class Game2048Test(unittest.TestCase):
    def test_end_check_True(self):
        matrix = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 64, 128]]
        self.assertEqual(end_check(matrix, 4), True)
        matrix = [[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]
        self.assertEqual(end_check(matrix, 4), True)

    def test_end_check_False(self):
        matrix = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 0, 32, 64], [16, 32, 64, 128]]
        self.assertEqual(end_check(matrix, 4), False)
        matrix = [[4, 4, 2, 4], [8, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]
        self.assertEqual(end_check(matrix, 4), False)
        matrix = [[4, 8, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]
        self.assertEqual(end_check(matrix, 4), False)

    def test_win_check_True(self):
        matrix = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 2048, 64], [16, 32, 64, 128]]
        self.assertEqual(win_check(matrix, 4), True)
        matrix = [[0, 0, 2, 0], [4, 16, 4, 2], [2, 4, 2, 0], [4, 2048, 64, 32]]
        self.assertEqual(win_check(matrix, 4), True)

    def test_win_check_False(self):
        matrix = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 64, 128]]
        self.assertEqual(win_check(matrix, 4), False)
        matrix = [[0, 0, 2, 0], [4, 16, 4, 2], [2, 4, 2, 0], [4, 2, 64, 32]]
        self.assertEqual(win_check(matrix, 4), False)
