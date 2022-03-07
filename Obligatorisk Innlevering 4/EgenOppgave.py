"""
Oppgave5
Sett opp et system som tar imot navn og bursdagsdatoen fra brukeren og
lagrer det. Dersom brukeren skal ha datoen så kan han lett slå opp her.
"""

bursdag = []

def leggtil():
    navn = input("Tast inn navnet til han du vil legge til")
    dato = int(input("Tast inn bursdagsdatoen i format DDMMÅÅÅÅ"))
    bursdagNavnDato = [navn, dato]
    bursdag.append(bursdagNavnDato)
    print(bursdag)

def opp():
    print("Det har ikke blitt lagt til noe her.")

def spørsmål():
    svar = input("Legge til navn og bursdag eller søke opp? tast inn A hvis du vil legge til eller B hvis du vil søke opp.")
    if svar == "A" or "a":
        print(leggtil())
    elif svar == "B":
        print(opp())

spørsmål()

# Har laget et system som vil kunne ta imot opplysning fra brukeren og vil kunne skrive det ut i terminalen
# Den spør brukeren om han vil legge til opplysninger eller skrive ut hele listen sånn at han kan se hvilke dato
# og navn som er i listen. 
