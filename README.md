# Adressen extraheren
Soms is het nodig om uit de merge bestanden de adressen te halen. In dit Python script wordt vanuit de PDF de adressen opgehaald.

## Installatie
Je hebt minimaal een installatie van Python nodig. Dit is beschreven in kennisitem *KI 3079 Algemeen: Python en Visual Studio Code installeren*. Als dit op jouw systeem geinstalleerd is kan je verder met de volgende stappen:

- Open terminal in Windows of Visual Studio code en typ: `https://github.com/FreddyMeijer/AdressenUitPDFHalen.git`
- Open in terminal of Visual Studio Code de map waarin de repo geplaatst is
- Typ nu `pip install -r requirements.txt`
- Voer Python bestand `adressenExtraheren.py` uit

## .gitignore
Omdat de Python code een CSV bestand maakt van adressen uit de PDF, zijn CSV bestanden uitgezonderd in deze sourcecontrol. Je wilt niet het risico lopen dat adressen van burgers op GitHub verschijnen.

## adressenExtraheren.py
Het Python script zal de gebruiker eerst vragen om een PDF document te kiezen waaruit de gegevens gehaald moeten worden (`def selectFile()`). Hierna moet de gebruiker aangeven om welk producttype uit PAL21 het gaat. Omdat iedere brief er net even anders uitziet, is de positie van het unieke kenmerk (aanslagnummer of kenteken) net even anders. In de eerste `while` loop van `def adressenExtraheren(bestand)` wordt afgedwongen dat de keuze 02, 04, 08, 09, 21, 22, 30 of 51 is.