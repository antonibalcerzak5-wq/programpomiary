import math
import matplotlib.pyplot as plt
import numpy as np
import json


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
    numer_pomiaru = 0
    file = open("data/dane.json")
    file_data = json.load(file)
    numer_pomiary = file_data["pomiary"]
    jednostka = input("Podaj jednostkę pomiaru: ")
    wartosc = float(input("Podaj wartość pomiaru: "))
    
    
    while wartosc != "":
        numer_pomiaru += 1
        wartosc = float(input("Podaj wartość pomiaru: "))
        dodaj_pomiar(wartosc, jednostka, numer_pomiaru)
        
def main():
    zbieranie_pomiaru()
    
if __name__ == "__main__":
    main()        

