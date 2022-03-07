from datasenter import Datasenter

def hovedprogram():                                         #Setter opp hovedprogrammet
    datasenter = Datasenter()

    filnavn = ['abel.txt','saga.txt']                       #Navn på fil
    
    for fil in filnavn:                                     #For-løkke som iterer gjennom de ulike filene
        datasenter.lesInnRegneklynge(fil)

    datasenter.skrivUtRegneklynge("abel")                   #Skriver ut informasjon fra abel.txt
    datasenter.skrivUtRegneklynge("saga")                   #Skriver ut informasjon fra saga.txt

hovedprogram()                                              #Kjører hovedprogrammet