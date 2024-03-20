import math
Seite_a = float(input("Gib die Seite a ein "))
Seite_b = float(input("Gib die Seite b ein "))
Seite_c = (Seite_a ** 2) + (Seite_b ** 2)
print("Die Diagonale beträgt " + str(math.sqrt(Seite_c)))
