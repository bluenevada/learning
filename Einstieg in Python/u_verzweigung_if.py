mi = 0.22
mj = 0.18
a = 2500

print("Bitte Gehalt in Euro angeben:")
zahl = float(input())

if zahl > a:
    print("Es ergibt sich eine Steuer von", mi * zahl, "Euro")
else:
    print("Es ergibt sich eine Steuer von", mj * zahl, "Euro")