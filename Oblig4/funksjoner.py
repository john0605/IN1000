#Oppgave1.1
def adder(tall1, tall2):
    return(int(tall1) + int(tall2))

print("Summen blir da", adder(4,3))
print("Summen blir da", adder(9,10))

# Jeg defininerte adder for så satt jeg opp en return som forteller at tallene
# skal legge sammen og printet det ut to ganger.

#Oppgave1.2/1.3
minTekst = input("Skriv inn en setning.")
minBokstav = input("Skriv inn en bokstav fra setningen din.")

def tellForekomst(minTekst, minBokstav):
    antall = 0

    for tegn in minTekst:
        if minBokstav == tegn:
            antall += 1
    print(antall)
tellForekomst(minTekst, minBokstav)

# her definerer jeg som oppgaven spør om så setter jeg opp en forløkke som vil kunne
# telle minTekst og minBokstav.
