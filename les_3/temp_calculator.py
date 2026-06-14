# temp_calculator.py – gemaakt door [jouw naam]
print("=" * 40)
print("  Temperatuuromrekening F → C")
print("=" * 40)

fahrenheit = float(input("Geef een temperatuur in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F = {celsius:.1f}°C")

print("=" * 40)
print("  Temperatuuromrekening C → F")
print("=" * 40)

celsius = float(input("Geef een temperatuur in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius:.1f} °C = {fahrenheit:.1f} °F")
