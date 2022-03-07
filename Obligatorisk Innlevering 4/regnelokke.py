#Oppgave2.1/2.2
liste = []
innlestTall = int(input("Skriv inn et tall."))
while innlestTall != 0:
    liste.append(innlestTall)
    innlestTall = int(input("Skriv inn et tall."))
print(liste)

#Oppgave2.3
for tall in liste:
    print(tall)

#Oppgave2.4
minSum = 0
for summen in liste:
    minSum += summen
print(minSum)

# Her regnte jeg ut summen helt vanlig ved bruken av forløkke.

#Oppgave2.5
def størsteTallet():
    størstTall = liste[0]
    for tallet in liste:
        if tallet > størstTall:
            størstTall = tallet
    print(størstTall)

def minsteTallet():
    minstTall = liste[0]
    for tallet in liste:
        if tallet < minstTall:
            minstTall = tallet
    print(minstTall)

størsteTallet()
minsteTallet()

# Her satt jeg opp tp prosedyrer som vil kunne slå ut det minst og største
# tallet ved bruk av enkel forløkke som sjekker om tallet er mindre enn eller
# større enn liste[0]
