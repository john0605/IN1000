# Oppgave 4
class Dato:                                                                 #Lager en klasse for Dato

    def __init__(self, nyDag, nyMåned, nyttÅr):                             #Definerer konstruktøren og setter inn instansvariablene
        self._nyDag = nyDag
        self._nyMåned = nyMåned
        self._nyttÅr = nyttÅr

    def lesÅr(self):                                                        #Setter opp en metoden som leser år 
        return self._nyttÅr                                                 #Dette vil kunne returnere året

    def skriverUtDato(self):                                                #Metode som vil kunne skrive ut hele datoen 
        return (self._nyDag, self._nyMåned, self._nyttÅr)                   #Returnerer datoen

    def sjekk(self, bestemtDag):                                            #Sjekker om dagen er det samme som bestemtedagen
        return self._nyDag == bestemtDag                                    #Dersom det er det samme så vil den slå ut True og hvis ikke False
    
    def sjekkFørEllerEtter(self, dag, måned, år):                           #Sjekk for å se om datoen er før eller etter, gir tre nye instansvariabler
        if år < self._nyttÅr:                                               #Sjekker om året er mindre enn den nye
            return "Før"                                                    #Hvis den er det så slår den ut Før
        elif år > self._nyttÅr:                                             #Sjekker om året er større enn den nye
            return "Etter"                                                  #Slår ut Etter
        if år == self._nyttÅr:                                              #Sjekker om året er det samme og setter opp en ny if setning
            if måned < self._nyMåned:                                       #Sjekker om måned er mindre
                return "Før"                                                #Slår ut Før dersom den er mindre
            elif måned > self._nyMåned:                                     #Sjekker om måned er større
                return "Etter"                                              #Slår ut Etter
            if måned == self._nyMåned:                                      #Sjekker om månded er det samme og setter opp enda en if setning
                if dag < self._nyDag:                                       #Sjekker om dag er mindre
                    return "Før"                                            #Returnerer Før
                elif dag > self._nyDag:                                     #Sjekker om dag er større
                    return "Etter"                                          #Returnerer Etter
                elif dag == self._nyDag:                                    #Sjekker om dagen er det samme
                    return "Samme Dato"                                     #Siden dagen er det samme så vil hele datoen være lik
    


