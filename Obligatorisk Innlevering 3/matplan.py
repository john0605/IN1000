#Oppgave4.1/4.2
ordbokBeboer = {"ivar" : ["pannekaker", "kyllingsalat", "oksesteik"],
        "kari nordmann" : ["brød", "egg", "pølser"]}

def beboerMatplan():
    print("navnet på beboerne er:", ordbokBeboer.keys())
    navnBeboer = input("Skriv inn navnet til en beboer.")
    if navnBeboer in ordbokBeboer:
        print(navnBeboer, "spiser", ordbokBeboer[navnBeboer])
    else:
        print("Vi har desverre ikke navnet i systemet vårt.")

beboerMatplan()

# Jeg satt opp en prosedyre som forteller navna på de som er i ordboka og tar
# imot navn fra brukeren og skriver ut hva personen spiser. 

"""
Oppgave4.3
a) Jeg hadde nok brukt liste. Siden det bare er navn så vil det være enklere å
kunne liste og søke opp. Det er bare enkelt og presist.

b) For denne hadde jeg brukt ordbok. Med navn som "key" og poeng som "value" så
vil det kunne være lett å søke opp hvor mange poeng mann har fått.

c) Har hadde jeg bare brukt liste ettersom det bare er navn.

d) Jeg hadde brukt ordbok. Hadde satt opp mat som "key" og deretter navn på alle
som er allergisk mot det.
"""
