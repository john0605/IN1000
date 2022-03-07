# Oppgave 3
class Hund:                                 #Setter opp klassen Hund.
    
    def __init__(self, alder, vekt):        #Definerer konstruktrøren med __init__ og setter instansvariablene.
        self._alder = alder
        self._vekt = vekt
        self._metthet = 10
    
    def hentUtAlder(self):                  #Setter opp en metode for å hente ut alder.
        return self._alder                  #Returnerer alder.
    
    def hentUtVekt(self):                   #Setter opp en metode som henter ut vekt.
        return self._vekt                   #Returnerer vekt.
    
    def spring(self):                       #Del oppgave 3.
        self._metthet -= 1                  #Begynner med å trekke 1 fra mettheten.
        if self._metthet < 5:               #If setningen sjekker om mettheten er under 5.
            self._vekt -= 1                 #Dersom den er uter 5 så vil den trekke 1 fra vekta og hvis ikke så kjører den videre.
    
    def spis(self, heltall):                #Del oppgave 4
        self._metthet += heltall            #Legger til heltall til mettheten.
        if self._metthet > 7:               #Sjekker om mettheten er over 7.
            self._vekt += 1                 #Dersom den er over vil den legger 1 til vekta. 

