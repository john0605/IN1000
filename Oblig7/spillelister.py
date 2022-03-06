#Oppgave 3
from sang import Sang

class Spilleliste:

    def __init__(self, listenavn):                                  #Konstruktøren samt lista blir satt opp her
        self._sanger = []
        self._navn = listenavn
    
    def lesFraFil(self, filnavn):                                   #Metoden åpner filen og leser data om sangene
        sangFil = open(filnavn)
        for linje in sangFil:
            alleData = linje.strip().split(';')                     #Splitter med ';' og setter dem i [0] og [1]
            sang = Sang(alleData[0] , alleData[1])
            self._sanger.append(sang)
        return sangFil

        sangFil.close()                                             #Lukker den åpne filen

    def leggTilSang(self, nySang):                                  #Metode for å legge til sang i listen
        self._sanger.append(nySang)
    
    def fjernSang(self, sang):                                      #Metode for å fjerne sang i listen
        self._sanger.remove(sang)
    
    def spillSang(self, sang):                                      #Metode som spiller av en sang fra listen
        sang.spill()
    
    def spillAlle(self):                                            #Metode som spiller av alle sangene i listen
        for sang in self._sanger:
            sang.spill()
    
    def finnSang(self, tittel):                                     #Metode som finner en spesifikt sang og returnerer om den er der
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                return sang
    
    def hentArtistUtvalg(self, artistnavn):                         #Setter opp ny liste og bruker if-sjekk for å se om artisten er der
        nySpilleListe = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                nySpilleListe.append(sang)
        return nySpilleListe                                        #For så returnerer lista

