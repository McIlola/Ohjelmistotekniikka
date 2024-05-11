## Sovelluslogiikka
```mermaid
 classDiagram
    class app{- puzzle_creator
    - number_hider}
        app -- game
    class game{- loop
    - start_screen
    - draw_board
    - search_events
    - timer
    - isprefill
    - errorcheck
    - end_screen}
```
App luo pelilaudan ja pilottaa numerot. Game käyttää pelilautaa luodakseen pelin ja antaa käyttäjän pelata.

## Sekvenssikaavio
```mermaid
sequenceDiagram
        game ->> app: Sudoku(mode)
```
## Sekvenssikaavio game:in toiminnasta.
```merrmaid
    
