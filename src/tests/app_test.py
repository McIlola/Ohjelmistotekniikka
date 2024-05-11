import unittest
from app import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.game = Sudoku(50)
        self.pelaa = self.game.puzzle_creator()

    def test_pelin_luominen_toimii(self):
        self.assertEqual(len(self.pelaa), 9)
        for i in self.pelaa:
            self.assertEqual(len(i), 9)
    
    def test_ruutujen_piilotus_toimii(self):
        peli = self.game.number_hider()
        zerocounter = 0
        for i in peli:
            zerocounter += i.count(0)
        self.assertEqual(zerocounter, 50)
            

