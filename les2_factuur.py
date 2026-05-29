klant = input("Naam klant:")
aantal_producten = int(input("Aantal producten:"))
prijs_per_stuk = float(input("Prijs per stuk:"))

# Berekent
subtotaal = aantal_producten * prijs_per_stuk
BTW_bedrag = subtotaal * 0.21
totaalbedrag = subtotaal + BTW_bedrag

print(f"=" * 40)
print(f"Factuur voor: {klant} NV")
print(f"Aantal producten: {aantal_producten}")
print(f"Prijs per stuk: € {prijs_per_stuk}")
print(f"=" * 40)
print(f"Subtotaal: € {subtotaal}")
print(f"BTW (21%): €{BTW_bedrag}")
print(f"TOTAAL: {totaalbedrag} ")
print(f"=" * 40)