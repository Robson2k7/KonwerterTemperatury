TEMPERATURE_SCALES = ("fahrenheit", "kelvin", "celsius")

def convert_to_celsius(degrees, source="fahrenheit"):
    if source.lower() ==  "fahrenheit":    # jeśli w funkcji wybierzemy source fahrenheit i podamy wartość degrees to funkcja użyje poniższego wzoru
        return (degrees-32) * (5/9)
    elif source.lower() == "kelvin":       # jeśli w funkcji wybierzemy source kelvin i podamy wartość degrees to funkcja użyje poniższego wzoru
        return degrees - 273.15
    else:
        return f"Nie potrafię przekonwertować z {source}"
    
print("To jest moduł temperature.")

# zdefiniowaliśmy funkcję, którą wywołamy w pliku Jupyter 

# Dodajemy funkcję do konwersji na Fahrenheita
def convert_to_fahrenheit(degrees, source="celsius"):
    if source.lower() == "celsius":
        return degrees * 9/5 + 32
    elif source.lower() == "kelvin":
        return (degrees - 273.15) * 9/5 + 32
    else:
        return f"Nie potrafię przekonwertować z {source}"

# Dodajemy funkcję do konwersji na Kelvina
def convert_to_kelvin(degrees, source="celsius"):
    if source.lower() == "celsius":
        return degrees + 273.15
    elif source.lower() == "fahrenheit":
        return (degrees - 32) * 5/9 + 273.15
    else:
        return f"Nie potrafię przekonwertować z {source}"