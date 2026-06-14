# calculator_menu.py – gemaakt door Lobke Vergauwen

while True:
    print("=" * 45)
    print("        Calculator Menu")
    print("=" * 45)
    print("1) BTW berekenen")
    print("2) Temperatuur omrekenen")
    print("3) Stoppen")
    print("=" * 45)

    keuze = input("Maak een keuze (1/2/3): ")

    if keuze == "1":
        print("\n--- BTW berekenen ---")

        bedrag = float(input("Voer het bedrag in excl. BTW (€): "))
        tarief = int(input("Welk BTW-tarief? (6, 12 of 21): "))

        btw = bedrag * (tarief / 100)
        totaal = bedrag + btw

        print("-" * 45)
        print(f"Bedrag excl. BTW : €{bedrag:.2f}")
        print(f"BTW ({tarief}%)        : €{btw:.2f}")
        print(f"Totaal incl. BTW : €{totaal:.2f}")
        print("-" * 45)

    elif keuze == "2":
        print("\n--- Temperatuur omrekenen ---")
        print("1) Fahrenheit naar Celsius")
        print("2) Celsius naar Fahrenheit")

        temp_keuze = input("Maak een keuze (1/2): ")

        if temp_keuze == "1":
            fahrenheit = float(input("Geef temperatuur in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9

            print(f"{fahrenheit}°F = {celsius:.1f}°C")

        elif temp_keuze == "2":
            celsius = float(input("Geef temperatuur in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32

            print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")

        else:
            print("Ongeldige temperatuurkeuze.")

    elif keuze == "3":
        print("Programma wordt afgesloten. Tot de volgende keer!")
        break

    else:
        print("Ongeldige keuze. Kies 1, 2 of 3.")

    print()