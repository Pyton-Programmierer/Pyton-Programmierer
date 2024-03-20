note1 =  int(input("Gib eine Note zwischen 1 und 6 ein "))
note2 =  int(input("Gib eine Note zwischen 1 und 6 ein "))
note3 =  int(input("Gib eine Note zwischen 1 und 6 ein "))
durchschnitt = (note1 +note2 +note3) / 3
print(durchschnitt)
if durchschnitt > 4:
    print("nicht Bestanden")
elif durchschnitt < 4:
    print("Gratuliere Bestanden")    