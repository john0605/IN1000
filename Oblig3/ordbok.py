#Oppgave2.1
varerButikk = {"melk" : 14.90, "brød" : 24.90, "yoghurt" : 12.90, "pizza" : 39.90}
print(varerButikk)

vare = str(input("Skiv in en vare som du liker."))
pris = float(input("Hvor mye koster denne varen? Skriv inn som flyttall."))

vare2 = str(input("Skriv in en vare som du trenger til å lage pizza."))
pris2 = float(input("Hvor mye koster denne varen? Skriv inn som flyttall."))

# Setter inn varene og prisene i ordboka og spør brukern om to ulike varer og
# priser som jeg da setter inn i 4 variabler

#Oppgave2.2
varerButikk[vare] = pris
varerButikk[vare2] = pris2
print(varerButikk)

# Setter variablene så inn i orboka for så printe ut det hele. 
