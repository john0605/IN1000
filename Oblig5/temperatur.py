#Oppgave4.1
def temperaturPerMåned(temperaturMåned):
    minFil = open(temperaturMåned)
    ordbok = {}
    for x in minFil:
        månedTemp = x.split(",")
        ordbok[månedTemp[0]] = float(månedTemp[1])
    minFil.close()
    return ordbok

print(temperaturPerMåned("max_temperatures_per_month.csv"))


#Oppgave4.2
def nyTemperaturRekord(varmesteTempratur, filnavn):
    minFil2 = open(filnavn)
    for y in minFil2:
        dagligTemperatur = y.split(",")
        dato = (f'{dagligTemperatur[1]} {dagligTemperatur[0]}')
        dato1 = dagligTemperatur[0]
        for key in varmesteTempratur:
            if key == dato1:
                if varmesteTempratur[key] < float(dagligTemperatur[2]):
                    varmesteTempratur[key] = float(dagligTemperatur[2])
                    print(f'Nye varmerekorden er {dato}:'
                          f'{dagligTemperatur[2]}grader Celcius')
    minFil2.close()
    return varmesteTempratur

varmesteMåned = nyTemperaturRekord(temperaturPerMåned("max_temperatures_per_month.csv"),
                  "max_daily_temperature_2018.csv")


#Oppgave4.3
def oppdatertOrdbok(ordbok, filnavn):
    minFil3 = open(filnavn, "w")
    for key in ordbok:
        minFil3.write(key)
        minFil3.write(",")
        minFil3.write(str(ordbok[key]))
    minFil3.close()
    return ordbok

oppdatertOrdbok(varmesteMåned, "max_daily_temperature_20.csv")