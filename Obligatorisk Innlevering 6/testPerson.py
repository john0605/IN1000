# Oppgave 6
from person import Person                                                                                       #Henter klassen Person fra person.py

def hovedprogram():                                                                                             #Definerer hovedprogrammet

    navn1 = str(input("Tast inn navnet ditt: "))                                                                #Variabel som tar imot input fra brukeren
    alder1 = int(input("Tast inn alderen din: "))                                                               #Dette gjør det samme
    person1 = Person(navn1, alder1)                                                                             #Obbjekt med variablene hentet fra brukeren
    dineHobby = input("Tast inn L for å legge til en hobby, eller s for å skrive ut informasjon: ")             #variabel for hobby
    while dineHobby != "s":                                                                                     #Setter opp en while løkke som vil kunne hente inn hobbyen
        if dineHobby == "l":
            dineHobbyer = input("skriv inn hobbyen din: ")
            dineHobby = input("Tast inn L for å legge til en hobby, eller s for å skrive ut informasjon: ")     #Dette vil kunne kjøre i løkke og inhente hobbyen flere ganger    
        elif dineHobby == "p":                                                                                  #Skriver ut informasjonen
             person1.skrivUt()
    person1.leggTilHobby(dineHobbyer)                                                                           #Legger til i listen
    person1.skrivUt()                                                                                           #Skriver ut informasjonen

hovedprogram()                                                                                                  #Kjører hovedprogrammet