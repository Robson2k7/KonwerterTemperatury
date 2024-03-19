import temperature

def main():
    print("Konwerter Temperatury")
    print("Dostępne skale: Celsius, Fahrenheit, Kelvin")
    source_scale = input("Podaj skalę źródłową: ").lower()
    target_scale = input("Podaj skalę docelową: ").lower()
    degrees = float(input("Podaj temperaturę do konwersji: "))
    
    if source_scale == "celsius" and target_scale == "fahrenheit":
        result = temperature.convert_to_fahrenheit(degrees, source="celsius") # z celsjusza na fahrenheita
    elif source_scale == "celsius" and target_scale == "kelvin":
        result = temperature.convert_to_kelvin(degrees, source="celsius") # z celsjusza na kelvina
    elif source_scale == "kelvin" and target_scale == "celsius":
        result = temperature.convert_to_celsius(degrees, source="kelvin") # z kelvina na celsjusza
    elif source_scale == "fahrenheit" and target_scale == "celsius":
        result = temperature.convert_to_celsius(degrees, source="fahrenheit") # z fahrenheita na celsjusza
    elif source_scale == "fahrenheit" and target_scale == "kelvin":
        result = temperature.convert_to_kelvin(degrees, source="fahrenheit") # z fahrenheita na kelvina
    elif source_scale == "kelvin" and target_scale == "fahrenheit":
        result = temperature.convert_to_fahrenheit(degrees, source="kelvin") # z kelvina na fahrenheita
    else:
        result = "Nie obsługiwana konwersja."

    print(f"Wynik konwersji: {result}")

if __name__ == "__main__":
    main()
input("Naciśnij Enter, aby zakończyć...")
