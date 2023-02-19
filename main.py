import random as ra

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

print("Ovo je igra vesala u kojoj je poenta pogoditi slova, a time i celu rec. Medjutim, postoji odredjeni broj gresaka koji omogucavaju da igra traje. Nakon vise od pet pogresno izabranih slova, igra se zavrsava. Srecno!")
print("I hate my life")


greske = 0


o = ["me", "development", "coincide", "monopoly", "ordinary", "chance", "volume","building", "trolley", "vein"]

izabranaRec = ra.choice(o)
pogodjenaRec = ""

# Koliko Slova toliko zvezdica
for c in izabranaRec:
    pogodjenaRec += "*"

pogodjenaRec = list(pogodjenaRec)
while greske < 5:
    x = input("Unesite odgovarajuce slovo: ")
    foundIndexes = find(izabranaRec, x)
    if len(foundIndexes) == 0:
        greske += 1
        print("Greska: " + str(greske))
    else:
        for index in foundIndexes:
            pogodjenaRec[index] = x
    print("".join(pogodjenaRec))

    if "".join(pogodjenaRec) == izabranaRec:
        print("Bravo care")
        break

print("Kraj igre")