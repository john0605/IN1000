#Oppgave 3.1
d1 = input("Hva er datoen idag? men bare dag:")
m1 = input("Hva er datoen idag? men bare måned:")
d2 = input("Når er bursdagen din? men bare dag:")
m2 = input("Når er bursdagen din? men bare måned:")

#Oppgave 3.2
if m1 == m1 < m2:
    print("Riktig rekkefølge!")
elif m1 == m2:
    if d1 < d2:
        print("Riktig rekkefølge!")
    elif d1 == d2:
        print("Sammen dato!")
    else:
        print("Feil dato!")
else:
    print("Feil dato!")

"""

Begynte med inputs for hver dag/dato. Dersom m1 er større enn m2 så blir det jo
riktig dato uansett.
Dersom det ikke går så brukte jeg elif for å spesifere hvilke dag som kommer
først og dersom det er feil så brukte jeg else.

"""
