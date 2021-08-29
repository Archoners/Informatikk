"""Dette programmet svarer på oppgave 2"""
#Spør brukeren om å oppgi to datoer i form av heltall,
#guider brukeren gjennom prosessen,
#og lagrer brukerens input i egne variabler for dag og dato.
print("Du kommer nå til å bli bedt om å oppgi to datoer")
print("Oppgi dag for første dato i form av et heltall")
dag1 = input()
print("Oppgi måned for første dato i form av et heltall")
måned1 = input()
print("Oppgi dag for andre dato i form av et heltall")
dag2 = input()
print("Oppgi måned for andre dato i form av et heltall")
måned2 = input()

#sjekker hvilken dato som kommer først
if måned1 < måned2:
    print("Riktig rekkefølge")
elif måned1 > måned2:
    print("Feil rekkefølge!")
else:
    if dag1 < dag2:
        print("Riktig rekkefølge!")
    elif dag1 == dag2:
        print("Samme dato!")
    else:
        print("Feil rekkefølge")