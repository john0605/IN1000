#Oppgave1.1
def addisjon(x,y):
    sum = x + y
    return sum

def delOppgave1_1():
    assert addisjon(1,3)
    assert addisjon(1,-6)
    assert addisjon(-9,-4)
    print(addisjon(5,10))

delOppgave1_1()

#Oppgave1.2
def subtraksjon(x,y):
    differansen = y - x
    return differansen

def divisjon(x,y):
    kvotient = x / y
    return kvotient

def delOppgave1_2():
    assert subtraksjon(20,50)
    assert subtraksjon(10,-4)
    assert subtraksjon(-20,-10)
    print(subtraksjon(5,10))

    assert divisjon(5,8)
    assert divisjon(3,-2)
    assert divisjon(-999,-9)
    print(divisjon(5,10))

delOppgave1_2()

# Jeg definerer de tre funksjonene med to parametre for så returnere svaret. Deretter setter jeg opp prosedyrer som 
# assereter de tre fuksjonene og printer ut det jeg har brukt som verdier.

#Oppgave1.3
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    centiMeter = antallTommer * 2.54
    return centiMeter

def delOppgave1_3():
    print(tommerTilCm(50))

delOppgave1_3()

# Løsner denne oppgaven på samme måte men her asserter jeg slik at tallet er over 0. Dersom tallet er 0 så vil det
# skje en assertion error. 

#Oppgave1.4
def skrivBeregninger():
    x = int(input("Skriv inn tall1:"))
    y = int(input("Skriv inn tall2:"))
    print("Resulat av summering:", addisjon(x,y))
    print("Resulat av subtraksjon:", subtraksjon(x,y))
    print("Resulat av divisjon:", divisjon(x,y))

    print("Konvertering fra tommer til cm:")
    antallTommer = int(input("Skriv inn et tall:"))
    print("Resulat:", tommerTilCm(antallTommer))

skrivBeregninger()

# Setter opp en prosedyre her som vil kunne innhente verdier fra brukeren som kan bruker inn i de ulike funksjonene
# for så returne de til brukeren. 
