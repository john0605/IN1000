#Oppgave4.1
ordet = input("Skriv inn et ord.")
bokstavOrd = int(len(ordet))
print("Det er", bokstavOrd, "bokstaver i ordet.")

# Dette vil kunne telle antall bokstaver som er i ordet ved bruk av len()

#Oppgave4.2
from collections import defaultdict
setning = input("Skriv inn en setning.")
liste = setning.split()

ordbok = defaultdict(int)
for ord in liste:
    ordbok[ord] += 1
print(ordbok)

# Her importer jeg defaultdict som vil kunne legge til verdier i listen. 

#Oppgave4.3
antallOrd = int(len(liste))
print("Det er", antallOrd, "ord i setningen din")

for ordene in ordbok:
    antallBokstaverOrd = int(len(ordene))
    print("Ordet", ordene, "forekommer", ordbok[ord],"gang, og har", antallBokstaverOrd, "bokstaver." )
