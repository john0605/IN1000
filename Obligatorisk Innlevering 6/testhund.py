# Oppgave 3
from hund import Hund                       #Henter klassen fra hund.py.

def hovedprogram():                         #Setter opp en prosedyre.
    hund1 = Hund(8, 13)                     #Setter inn verdiene for instansvariablene.
    hund1.spring()                          #Kjører spring() første gang.
    hund1.spis(4)                           #Kjører spis() med heltall 4.
    print(hund1.hentUtVekt())               #Returnerer vekta til terminalen ved å printe den ut.
    
    hund1.spring()                          #Kjører spring for andre gang.
    hund1.spis(8)                           #Kjører spis for andre gang.
    print(hund1.hentUtVekt())               #Returnerer den nye vekta til terminalen.

hovedprogram()                              #Her kaller jeg på hele programmet.