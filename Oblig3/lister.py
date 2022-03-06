#Oppgave1.1
minListe = [2, 6, 9]
minListe.append(4)
print(minListe[0] , minListe[2])

# Ført inn en liste med tre tall, så printet ut første og siste ledd.

#Oppgave1.2
navnListe = []
input("Hei, tast inn fire navn men først tast inn ok hvis du har skjønt oppgaven.")
navn1 = str(input("Navn1:"))
navn2 = str(input("Navn2:"))
navn3 = str(input("Navn3:"))
navn4 = str(input("Navn4:"))
alleNavn = navn1, navn2, navn3, navn4
navnListe.append(alleNavn)

# Lagde inputs for hvert navn og samla det i en funksjon som jeg legger til i en liste.

#Oppgave1.3
if navn1 == "john":
    print("Du husket meg!")
elif navn2 == "john":
    print("Du husket meg!")
elif navn3 == "john":
    print("Du husket meg")
elif navn4 == "john":
    print("Du husket meg!")
else:
    print("Glemte du meg?")

# Sjekker om navnet mitt passer inn med inputen.

#Oppgave1.4
summen_minListe = minListe[0] + minListe[1] + minListe[2] + minListe[3]
produkt_minListe = minListe[0] * minListe[1] * minListe[2] * minListe[3]

nyListe = [summen_minListe, produkt_minListe]
minListe.extend(nyListe)
print(minListe)
minListe.pop(5)
minListe.pop(4)
print(minListe)

# Lagde først to variabler som jeg legger til i en liste for så samle det i en
# liste med den første listen ved bruken av extend, så fjernet jeg de siste to ledd.
