[Release viikko 5](./realeases/viikko5)
# Sudokupeli

Eli peli jossa tarkoitus täyttää 9x9 lauta numeroilla 1-9 sillä tavalla että jokainen vaaka- ja pystysuuntainen rivi sekä jokainen 3x3 ruutu sisältää numerot 1-9 sudokupeli. Aloittaessa luo satunnaisen laudan ja pilottaa osan nuomeroista ennen pelin alkua. Näitä numeroita voi sitten alkaa täytellä kunnes peli on läpäisty.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```
poetry install
```

2. Käynnistä sovellus komennolla:

```
poetry run invoke start
```

3. Jos Windows-koneella niin käynnistä sovellus komennolla:

```
poetry run invoke windows-start
```
### Testaus

Testit suoritetaan komennolla:

```
poetry run invoke test
```
```
poetry run invoke windows-test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:
```
poetry run invoke coverage
```
tai
```
poetry run invoke coverage-report
```
windows koneella:
```
poetry run invoke windows-coverage
```
tai
```
poetry run invoke windows-coverage-report
```
Raportti generoituu _htmlcov_-hakemistoon.
### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```
poetry run invoke lint
```
ja
```
poetry run invoke windows-lint
```
