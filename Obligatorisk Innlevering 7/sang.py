#Oppgave 2
class Sang:
    def __init__(self, artist, tittel):                                     #Definerer innit med artist, og tittel
        self._tittel = tittel
        self._artist = artist
    
    def spill(self):                                                        #Metode som vil kunne spille av sangen
        print(f'Spiller {self._tittel} av {self._artist} ')
    
    def sjekkArtist(self, navn):                                            #Vil kunne sjekke artisten
        if any(x in navn
            for x in self._artist.split() ):                                #Og returnerer om det er samme eller ikke
            return True
        else:
            return False
    
    def sjekkTittel(self, tittel):                                          #Vil kunne sjekke om tittelen er det samme
        return tittel.lower() == self._tittel.lower()
    
    def sjekkArtistOgTittel(self, artist, tittel):                          #Sjekker både tittelen og artisten
        return self.sjekkArtist(artist) and self.sjekkTittel(tittel)
