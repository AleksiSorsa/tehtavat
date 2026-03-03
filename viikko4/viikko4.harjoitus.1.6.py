summa = 0

while True:
    luku = int(input("anna joku luku, -1 lopettaa: "))

    if luku == -1:
        break
    elif luku >= 10:
        continue

    summa += luku

print("Summa on", summa)