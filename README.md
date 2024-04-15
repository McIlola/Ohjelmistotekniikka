# Sudokupeli

*Yksinkertainen sudokupeli.* Ehkä jotain vaikeusasteita. Luo laudan ja pilottaa osan nuomeroista ennen pelin alkua.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

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

