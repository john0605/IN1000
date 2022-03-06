from node import Node
from rack import Rack

class Regneklynge:												#Setter opp klassen Regneklynge
	def __init__(self, noderPerRack):
		self._noderPerRack = int(noderPerRack)
		self._racksListe = []

	def settInnNode(self, node):								#Setter noder inn i listen som ble opprettet
		if len(self._racksListe) == None:
			rack = Rack()
			rack.settInn(node)
			self._racksListe.append(rack)
			return

		for x in self._racksListe:
			if x.getAntNoder() < self._noderPerRack:
				x.settInn(node)
				return
		
		nyRack = Rack()											#Setter opp en ny rack dersom det er fult
		nyRack.settInn(node)
		self._racksListe.append(nyRack)

	def antProsessorer(self):									#Metoden beregner det totale antall prosessorer
		sammenlagtProsessorer = 0
		for x in self._racksListe:
			sammenlagtProsessorer += x.antProsessorer()
		return sammenlagtProsessorer							#Returnerer antallet

	def noderMedNokMinne(self, paakrevdMinne):					#Sjekker antall noder med gitt grense
		nodeMinne = 0
		for x in self._racksListe:
			nodeMinne += x.noderMedNokMinne(paakrevdMinne)
		return nodeMinne										#Returnerer alle prosessorer

	def antRacks(self):											#Metoden returnerer antall racks i regneklyngen
		return len(self._racksListe)