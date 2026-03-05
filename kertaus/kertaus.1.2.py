tuntipalkka = int(input("mikä on tuntipalkkasi?:"))
print("tuntipalkka:", tuntipalkka)

tehdyt_tunnit = int(input("Montako tuntia teit?:"))
print("tehdyt_tunnit:", tehdyt_tunnit)

paiva =  input("Mikä päivä on:?")
print("paiva:", paiva)

if  paiva == 'sunnuntai':
    paivapalkka = tuntipalkka * 2 * tehdyt_tunnit
else:
    paivapalkka = tuntipalkka * tehdyt_tunnit
print("paivapalkka", paivapalkka)

