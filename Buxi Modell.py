input = int( input("bitte zahl eingeben"))
for i in range(2,10):
    calc = input *i
    print(str(input) + "*" + str(i) + " = " + str(calc))
    input =calc

for i in range(9,1,-1):
    calc = input /i
    print(str(input) + "/" + str(i) + " = " + str(calc))
    input = calc