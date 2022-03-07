#Oppgave5
"""
5.a) Sett opp en ordbok med tre ulike fotball lag som nøkkelverdi
og landet laget kommer fra som innholdsverdi.

5.b) Hent inn et lag fra brukeren.

5.c) Print ut hele ordoka og skriv at laget som ble inhetet fra brukeren er den
dårligste.

"""

#5.a)
fotballLag = {"manchester united" : "england", "psg" : "frankrike",
            "barcelona" : "spania"}

#5.b)
brukerLag = input("Hvilket lag heier du på")
brukerLand = input("Hvor kommer laget fra")

#5.c)
print(fotballLag, "og den dårligste laget er", brukerLag)
