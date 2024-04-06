import sys
import pygame
import os
from random import sample

class Sudoku:
    def __init__(self) -> None:
        pass
    
    def puzzle_creator(self):
        base = 3
        side = base*base

        def pattern(r,c): 
            return (base*(r%base)+r//base+c)%side
        
        def shuffle(n): 
            return sample(n,len(n)) 
        
        rBase = range(base)
        rows = []
        for i in shuffle(rBase):
            for r in shuffle(rBase):
                 rows.append(i*base+r)
        
        colums = []
        for i in shuffle(rBase):
            for c in shuffle(rBase):
                 colums.append(i*base+c)
                
        nums = shuffle(range(1,base*base+1))
        board = []
        for c in colums:
            row = []
            for r in rows:
                row.append(nums[pattern(r,c)])
            board.append(row)
        return board

if __name__=="__main__":
    pelaa = Sudoku()
    for i in pelaa.puzzle_creator(): print(i)

