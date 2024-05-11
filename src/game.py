import sys
import pygame
from app import Sudoku

class Game:
    """Luokka, jolla itse sudoku peliä pelataan.
    """
    def __init__(self) -> None:
        """Luokan konstruktori, joka antaa aloitusarvoja sekä aloittaa luokan toiminnan.

        Args:
            size: pelilaudan sivun suuruus.
            cell: yhden ruudun suuruus.
            bar: yläpalkin koko.
            display_size: näytön sivun suuruus.
            display: näyttö johon piirretään.
            font: tekstissä käytettävä fontti.
            cell_x ja cell_y: selvittää missä pelaaja on näytöllä.
            rect: neliö joka näyttää misää pelaaja on näytöllä.
            ready: määrittää onko pelaaja valmis aloittamaan.
            errors: määrä virheitä jota pelaajalla on.
            loop(): aloittaa while silmukan.
        """
        pygame.init()
        self.size = 9
        self.cell = 50
        self.bar = 70
        self.display_size = self.size * self.cell
        self.display = pygame.display.set_mode((self.display_size, 
                                                self.display_size+self.bar))
        self.font = pygame.font.SysFont("Arial", 30)
        self.cell_x, self.cell_y = 0, 0
        self.rect = pygame.Rect(0, self.bar, self.cell, self.cell)
        self.ready = False
        self.errors = 0
        self.loop()

    def loop(self):
        """While silmukka joka kutsuu luokan aloitusnäytön ja sen jälkeen piirto ja tapahtuman etsintä metodeita.
        """
        while True:
            if not self.ready:
                self.start_screen()
            else:
                self.draw_board()
                self.search_events()
    
    def start_screen(self):
        """Aloitusnäyttö, antaa mahdollisuuden valita vaikeusaste.

        Args:
        modebutton1 ja modebutton2: luo ruudun jota painamalla voi valita vaikeusasteen.
        text1 ja text2: vaikeusasteiden tekstit. 
        game: luo pelilaudan kutsumalla app.py:n luokkaa riippuen vaikeusasteesta.
        start: pelin aloitusaika.
        """
        self.display.fill((0, 0, 0))
            
        self.modebutton1 = pygame.Rect(self.display_size/2-75,50,150,50)
        pygame.draw.rect(self.display,(255,255,255),self.modebutton1)
        
        self.modebutton2 = pygame.Rect(self.display_size/2-75,150,150,50)
        pygame.draw.rect(self.display,(255,255,255),self.modebutton2)
        
        text1=self.font.render("Easy mode",True,(0,0,0))
        self.display.blit(text1,
                          (self.modebutton1.centerx-text1.get_width()/2,
                           self.modebutton1.centery-text1.get_height()/2))
        text2=self.font.render("Hard mode",True,(0,0,0))
        self.display.blit(text2,
                          (self.modebutton2.centerx-text2.get_width()/2,
                           self.modebutton2.centery-text2.get_height()/2))
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(self.modebutton1,event.pos):
                    self.game = Sudoku(30)
                    self.ready = True
                    self.start = pygame.time.get_ticks()
                if pygame.Rect.collidepoint(self.modebutton2,event.pos):
                    self.game = Sudoku(50)
                    self.ready = True
                    self.start = pygame.time.get_ticks()          
            if event.type == pygame.QUIT: 
                sys.exit() 
        pygame.display.flip()
            
    def draw_board(self):
        """Piirtää pelilaudan käyttäen Sudoku luokan antamaa listojen listaa. 
        Jättää tyhjäksi kaikki ruudut jossa on nolla ja lisää numeron niihin jossa on jotain muuta.
        Lisää myös ajan- ja virheiden laskurin.
        """
        self.display.fill((0,0,0))
        pygame.display.set_caption("Sudoku")
        for i in range(self.size):
            for j in range(self.size):
                if self.game.given_puzzle[i][j] == 0:
                    pygame.draw.rect(self.display, (255,0,0), 
                                     (i*self.cell,j*self.cell+self.bar,
                                      i*self.cell+self.cell,j*self.cell+self.cell), 1)                    
                elif self.game.given_puzzle[i][j] != 0 and (i*9+j) not in self.game.hiddennum:
                    pygame.draw.rect(self.display, (255,0,0), 
                                     (i*self.cell,j*self.cell+self.bar,
                                      i*self.cell+self.cell,j*self.cell+self.cell), 1)
                    number = self.font.render(str(self.game.given_puzzle[i][j]), 
                                              True, (255,0,0))
                    self.display.blit(number,(i*self.cell+18,j*self.cell+8+self.bar))
                else:
                    pygame.draw.rect(self.display, (255,0,0), 
                                     (i*self.cell,j*self.cell+self.bar,
                                      i*self.cell+self.cell,j*self.cell+self.cell), 1)
                    number = self.font.render(str(self.game.given_puzzle[i][j]), 
                                              True, (255,255,255))
                    self.display.blit(number,(i*self.cell+18,j*self.cell+8+self.bar)) 
        pygame.draw.rect(self.display, (255,255,255), 
                         self.rect, 2)
        pygame.draw.line(self.display, (255,255,255), 
                         (3*self.cell, self.bar), 
                         (3*self.cell, self.size*self.cell+self.bar), 3)
        pygame.draw.line(self.display, (255,255,255), 
                         (6*self.cell, self.bar), 
                         (6*self.cell, self.size*self.cell+self.bar), 3)
        pygame.draw.line(self.display, (255,255,255), 
                         (0, 3*self.cell+self.bar), 
                         (self.size*self.cell, 3*self.cell+self.bar), 3)
        pygame.draw.line(self.display, (255,255,255), 
                         (0, 6*self.cell+self.bar), 
                         (self.size*self.cell, 6*self.cell+self.bar), 3)
        errortext = self.font.render(f"Errors(esc to check): {self.errors}",True,(255,255,255))
        self.display.blit(errortext,
                          (self.display_size-20-errortext.get_width(), 15))
        self.timer()
        pygame.display.flip()
    
    def search_events(self):
        """Käy läpi tapahtumia. Pelistä poistumisen, numeroiden ja nuolinäppäinten painallukset ja laudan tarkastuksen.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and self.cell_y<8:
                    self.rect.move_ip(0, self.cell)
                    self.cell_y += 1 
                if event.key == pygame.K_UP and self.cell_y>0:
                    self.rect.move_ip(0, -self.cell)
                    self.cell_y -= 1
                if event.key == pygame.K_RIGHT and self.cell_x<8:
                    self.rect.move_ip(self.cell, 0)
                    self.cell_x += 1 
                if event.key == pygame.K_LEFT and self.cell_x>0:
                    self.rect.move_ip(-self.cell, 0)
                    self.cell_x -= 1
                if event.key == pygame.K_1 or event.key == pygame.K_KP1 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 2   
                if event.key == pygame.K_3 or event.key == pygame.K_KP3 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 9 
                if event.key == pygame.K_0 or event.key == pygame.K_KP0 and self.isprefill():
                    self.game.given_puzzle[self.cell_x][self.cell_y] = 0
                if event.key == pygame.K_ESCAPE:
                    self.errorcheck()
    
    def timer(self):
        """Tekee ajanlaskurin sekunneissa ja näyttää sen vasemmassa yläkulmassa.
        """
        timer = self.font.render(f"{(pygame.time.get_ticks()-self.start)//1000} s", 
                                              True, (255,255,255))
        self.display.blit(timer,(20,15))
    
    def isprefill(self):
        """Tarkastaa jos ruutu johon numeroa ollaan laittamassa on etukäteen täytty.

        Returns:
            True: Jos ruutun voidaan laittaa numero
            False: Etukäteen täytetty ja estää täyttämistä.
        """
        if self.cell_x * 9 + self.cell_y in self.game.hiddennum:
            return True
        return False
    
    def errorcheck(self):
        """Tarkastaa jos vastaukset ovat oikein ja poistaa väärät.
        Laskee myös virheiden määrän, jos virheitä ei ole, niin lopettaa pelin.
        """
        correct = True
        for i in range(self.size):
            for j in range(self.size):
                if self.game.given_puzzle[i][j] != self.game.solution[i][j]:
                    if self.game.given_puzzle[i][j] != 0:
                        self.errors += 1
                    self.game.given_puzzle[i][j] = 0
                    correct = False
        if correct:
            self.record = (pygame.time.get_ticks()-self.start)//1000
            self.endscreen()

    def endscreen(self):
        """Luo lopetusnäytön jossa saa nähdä tuloksensa pelistä, sekä aloittaa uudelleen.

        Args:
        restartbutton: ruutu, jota painamalla voi aloittaa pelin uudelleen.
        restarttext: napin päällä oleva teksti.
        timetext ja errortext: kertovat ajan ja virheiden määrän.
        """
        while True:
            self.display.fill((0, 0, 0))

            self.restartbutton = pygame.Rect(self.display_size/2-75,self.display_size,150,50)
            pygame.draw.rect(self.display,(255,255,255),self.restartbutton)

            restarttext = self.font.render("Restart",True,(0,0,0))
            self.display.blit(restarttext,
                              (self.modebutton1.centerx-restarttext.get_width()/2,
                               self.restartbutton.centery-restarttext.get_height()/2))

            timetext = self.font.render(f"Your time was: {self.record} s",True,(255,255,255))
            self.display.blit(timetext,
                              (self.display_size/2-timetext.get_width()/2,self.bar))
            
            errortext = self.font.render(f"Errors: {self.errors}",True,(255,255,255))
            self.display.blit(errortext,
                              (self.display_size/2-errortext.get_width()/2,50+self.bar))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect.collidepoint(self.restartbutton,event.pos):
                        Game()     
                if event.type == pygame.QUIT: 
                    sys.exit() 
            pygame.display.flip()
    
if __name__ == "__main__":
    Game()
