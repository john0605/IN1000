#Oppgave3
"""
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)
hovedprogram()

Funksjonen  "minFuksjon()" og prosedyren "hovedprogram()" tar ikke imot noen argumenter. Variablene "a" og "b" innholder to
verdier 42 og 0, og variablen "b" blir printet ut og settes som lik "a". I "minFunksjon()" så har vi en loop inn i der
så har vi variabel "c" som har veriden 3 og dette plusses med 1. Variabel "b" plusses med "a" som ikke er definert ettersom 
funskjonen ikke tar imot noen argumenter. Dette vil få programmet til å stoppe. 

"""