#Oppgave1.1
def lagBrukernavn(navn):
    navn = navn.lower()
    navnSplit = navn.split()
    brukerNavn = navnSplit[0] + navnSplit[1][0]
    return(brukerNavn)

#Oppgave1.2
def lagEpost(brukernavn, suffix):
    Epost = (f'{brukernavn}@{suffix}')
    Epost = Epost.lower()
    return(Epost)

#Oppgave1.3
def skrivUtEpost(ordbok):
    for x in ordbok:
        liste = lagEpost(x, ordbok[x])
    return liste

#Oppgave1.4
def hovedprogram():
    ordbok = {}
    brukerInput = input("Tast inn i for å legge til, p for å printe eller s for å gå ut av programmet.")
    while brukerInput != "s":
        if brukerInput == "i":
            navn = input("Tast inn et navn, både fornavn og etternavn:")
            brukernavn = lagBrukernavn(navn)
            suffix = input("Tast inn en suffix, dette kan være for eksempel: hotmail.com eller student.matnat.uio.no:")
            ordbok[brukernavn] = suffix
            brukerInput = input("Tast inn i for å legge til, p for å printe eller s for å gå ut av programmet.")
        elif brukerInput == "p":
            print("Eposten:" , skrivUtEpost(ordbok))
            brukerInput = input("Tast inn i for å legge til, p for å printe eller s for å gå ut av programmet.")
        
hovedprogram()
print("Programm avsluttet :) ")