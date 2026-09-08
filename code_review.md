### Fynd 1 - Hela programmet körs vid import

**Observation:** Hela arbetsflödet körs på modulnivå.

**Konsekvens:** Import läser och skriver filer. Koden får oväntade sidoeffekter och blir svår att återanvända och testa.

**Förslag:** Lägg programstarten i en `main()`-funktion och skydda anropet med en main-guard

<br>

### Fynd 2 - Flera ansvar är sammanblandade

**Observation:** Scriptet blandar filhantering, validering, transformationslogik, rapportering och programflöde.

**Konsekvens:** Delarna kan inte testas eller återanvändas oberoende av varandra. Olika typer av förändringar behöver göras på samma plats.

**Förslag:** Separera ren transformationslogik från filhantering och orkestrering.

<br>

### Fynd 3 - Valideringen ger ett generellt fel

**Observation:** Valideringen kastar `Exception` med meddelandet `Fel data`.

**Konsekvens:** Felet är svårt att felsöka och svårt att kontrollera specifikt i ett automatiskt test. Det framgår inte vilka kolumner som saknas.

**Förslag:** Kasta `ValueError` och namnen på dom saknade kolumnerna.

<br>

### Fynd 4 – Central felhantering

**Observation:** Programmets huvudfunktion fångar oväntade fel runt anropet
till `run_pipeline`. Felet loggas med traceback och kastas sedan vidare.

**Konsekvens:** Användaren får ett tydligt felmeddelande samtidigt som
informationen om var felet uppstod bevaras. Pipeline-funktionerna kan
fortfarande testas individuellt.

**Förslag:** Behåll den centrala felhanteringen. Lägg endast till lokala
`try/except` där ett fel kan hanteras meningsfullt, exempelvis om ett
I/O-fel behöver kompletteras med information om vilken fil som inte kunde
läsas eller sparas.

<br>

### Fynd 5 - Inställningar för validering är hårdkodade

**Observation:** Krav på kolumner ligger direkt i programflödet.

**Konsekvens:** Det blir svårare att köra programmet med andra filer. Progrtammet blir mindre flexibelt.

**Förslag:** Samla generella instälningar för validering, sökvägar och vilka rapporter som ska skapas på ett ställe.

<br>

### Fynd 6 - Statusmeddelanden använder print

**Observation:** `print()` används för att beskriva att programmet läser data och att körningen är klar.

**Konsekvens:** Det går inte att styra nivå, format, destination, och det framgår inte vilken modul som skapade meddelandet.

**Förslag:** Använd modulloggers för körinformation och konfigurera loggning centralt vid programmets startpunkt.

<br>

### Fynd 7 - Centrala uträkningar saknar tydliga testgränser

**Observation:** uträkningarna för order_value, discounted_value, total_sales, number_of_orders och number_of returns är bundna till hela filflödet.

**Konsekvens:** För att kontrollera uträkningarna måste vi köra hela scriptet och läsa resultatfilen. Testerna blir långsammare och det blir svårare att se var ett fel uppstår.

**Förslag:** Extrahera rena funktioner som tar emot en DataFrame och returnerar en ny DataFrame. Testa den med små DataFrames i minnet.

<br>

### Fynd 8 - Namnen beskriver dataflödet dåligt

**Observation:** Namnen `data` och `result` är allmänna och säger väldigt lite om objektens innehåll eller roll.

**Konsekvens:** Dataflödet blir svårare att följa, särskillt om programmet skulle växa och fler mellanresultat skulle tillkomma.

**Förslag:** Använd mer beskrivande namn, t.ex: `history`, `prepared` och `summary`

<br>

## Prioritering

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