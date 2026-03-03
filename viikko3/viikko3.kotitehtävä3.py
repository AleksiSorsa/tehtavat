sp = input("Anna sukupuolesi (n/m): ")
hg = int(input("Anna hemoglobiiliarvosi: "))

if sp == "n":
    if hg < 117:
        print("hemoglobiinisi on alhainen")
    elif 117 <= hg <= 175:

    else:
        print("hemoglobiinisi on korkea")

elif sp == "m":
    if hg < 134:
        print("hemoglobiinisi on alhainen")
    elif 134 <= hg <= 195:

    else:
        print("hemoglobiinisi on korkea")
else:
    print("Virheellinen sukupuoli")
