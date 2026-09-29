def convert_temperature(value, unit):
    unit = unit.strip().upper()
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
    else:
        return None


print("======= KONVERSI SUHU =======")

input_suhu = float(input("Masukkan nilai suhu: "))
unit = input("Masukkan satuan suhu ('C' untuk Celcius atau 'F' untuk Fahrenheit): ").strip().upper()
konversi = convert_temperature(input_suhu, unit)

if konversi is None:
    print("Satuan tidak dikenal. Gunakan 'C' atau 'F'.")
elif unit == 'C':
    print(f"{input_suhu}°C = {konversi:.2f}°F")
else:
    print(f"{input_suhu}°F = {konversi:.2f}°C")