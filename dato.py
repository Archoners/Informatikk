#Få verdien av alle 4 variabler. Bruker int fordi vi vill bare ha heltall.
day = int (input("Si meg en random dag!"))
month = int (input("Si meg en random maaned!"))
newday = int (input("Si meg en dag til!"))
newmonth = int (input("Si meg en maaned til!"))
#Sjekker om variabelen for "Month" er mindre enn "newmonth". Fordi det er bare snakk om dag og måned og ikke år, det er mulig å få vite om det er riktig rekefølge ved at month er mindre enn new month.
if month < newmonth:
 print("Riktig Rekefølge!")
 #Samme som forrige men bare omvendt. Fordi det er ingen snakk om år så vet vi at det er feil rekefølge ved kunnskapen at newmonth er mindre enn month
elif month > newmonth:
 print("Feil Rekefølge!")
else:
  #Hvis month og new month er lik (=) da sjekker programmet dagene, same prinsippet følges her og 
  if day < newday:
   print("Riktig Rekefølge")
   
  elif day > newday:
   print("Feil Rekefølge")
   #Else kommando brukes her for situasjoner hvor rekefølgen er samme (=). Fordi vi har bare <,> og = så er det mulig å bruke else
  else:
    print("Samme Rekefølge!")