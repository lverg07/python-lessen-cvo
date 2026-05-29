getal_1 = int(input("Voer het eerste gehele getal in:"))
getal_2 = int(input("Voet het tweede gehele getal in:"))

# Berekening

som = getal_1 + getal_2
verschil = getal_1 - getal_2
product = getal_1 * getal_2

# Resultaat

print(f"Som: {som}")
print(f"Verschil: {verschil}")
print(f"Product: {product}")

#Deel 2

if getal_1 %2 == 0:
    print("Getal is even")
else:
    print("Getal is oneven")

# Berekening

kwadraat = getal_1 ** 2

print(f"Kwadraat: {kwadraat}")