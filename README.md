# ProjectC_Assignments
Hier staan de summatieve opdrachten van Project C

# Luka Herrmann

# Mastermind
    # Handleiding
    Run de file 'Mastermind_Control' om het spel op te starten.
    In lijn 65 t/m 70 van 'Mastermind_Control' kan je configureren welk algoritme je wil dat de computer gebruikt om jouw code te raden
    
    # Heuristiek
    Van de mogelijke oplossingen kijken welke frequentie van unieke kleuren het dichtst bij de helft van het totale aantal oplossingen ligt en daar een oplossing willekeurig van       uitkiezen. Doe dit steeds opnieuw totdat de oplossing gevonden is.
    
    # Pseudocode
    1.	Het systeem prompt de gebruiker met de keuze of hij/zij wil raden of de computer laten raden.
    2.	Als de gebruiker kiest om de code te raden
        2.1.	Het syteem genereert een willekeurige code bestaande uit 6 mogelijke kleuren.
        2.2.	De gebruiker raadt een combinatie.
        2.3.	Als de code niet klopt
            2.3.1.	 Als de gebruiker minder dan twaalf pogingen heeft gedaan
            2.3.1.1.	Het systeem geeft aan hoeveel kleuren van de code de gebruiker correct heeft geplaatst en hoeveel kleuren correct gekozen zijn, maar niet op de juiste                              plek.
            2.3.1.2.	Ga naar stap 2.2.
            2.3.2.	 Als de gebruiker twaalf pogingen heeft gedaan
            2.3.2.1.	De gebruiker heeft verloren (Einde programma).
        2.4.	Als de code klopt
        2.4.1.	 De gebruiker heeft gewonnen (Einde programma).
    3.	Als de gebruiker kiest om de code te maken
        3.1.	Het systeem vraagt wat voor code de gebruiker wil, bestaande uit 4 gekozen kleuren van de 6 mogelijke kleuren.
        3.2.	Het systeem raadt een combinatie.
        3.3.	Als de code niet klopt
            3.3.1.	 Als het systeem minder dan twaalf pogingen heeft gedaan
            3.3.1.1.	De gebruiker geeft aan hoeveel kleuren van de code de gebruiker correct heeft geplaatst en hoeveel kleuren correct gekozen zijn, maar niet op de juiste                             plek.
            3.3.1.2.	Ga naar stap 3.2.
            3.3.2.	 Als het systeem twaalf pogingen heeft gedaan
            3.3.2.1.	De gebruiker heeft gewonnen (Einde programma).
        3.4.	Als de code klopt
        3.4.1.	 De gebruiker heeft verloren (Einde programma).

