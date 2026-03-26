lista = []

while True:
    arvo = int(input("uusi arvo:"))

    if arvo == 0:
        print("hei hei!")
        break

    lista.append(arvo)

    print("lista nyt:", lista)
    print("lista järjestyksessä", sorted (lista))
