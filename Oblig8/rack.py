from node import Node

class Rack:                                                     #Setter opp klassen
    def __init__(self):                                         #Setter opp en liste noder
        self._nodeListe = []

    def settInn(self, node):                                    #Legger noder til i listen
        self._nodeListe.append(node)

    def getAntNoder(self):                                      #Regner ut lengden av noden
        return len(self._nodeListe)

    def antProsessorer(self):                                   #Teller totale antall prosessorer
        sammenlagtProsessorer = 0
        for x in self._nodeListe:
            sammenlagtProsessorer += x.antProsessorer()
        return sammenlagtProsessorer

    def noderMedNokMinne(self, paakrevdMinne):                  #Teller antall noder i en klynge med grenser
        nokMinne = 0
        for x in self._nodeListe:
            if x.nokMinne(paakrevdMinne) == True:
                nokMinne += 1
        return nokMinne                                         #Returnerer nokMinne
