def temperature():
    
    print("=" * 60)
    
    celsius = float(input("Temperature en Celsius : "))
    
    fahrenheit = (celsius * 9 / 5) + 32
    
    print(f"{celsius} degres C = {fahrenheit:.2f} degres F")
    
    print("\nTests de verification :")
    
    assert (0 * 9/5) + 32 == 32.0, "Erreur : 0 degres C devrait etre 32 degres F"
    
    assert (100 * 9/5) + 32 == 212.0, "Erreur : 100 degres C devrait etre 212 degres F"
    
    print("Formule correcte !")

if __name__ == "__main__":
    
    temperature()