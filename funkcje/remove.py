import math
import matplotlib.pyplot as plt
import numpy as np
import json


def usuwanie_pomiaru(numer_pomiaru):
    with open("data/dane.json") as file:
        file_data = json.load(file)
        pomiary = file_data.get("pomiary", [])
        pomiary = [p for p in pomiary if p.get("numer_pomiaru") != numer_pomiaru]
        file_data["pomiary"] = pomiary
    with open("data/dane.json", "w") as file:
        json.dump(file_data, file, indent=4)
        

def main():
    numer_pomiaru = int(input("Podaj numer pomiaru do usunięcia: "))
    usuwanie_pomiaru(numer_pomiaru)
    print(f"Pomiar o numerze {numer_pomiaru} został usunięty.")
    
if __name__ == "__main__":
    main()