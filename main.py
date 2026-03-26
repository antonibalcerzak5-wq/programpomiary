import math
import matplotlib.pyplot as plt
import numpy as np
import json


def wybor_funkcji():
    print("Wybierz funkcję programu:")
    print("1. Dodaj pomiar")
    print("2. Wyświetl wyniki")
    print("3. Usuń pomiar")
    while True:
        wybor = input("Wprowadź numer funkcji (1 lub 2): ")
        match wybor:
            case "1":
                zbieranie_pomiaru()
                break
            case "2":
                from funkcje.read import main
                main()
                break
            case "3":
                from funkcje.remove import main
                main()
                break
            case _:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

def dodaj_pomiar(wartosc,jednostka,numer_pomiaru):
    
    with open("data/dane.json") as file:
        
        file_data = json.load(file)
        file_data["pomiary"].append({
            "wartosc": wartosc,
            "jednostka": jednostka,
            "numer_pomiaru": numer_pomiaru
        })
    with open("data/dane.json", "w") as file:
        json.dump(file_data, file, indent=4)



def zbieranie_pomiaru():
    with open("data/dane.json") as file:
        file_data = json.load(file)

    pomiary = file_data.get("pomiary", [])
    numer_pomiaru = 0
    if pomiary:
        numer_pomiaru = max((p.get("numer_pomiaru", 0) for p in pomiary), default=0)

    numer_pomiaru += 1
    jednostka = input("Podaj jednostkę pomiaru: ")

    while True:
        wartosc_input = input("Podaj wartość pomiaru (enter aby zakończyć): ")
        if wartosc_input.strip() == "":
            print("Koniec zbierania pomiarów.")
            break
        try:
            wartosc = float(wartosc_input)
        except ValueError:
            print("Nieprawidłowa wartość. Spróbuj ponownie.")
            continue

        dodaj_pomiar(wartosc, jednostka, numer_pomiaru)
        numer_pomiaru += 1
    
    odp = input("Czy chcesz wyświetlić wyniki? (TAK/NIE)")
    if odp.lower() == "tak":
        from funkcje.read import main
        main()
    else:
        print("Dziękuję za skorzystanie z programu.")
        
        
def main():
    wybor_funkcji()
    
if __name__ == "__main__":
    main()        

