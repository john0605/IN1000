#Oppgave3
def billett():
    alder = int(input("Skriv inn alder på kjøperen."))
    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif alder > 17 and alder < 63:
        billettpris = 50
    elif alder >= 63:
        billettpris = 35

    print("Billetten din koster", billettpris, "kroner.")

billett()

# Jeg satt opp en prosedyre med to ulike variabler. Hentet inn alder fra bruker
# og satt opp en if liste som definerte prisen ut ifra alderen. 
