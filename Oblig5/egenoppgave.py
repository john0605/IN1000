#Skriv oppgavetekst som gir bruker mulighet til å lage en oppgave
# og at bruker kan svare på en ferdig lagd oppgave.
#løs vha innlesning fra fil.
svar_liste = []
fasit = [20, 10, 4]
svar_egen_oppgave = []
fasit2 = []
def les_fil(filnavn):
    min_fil = open(filnavn)
    indeks = 0
    for i in min_fil:
        indeks += 1
        print(f"oppgave {indeks}: {i}")
        svar_opg = int(input("svar: "))
        svar_liste.append(svar_opg)
        svar_egen_oppgave.append(svar_opg)
    min_fil.close()

def retting(svar_liste, fasit):
    indeks = 0
    for i in svar_liste:
        print(f"svar {indeks + 1}: {i}")
        if svar_liste[indeks] == fasit[indeks]:
            print("riktig!")
            indeks +=1
        else:
            print("feil, riktig svar var", fasit[indeks])
            indeks +=1


def lag_oppgave(filnavn):
    min_fil2 = open(filnavn, "w")
    inp = ""
    indeks = 1
    while inp != "s":
        min_fil2.write(f"Oppgave {indeks}: ")
        min_fil2.write(input("skriv oppgave: "))
        min_fil2.write("\n")
        fasit2.append(int(input("fasit svar: ")))
        inp = input("lage en til opg? tast s for stop: ")
        indeks += 1
    min_fil2.close()

print("ønsker du å lage en oppgave og løse den eller ønsker du å løse fedig lagde oppaver?")
svar_fra_bruker = input("tast tallet 1 for å lage oppgave. tast 2 for å løse oppgave: ")
if svar_fra_bruker == "1":
    lag_oppgave("bok1.csv")
    opg_svar = input("din oppgave er nå skrevet! ønsker du å svare den? ")
    if opg_svar == "ja":
        les_fil("bok1.csv")
        retting(svar_egen_oppgave, fasit2)
elif svar_fra_bruker == "2":
    les_fil("bok.csv")
    retting(svar_liste, fasit)
else:
    print("ugyldig input")



