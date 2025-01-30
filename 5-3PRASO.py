nummer = input("Skriv personnummer: ")

kön = int(nummer[-2])

if kön%2 == 0:
    print("Kvinna")
else:
    print("Mann")