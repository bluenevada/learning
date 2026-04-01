print("What do you want to calculate?")
print("Type 1 for bin - hex")
print("Type 2 for hex - bin")
print("Type 3 for dez - bin")
print("Type 4 for bin - dez")
print("Type 5 for dez - hex")
print("Type 6 for hex - dez")

type = input()
type = int(type)

#bin-hex
if type == 1:
    print("Enter a binary number:")
    bin_num = input()
    bin_num = int(bin_num, 2)
    hex_num = hex(bin_num)
    hex_num = hex_num.lower().lstrip("0x")
    print(hex_num)

#hex-bin
elif type == 2:
    print("Enter a hexadecimal number:")
    hex_num = input()
    hex_num = int(hex_num, 16)
    bin_num = bin(hex_num)
    bin_num = bin_num.lower().lstrip("0b")
    print(bin_num)

#dez-bin
elif type == 3:
    print("Enter a hexadecimal number:")
    dez_num = input()
    dez_num = int(dez_num)
    bin_num = bin(dez_num)
    bin_num = bin_num.lower().lstrip("0b")
    print(bin_num)
#bin-dez
elif type == 4:
    print("Enter a binary number:")
    bin_num = input()
    bin_num = int(bin_num, 2)
    dez_num = int(bin_num)
    print(dez_num)

#dez-hex
elif type == 5:
    print("Enter a hexadecimal number:")
    dez_num = input()
    dez_num = int(dez_num)
    hex_num = hex(dez_num)
    hex_num = hex_num.lower().lstrip("0x")
    print(hex_num)

#hex-dez
elif type == 6:
    print("Enter a binary number:")
    hex_num = input()
    hex_num = int(hex_num, 16)
    dez_num = int(hex_num)
    print(dez_num)

else:
    print("Invalid input!")