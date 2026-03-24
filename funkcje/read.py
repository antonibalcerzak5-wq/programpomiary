import math
import matplotlib.pyplot as plt
import numpy as np
import json



def read_data_from_json(file_path):
    with open(file_path) as file:
        file_data = json.load(file)
    x_values = []
    y_values = []
    for pomiar in file_data.get("pomiary", []):
        x_values.append(pomiar.get("numer_pomiaru"))
        y_values.append(pomiar.get("wartosc"))
    return x_values, y_values

def wykres(x,y, file_data):
    
    plt.plot(x, y, marker='o')
    plt.title(f"Wykres pomiarów w {file_data.get('pomiary', [{}])[0].get('jednostka', '')}")
    plt.xlabel("Numer pomiaru")
    plt.ylabel("Wartość pomiaru")
    plt.grid()
    plt.show()

def main():
    x, y = read_data_from_json("data/dane.json")
    print("Liczba pomiarów:", len(x))
    print("Średnia wartość pomiarów:", sum(y) / len(y))
    with open("data/dane.json") as file:
        file_data = json.load(file)
    wykres(x, y, file_data)
    
if __name__ == "__main__":
    main()