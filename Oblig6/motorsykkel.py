# Oppgave 1
class Motorsykkel:                                                          #Setter opp en klasse Motorsykkel

    def __init__(self, merke, registreringsnummer, kilometerstand):         #Definerer __init__ med instansvariablene
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._kilometerstand = kilometerstand

    def kjør(self, km):                                                     #Definerer metoden kjør
        self._kilometerstand += km                                          #Setter kilometerstanden som km

    def hentKilometerstand(self):                                           #Enda en metode som henter ut kilometerstand
        return self._kilometerstand                                         #Returnerer kilometerstanden til terminalen
    
    def skrivUt(self):                                                      #Definerer metoden skrivUt og skriver ut alt av info
        print(f'-----MERKE----')                    
        print(f'Merke = {self._merke}')                             
        print(f'Registreringsnummer = {self._registreringsnummer}')
        print(f'Kilometerstand = {self._kilometerstand}')
