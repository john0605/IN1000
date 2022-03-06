# Oppgave 4
from dato import Dato                                           #Henter klassen Dato fra dato.py

def hovedprogram():                                             #Definerer hovedprogram()
    dato1 = Dato(15,8,2021)                                     #Setter inn verdier for instansvariablene
    print(dato1.lesÅr())                                        #Del oppgave 3b: skriver ut året   

    if dato1.sjekk(15):                                         #Del oppgave 3c: skrier ut dersom dag er lik 15
        print("Lønningdag! ")
    elif dato1.sjekk(1):
        print("Ny måned, nye muligheter ")
    
    lagretDato1 = dato1.skriverUtDato()                         #Del oppgave 3d: Lagrer datoen som en streg
    print(lagretDato1)                                          #Skriver ut datoen

    nyDag1 = int(input("Tast inn en dag: "))                    #Del oppgave 3g: leser inn dato fra brukeren
    nyMåned1 = int(input("Tast inn en måned: "))
    nyttÅr1 = int(input("Tast inn et år: "))
    dato2 = Dato(nyDag1, nyMåned1, nyttÅr1)                     #Setter den opp som dato2 og kjører den gjennom sjekkFørEllerEtter metoden. 
    print(f'Datoen: {dato2.skriverUtDato()} kommer {dato1.sjekkFørEllerEtter(nyDag1, nyMåned1, nyttÅr1)} den nye datoen:{dato1.skriverUtDato()}.')

hovedprogram()                                                  #Kjører hovedprogram()