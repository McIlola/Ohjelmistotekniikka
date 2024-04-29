from random import sample
import copy

class Sudoku:
    """Luokka, joka luo pelilaudan ja pilottaa osan numeroista.
    """
    def __init__(self) -> None:
        """Luokan konstruktori, joka päättää laudan suuruden ja piilotettujen numeroiden määrän.

        Args:
            base: yhden osan sivun suuruus.
            side: yhden sivun suuruus.
            hiddennum: satunnaisesti luotu lista numeroista jota pilotetaan.
        """
        self.base = 3
        self.side = self.base * self.base
        self.hiddennum = sample(range(self.side*self.side), 50)
        self.solution = self.puzzle_creator()
        self.given_puzzle = self.number_hider()

    def puzzle_creator(self):
        """Luo satunnaisen oikean pelilaudan.
        
        Returns:
            Listan listoista jotka sisältävät pelilaudan.
        """
        def pattern(r, c):
            return (self.base*(r % self.base)+r//self.base+c) % self.side

        def shuffle(n):
            return sample(n, len(n))
        rbase = range(self.base)
        rows = []
        for i in shuffle(rbase):
            for r in shuffle(rbase):
                rows.append(i*self.base+r)
        colums = []
        for i in shuffle(rbase):
            for c in shuffle(rbase):
                colums.append(i*self.base+c)
        nums = shuffle(range(1, self.base*self.base+1))
        self.board = []
        for c in colums:
            row = []
            for r in rows:
                row.append(nums[pattern(r, c)])
            self.board.append(row)
        return self.board

    def number_hider(self):
        """Kopioi pelilaudan ja käyttää listaa: hiddennum piilottaakseen osan numeroista.

        Returns:
            Lista listoista jossa osa numeorista piilotettu, eli vaihdettu nollaksi.
        """
        self.puzzle = copy.deepcopy(self.board)
        for i in self.hiddennum:
            self.puzzle[i//9][i % 9] = 0
        return self.puzzle
