# Oppgave 1
from motorsykkel import Motorsykkel                                  #Henter klassen Motorsykkel fra motorsykkel.py

def hovedprogram():                                                  #Definerer prosedyren hovedprogram()
    motorsykkel1 = Motorsykkel("BMW", "FN4216", 50000)               #Setter opp tre ulike motorsykkeler med ulike verdier
    motorsykkel2 = Motorsykkel("Kawasaki", "UD8416", 790000)
    motorsykkel3 = Motorsykkel("Honda", "LJ7953", 43000)

    motorsykklene = [motorsykkel1, motorsykkel2, motorsykkel3]       #Lager en liste med alle motorsykklene
    for MP in motorsykklene:    
        MP.skrivUt()                                                 #skriver ut informasjonen til alle motorsykklene i lista
    
    motorsykkel3.kjør(10)                                            #Setter inn en verdi av 10 dette legges til kilometerstanden
    print(motorsykkel3.hentKilometerstand())                         #Printer ut til terminalen

hovedprogram()                                                       #Her kaller jeg på hele programmet