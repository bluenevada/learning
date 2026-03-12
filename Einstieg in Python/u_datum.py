print("Geben Sie den Tag des Datums an:")
day = input()
d = int(day)

print("Geben Sie den Monat des Datums an:")
month = input()
m = int(month)

print("Geben Sie das Jahr des Datums an:")
year = input()
j = int(year)

if (d == 28 and m == 2) 
    or (d == 30 and (m == 4 or m == 6 or m == 9 or m == 11)):
    print("Letzter Tag")

if j % 4 == 0:
    print("Schaltjahr")

if (d < 1 or d > 31) and (m < 1 or m > 12) and (d < 1 or ((d > 28 and m == 2)
                                                          or (d == 29 and m == 2 and j % 4 != 0)) 
     or (d > 30 and (m == 4 or m == 6 or m == 9 or m == 11))):
    print("Ungültiges Datum")
else: 
    print("Gültiges Datum")