ika = int(input("Kuinka vanha olet? "))

if ika >= 65:
    print("Olet eläkkeellä!")

elif ika >= 18:
    print("Olet työikäinen!")
elif ika >= 7:
    print("olet kouluikäinen!")
else:
    print("Olet pieni lapsi.")
