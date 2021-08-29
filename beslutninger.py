#Spør brukeren om de vil ha brus
brus = input("Vil du ha brus?")
#bruker .lower() sånn at brukeren skal ha muligheten å skrive ja eller nei på hvilken som helst måte eg. (JA,jA,NEi,nEI osv)
brus = brus.lower()
#Bruke if for å sjekke om brukeren svarer "ja" på om han vil ha brus
if brus == "ja":
    print("Her har du en brus!")
#Samme som forrige men elif sjekker om brukeren skriver nei
elif brus == "nei":
    print("Den er grei.")
#bruker else: kommando for å sjekke om brukeren skriver noe annet enn ja eller nei
else:
    print("Det forstod jeg ikke helt.")
    