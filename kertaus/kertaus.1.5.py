print("1: yhteenlasku")
print("2: vähennyslasku")
print("3: kertolasku")
print("4: jakolasku")
print("0: lopetus")

while True:
    valinta = input("Valitse 1-4 tai 0 lopettaaksesi ohjelman:")

    if valinta == "0":
        break

    if valinta == "1" or valinta == "2" or valinta == "3" or valinta == "4":
        luku1 = int(input("Anna luku1)"))
        luku2 = int(input("Anna luku2"))
        if valinta == "1":
            tulos = luku1 + luku2
            print(f"tulos: {luku1} + {luku2} = {tulos}"

elif valinta == "2":
            tulos = luku1 - luku2
            print(f"Tulos: {luku1} - {luku2} = {tulos}")

elif valinta == "3":
            tulos = luku1 * luku2
            print(f"Tulos: {luku1} * {luku2} = {tulos}")

elif valinta == "4":
    if luku2 != 0:
        tulos = luku1 / luku2
        print(f"Tulos: {luku1} / {luku2} = {tulos}")
        else:
        print("Nollalla ei voi jakaa")
        else:
        print("Virheellinen valina")





















luku1 = int(input("Anna luku1,'Lopeta, lopettaa.:"))
luku2 = int(input("Anna luku2:"))
lasku= input("Minkä laskun haluat tehdä:")

while True:
    if:
        yhteenlasku= (luku1 + luku2)
        vähennyslasku= (luku1 - luku2)
        kertolasku= (luku1 * luku2)
        jakolasku= (luku1 / luku2)

    else:
        break
