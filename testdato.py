day = int (input("Si meg en random dag!"))
month = int (input("Si meg en random maaned!"))
newday = int (input("Si meg en dag til!"))
newmonth = int (input("Si meg en maaned til!"))

if month < newmonth:
 print("Riktig Rekefølge!")
elif month > newmonth:
 print("Feil Rekefølge!")
else:
  if day < newday:
   print("Riktig Rekefølge")
  elif day > newday:
   print("Feil Rekefølge")
  else:
    print("Samme Rekefølge!")