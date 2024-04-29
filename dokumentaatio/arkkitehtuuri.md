## Sovelluslogiikka
```mermaid
 classDiagram
    class app{- puzzle_creator
    - number_hider}
        app -- game
    class game{- loop
    - draw_board
    - search_events}
```
App luo pelilaudan ja pilottaa numerot. Game käyttää pelilautaa luodakseen pelin ja antaa käyttäjän pelata.

## Sekvenssikaavio
```mermaid
sequenceDiagram
        game ->> app: Sudoku()
    
