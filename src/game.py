import sys
import pygame
from app import Sudoku
pygame.init()

class Game:
    """Luokka, jolla itse sudoku peliä pelataan.
    """
    def __init__(self) -> None:
        """Luokan konstruktori, joka antaa aloitus arvoja sekä aloittaa luokan toiminnan.

        Args:
            game: luo pelilaudan kutsumalla app.py:n luokkaa.
            size: pelilaudan sivun suuruus.
            cell_size: yhden ruudun suuruus.
            display_size: näytön sivun suuruus.
            display: näyttö johon piirretään.
            font: tekstissä käytettävä fontti.
            cell_x ja cell_y: selvittää missä pelaaja on näytöllä.
            rect: neliö joka näyttää misää pelaaja on näytöllä.
            loop(): aloittaa while silmukan.
        """
        self.game = Sudoku()
        self.size = len(self.game.solution)
        self.cell_size = 50
        self.display_size = self.size * self.cell_size
        self.display = pygame.display.set_mode((self.display_size, self.display_size))
        self.font = pygame.font.SysFont("Arial", 30)
        self.cell_x, self.cell_y = 0, 0
        self.rect = pygame.Rect(0, 0, self.cell_size, self.cell_size)
        self.loop()

    def loop(self):
        """While silmukka joka kutsuu luokan piirto ja taphtuman etsintä metodeita.
        """
        while True:
            self.draw_board()
            self.search_events()
            
    def draw_board(self):
        """Piirtää pelilaudan käyttäen Sudoku luokan antamaa listojen listaa. Jättää tyhjäksi kaikki ruudut jossa on nolla ja lisää numeron niihin jossa on jotain muuta.
        """
        self.display.fill((0,0,0))
        pygame.display.set_caption("Sudoku")
        for i in range(self.size):
            for j in range(self.size):
                if self.game.given_puzzle[i][j] == 0:
                    pygame.draw.rect(self.display, (255,0,0), (i*self.cell_size,j*self.cell_size,i*self.cell_size+self.cell_size,j*self.cell_size+self.cell_size), 1)                    
                elif self.game.given_puzzle[i][j] != 0 and (i*9+j) not in self.game.hiddennum:
                    pygame.draw.rect(self.display, (255,0,0), (i*self.cell_size,j*self.cell_size,i*self.cell_size+self.cell_size,j*self.cell_size+self.cell_size), 1)
                    number = self.font.render(str(self.game.given_puzzle[i][j]), True, (255,0,0))
                    self.display.blit(number,(i*self.cell_size+18,j*self.cell_size+8))
                else:
                    pygame.draw.rect(self.display, (255,0,0), (i*self.cell_size,j*self.cell_size,i*self.cell_size+self.cell_size,j*self.cell_size+self.cell_size), 1)
                    number = self.font.render(str(self.game.given_puzzle[i][j]), True, (255,255,255))
                    self.display.blit(number,(i*self.cell_size+18,j*self.cell_size+8)) 
        pygame.draw.rect(self.display, (255,255,255), self.rect, 2)
        pygame.draw.line(self.display, (255,255,255), (3*self.cell_size, 0), (3*self.cell_size, self.size*self.cell_size), 3)
        pygame.draw.line(self.display, (255,255,255), (6*self.cell_size, 0), (6*self.cell_size, self.size*self.cell_size), 3)
        pygame.draw.line(self.display, (255,255,255), (0, 3*self.cell_size), (self.size*self.cell_size, 3*self.cell_size), 3)
        pygame.draw.line(self.display, (255,255,255), (0, 6*self.cell_size), (self.size*self.cell_size, 6*self.cell_size), 3)
        pygame.display.flip()
    
    def search_events(self):
        """Käy läpi tapahtumia. Tässä vaiheessa pelistä poistumisen ja numeroiden ja nuolinäppäinten painallukset.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and self.cell_y<8:
                    self.rect.move_ip(0, self.cell_size)
                    self.cell_y += 1 
                if event.key == pygame.K_UP and self.cell_y>0:
                    self.rect.move_ip(0, -self.cell_size)
                    self.cell_y -= 1
                if event.key == pygame.K_RIGHT and self.cell_x<8:
                    self.rect.move_ip(self.cell_size, 0)
                    self.cell_x += 1 
                if event.key == pygame.K_LEFT and self.cell_x>0:
                    self.rect.move_ip(-self.cell_size, 0)
                    self.cell_x -= 1
                if event.key == pygame.K_1 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 1
                if event.key == pygame.K_2 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 2   
                if event.key == pygame.K_3 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 3
                if event.key == pygame.K_4 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 4
                if event.key == pygame.K_5 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 5
                if event.key == pygame.K_6 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 6
                if event.key == pygame.K_7 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 7
                if event.key == pygame.K_8 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 8
                if event.key == pygame.K_9 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 9 
                if event.key == pygame.K_0 and (self.cell_x * 9 + self.cell_y) in self.game.hiddennum:
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 0 
if __name__ == "__main__":
    Game()
