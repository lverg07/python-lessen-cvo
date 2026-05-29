klant = input("Naam klant:")
aantal_producten = int(input("Aantal producten:"))
if aantal_producten < 0:
    print("Fout: Aantal producten kan niet minder dan 0 zijn.")
else:
    prijs_per_stuk = float(input("Prijs per stuk:"))
    # Berekent
    subtotaal = aantal_producten * prijs_per_stuk
    BTW_bedrag = subtotaal * float(input("BTW-percentage:"))
    totaalbedrag = subtotaal + BTW_bedrag

    afgerond_prijs_per_stuk = round(prijs_per_stuk,2)
    afgerond_subtotaal = round(subtotaal,2)
    afgerond_BTW_bedrag = round(BTW_bedrag,2)
    afgerond_totaalbedrag = round(totaalbedrag,2)

    print(f"=" * 40)
    print(f"Factuur voor: {klant} NV")
    print(f"Aantal producten: {aantal_producten}")
    print(f"Prijs per stuk: € {afgerond_prijs_per_stuk}")
    print(f"=" * 40)
    print(f"Subtotaal: € {afgerond_subtotaal}")
    print(f"BTW (21%): €{afgerond_BTW_bedrag}")
    print(f"TOTAAL: {afgerond_totaalbedrag} ")
    print(f"=" * 40)