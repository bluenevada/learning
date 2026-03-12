mi = 0.22
mj = 0.18
mk = 0.26
a = 2500
b = 4000

print("Bitte Gehalt in Euro angeben:")
zahl = float(input())

if zahl > b:
    print("Es ergibt sich eine Steuer von", mk * zahl, "Euro ")
    print("Mit", mk *100, "Prozent")
elif zahl > a:
    print("Es ergibt sich eine Steuer von", mi * zahl, "Euro")
    print("Mit", mi *100, "Prozent")
else:
    print("Es ergibt sich eine Steuer von", mj * zahl, "Euro")
    print("Mit", mj *100, "Prozent")