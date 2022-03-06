# Oppgave 6

""" Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter
og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
instansvariabel hobbyer som en tom liste . Skriv en metode leggTilHobby som tar
imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode
skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og
alder kaller på metoden skrivHobbyer.
Lag deretter et testprogram for klassen Person der du lar brukeren skrive inn navn og
alder, og oppretter et Person-objekt med informasjonen du får. Deretter skal brukeren
ved hjelp av en løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger
ønsker å oppgi hobbyer skal informasjon om brukeren skrives ut."""

class Person:                                                       #Setter opp en klasse for Person
    def __init__(self, navn, alder):                                #Setter inn instansvariablene
        self._navn = navn
        self._alder = alder
        self._hobby = []
    
    def leggTilHobby(self, nyHobby):                                #Definerer leggTilHobby med en instasvariabel
        self._hobby.append(nyHobby)                                 #nyHobby vil bli lagt til i listen self._hobby
    
    def skrivHobbyer(self):                                         #Methode som skriver ut hobby
        print(self._hobby)                                          #Skriver ut hobby til terminalen
    
    def skrivUt(self):                                              #Methode som vil kunne skrive ut all informasjon
        print("---Person---")
        print(f'Navnet ditt: {self._navn}')
        print(f'Alderen din: {self._alder}')
        print(f'Dine hobby: {self._hobby}')
