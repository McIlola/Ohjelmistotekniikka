```mermaid
 classDiagram
    class app{- puzzle_creator
    - number_hider}
        app -- game
    class game{- loop
    - draw_board
    - search_events}
```
