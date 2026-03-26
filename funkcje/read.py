import math
import matplotlib.pyplot as plt
import numpy as np
import json



def read_data_from_json(file_path):
    global jednostka
    jednostka = input("Podaj jednostkę pomiaru do wyświetlenia: ")
    i = 0
    with open(file_path) as file:
        file_data = json.load(file)
    x_values = []
    y_values = []
    for pomiar in file_data.get("pomiary", []):
        if pomiar.get("jednostka") != jednostka:
            continue
        else:
            x_values.append(i)
            y_values.append(pomiar.get("wartosc"))
            i += 1
    return x_values, y_values

def wykres(x,y, file_data):
    
    odchylenie_standardowe = np.std(y)
    
    plt.plot(x, y, marker='o')
    plt.title(f"Wykres pomiarów w {jednostka}")
    plt.xlabel("Numer pomiaru")
    plt.ylabel("Wartość pomiaru")
    plt.plot(x, [np.mean(y)]*len(x), color='red', linestyle='--', label='Średnia')
    plt.fill_between(x, np.mean(y) - odchylenie_standardowe, np.mean(y) + odchylenie_standardowe, color='red', alpha=0.2, label='Odchylenie standardowe')
    plt.legend()
    plt.grid()
    plt.show()

def main():

    x, y = read_data_from_json("data/dane.json")
    print("Liczba pomiarów:", len(x),jednostka)
    print("Średnia wartość pomiarów:", sum(y) / len(y),jednostka)
    print(f"Największa wartość pomiaru: {max(y)} {jednostka}")
    print(f"Najmniejsza wartość pomiaru: {min(y)} {jednostka}")
    with open("data/dane.json") as file:
        file_data = json.load(file)
    
    wykres(x, y, file_data)
    
if __name__ == "__main__":
    main()