#Oppgave3.1
steder=[]
for x in range(0,5):
    reisemål = input("Tast inn fem reisemål.")
    steder.append(reisemål)

# Setter opp en for loop som vil kunne hente inn fem inputs fra brukeren

#Oppgave3.2
klesplagg=[]
for y in range(0,5):
    plagg = input("Tast inn fem klesplagg.")
    klesplagg.append(plagg)

avreisedato=[]
for z in range(0,5):
    dato = int(input("Tast inn fem avreisedato."))
    avreisedato.append(dato)

# Setter opp en for loop som vil kunne hente inn fem inputs fra brukeren, på
# samme måte som forrige oppgave.

#Oppgave3.3
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedato)

# Her legger jeg bare til de tre listene i den nye listen ved bruk av append

#Oppgave3.4
for a in reiseplan:
    print(*a)

# print(*) vil kunne printe ut listene i terminalen hver for seg.

#Oppgave3.5
liste_indeks1 = int(input("Velg mellom tallene 0 til 2."))
while liste_indeks1:
    if liste_indeks1 != 0 and liste_indeks1 > 2:
        print("ugyldig input.")
        liste_indeks1 = int(input("Velg mellom tallene 0 til 2."))
    else:
        break

liste_indeks2 = int(input("Velg mellom tallene 0 til 4."))
while liste_indeks2:
    if liste_indeks2 != 0 and liste_indeks2 > 4:
        print("ugyldig input.")
        liste_indeks2 = int(input("Velg mellom tallene 0 til 4."))
    else:
        break

print(reiseplan[liste_indeks1][liste_indeks2])

# Her har jeg satt opp en program som vil kunne la brukeren taste inn tallene
# sine på nytt dersom de ikke er gyldige. Dette gjorde jeg ved bruken av to
# while loops. Dersom tallene er gyldig vil den slå ut plasseringen i den
# nøstede listen.
