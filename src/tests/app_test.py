import unittest
from app import Sudoku

class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.pelaa = Sudoku()
    
    def test_pelin_luominen_toimii(self):
        peli = self.pelaa.puzzle_creator()
        for i in peli:
            self.assertEqual(len(i), 9)