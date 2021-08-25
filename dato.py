day = input("Si meg en random dag!")
month = input("Si meg en random maaned!")
newday = input("Si meg en dag til!")
newmonth = input("Si meg en maaned til!")
if day + month < newday + newmonth:
 print("Riktig rekefolge!")
 if day + month > newday + newmonth:
  print("Feil Rekefolkge!")
if day + month == newday + newmonth:
    print("Samme dato!")