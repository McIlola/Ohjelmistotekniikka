from random import sample
#import sys
#import os
#import pygame

class Sudoku:
    def __init__(self) -> None:
        pass

    def puzzle_creator(self):
        base = 3
        side = base*base

        def pattern(r, c):
            return (base*(r % base)+r//base+c) % side

        def shuffle(n):
            return sample(n, len(n))
        rbase = range(base)
        rows = []
        for i in shuffle(rbase):
            for r in shuffle(rbase):
                rows.append(i*base+r)
        colums = []
        for i in shuffle(rbase):
            for c in shuffle(rbase):
                colums.append(i*base+c)
        nums = shuffle(range(1, base*base+1))
        self.board = []
        for c in colums:
            row = []
            for r in rows:
                row.append(nums[pattern(r, c)])
            self.board.append(row)
        return self.board

    def number_hider(self):
        side = 9
        self.puzzle = self.board.copy()
        for i in sample(range(side*side), 50):
            self.puzzle[i//9][i % 9] = 0
        return self.puzzle


if __name__ == "__main__":
    pelaa = Sudoku()
    for i in pelaa.puzzle_creator():
        print(i)
    print("")
    for i in pelaa.number_hider():
        print(i)
