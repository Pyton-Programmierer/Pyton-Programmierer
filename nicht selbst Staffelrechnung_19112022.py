benutzereingabe = input("bitte zahl eingeben") # Eingabe der Zahl die berechnet wird
print(type(benutzereingabe))
print("eingegeben wurde: " + benutzereingabe)  # Ausgabe der Zahl die eingegeben wurde
benutzereingabe = int(benutzereingabe)
input = int( input("bitte zahl eingeben"))
for i in range(2,10):
    calc = input *i
    print(str(input) + "*" + str(i) + " = " + str(calc))
    input =calc

for i in range(9,1,-1):
    calc = input /i
    print(str(input) + "/" + str(i) + " = " + str(calc))
    input = calc

