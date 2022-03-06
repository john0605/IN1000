class Node:                                             #Setter opp klassen
    def __init__(self, minne, antPros):                 #Paramterere minnestr og prosessorer
        self._minne = minne
        self._antPros = antPros
    
    def antProsessorer(self):                           #Returnerer antall prosessorer
        return self._antPros
    
    def nokMinne(self, paakrevdMinne):                  #Returnerer boolean verdi
        return self._minne >= paakrevdMinne