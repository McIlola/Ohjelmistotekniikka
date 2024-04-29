# Käyttöohje
Lataa ensin uusin versio koodista linkistä [releases](https://github.com/McIlola/Ohjelmistotekniikka/releases) tai projektin etusivulta painamalla vihreää "Code" nimistä näppäintä ja painamalla "Download ZIP" avautuvasta valikosta.

## Ohjelman käynnistäminen
Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```
poetry install
```
Jonka jälkeen voit käynnistää ohjelman komenolla:
```
poetry run invoke start
```
Jos satut olemaan Windows-koneella, voit käynnistää ohjelman komenolla:
```
poetry run invoke windows-start
```
## Pelaaminen
Käynnistyksen jälkeen näytölle avautuu Sudokupeli, jossa voi liikkua nuolinäppäiminen avulla, ruutu jossa pelaaja sillä hetkellä on se ruutu jossa on valkoinen neliö punaisen sijaan, aloittaessa tämä ruutu on aina vasen yläkulma. Pelaaja voi lisätä numeroita tyhjiin ruutuihin ja ruutuihin jossa on valkoinen numero. Esitäytettyihin ruutuihin ei voi lisätä numeroa.

Pelin tarkoitus on täyttää koko ruudukko sillä tavalla että jokaisessa vaaka- ja pystysuorassa linjassa on numerot 1-9, sekä jokaisessa 3*3 kokoisessa ruudussa on numerot 1-9 (nämä ruudut merkattu valkoisella). Peli on läpäisty kun koko ruudukko on täytetty oikein.
