# Order Report

Projektet läser orderdata från `data/orders.csv`, validerar och städar
datan samt skapar CSV-rapporter i `output/`.

Rapporterna visar en översikt, försäljning per kategori och region
samt returer per kategori.

## Installation och beroenden

Projektet kräver Python 3.10 eller senare.
Pandas används för databehandling och pytest för tester.

Kör följande från projektmappen i Git Bash på Windows:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -e .
python -m pip install pytest
```

Pandas installeras automatiskt tillsammans med projektet.

## Köra programmet

Kör från projektmappen med den virtuella miljön aktiverad:

```bash
python -m order_report
```

Rapporterna sparas i mappen `output/`, som skapas automatiskt.

## Köra testerna

```bash
python -m pytest
```

## Projektstruktur

- `data/` – orderdata som programmet läser.
- `output/` – genererade rapporter.
- `src/order_report/` – programmets kod:
  - `__main__.py` – startar programmet och hanterar fel.
  - `config.py` – sökvägar och logginställningar.
  - `pipeline.py` – kör bearbetningens olika steg.
  - `io.py` – läser och sparar CSV-filer.
  - `validate.py` – kontrollerar orderdata.
  - `transform.py` – städar data och beräknar ordervärden.
  - `report.py` – skapar rapporterna.
- `tests/` – tester för projektets funktioner.
- `pyproject.toml` – projektinställningar och beroenden.


# Reflektion

## 1. Vilka var de viktigaste problemen i originalkoden?

De som står i code_review.md:
### Hög prioritet
1. Fynd 1 - Hela programmet körs vid import
2. Fynd 2 - Flera ansvar är sammanblandade
3. Fynd 7 - Centrala regler saknar tydliga testgränser

### Medelprioritet
4. Fynd 3 - Valideringen ger ett generellt fel
4. Fynd 4 - Try och except runt hela scriptet
5. Fynd 5 - Inställningar för validering är hårdkodade
6. Fynd 6 - Statusmeddelanden använder print

### Låg prioritet
7. Fynd 8 - Namnen beskriver dataflödet dåligt

## 2. Vilka förändringar tycker du förbättrade programmet mest?
Jag tycker att den generella omstruktureringen där varje modul har ett specifikt ansvar och varje funktion en specifik funktion och inte hanteras för mycket olika uppgifter. Detta gör det beydligt lättare att ha en bra överblick över projektet.

## 3. Varför valde du den projektstruktur du använde?
Jag använde en blandning av de strukturerna som du visat i dina videos och i projektbeskrviningen. Jag tycker det blev en lagom struktur för storleken av detta projekt. För många moduler kan också göra det krångligt så jag nöjde mig med några få med tydlig uppgift.

## 4. Var använde du OOP/dataclass och varför passade det där?
Jag använde OOP/dataclass i configurationen för att enkelt kunna byta sökvägar på ett ställe. Man skulle även kunna lägga andra inställningar där som tex vilka rapporter som ska skapas om man vill ha ett mer flexibelt projekt.

## 5. Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?
Testerna kontrollerar att programmets funktioner uppfyller sina förväntade ”kontrakt”, till exempel vilka situationer som ska ge ett undantag respektive en varning. De kontrollerar också att datastädning, validering, beräkningar och rapporter ger förväntade resultat. Vid framtida ändringar hjälper testerna till att upptäcka om något som tidigare fungerade har gått sönder

## 6. Vad var svårast?
Att förstå symbiosen mellan loggermeddellande, try except och raise. Hur dessa ska användas i kombination på ett bra sätt.

## 7. Vad hade du velat förbättra ytterligare om du haft mer tid? 
Att lägga till fler inställningar i configurationen som gör det enklet att skapa andra typer av rapporter. 