from regneklynge import Regneklynge
from node import Node
class Datasenter:                                                                       #Setter opp klassen datasenter
	def __init__(self):
		self._klynger = {}

	def lesInnRegneklynge(self, filnavn):                                               #metode som inhenter data fra fil
            fil = open(filnavn, 'r')                                                    #Åpner filen
            navnPåFil = filnavn.strip(".txt")                                           #Fjerner .txt fra fil navnet
            for x in fil:                                                               #for-løkke som går gjennom filen
                liste = x.strip().split()
                if len(liste) == 1:
                    nyRegneklynge = Regneklynge(int(liste[0]))                          #Setter data fra fil inn i ordboka    
                else:
                    for y in range(int(liste[0])):
                        nyNode = Node(int(liste[1]), int(liste[2]))
                        nyRegneklynge.settInnNode(nyNode)
            self._klynger[navnPåFil] = nyRegneklynge

            fil.close()                                                                 #lukker filen

	
	def skrivUtAlleRegneklynger(self):                                                  #Skriver ut all informasjon om alle regneklynger
		for x in self._klynger:                                                         #For-løkke for å iterere gjennom regneklyngene
			self.skrivUtRegneklynge(x)	


	def skrivUtRegneklynge(self, navn):                                                 #Skriver ut informasjon om en spesifikt regneklynge
            if navn in self._klynger:
                regneklynge = self._klynger[navn]
                print(f'\n---- Informasjon om regneklyngen {navn} ----')
                print(f'Antall rack: {regneklynge.antRacks()} ')
                print(f'Antall prossesorer: {regneklynge.antProsessorer()}')
                print(f'Noder med minst 32GB: {regneklynge.noderMedNokMinne(32)} ')
                print(f'Noder med minst 64GB: {regneklynge.noderMedNokMinne(64)} ')
                print(f'Noder med minst 128GB: {regneklynge.noderMedNokMinne(128)} ')   #Skriver ut til terminalen som satt opp i oppgaven