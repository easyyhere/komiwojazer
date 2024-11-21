import matplotlib.pyplot as plt

# Współrzędne miast
cities = [(87, 58), (84, 58), (97, 87), (84, 86), (45, 69),
          (27, 19), (45, 22), (64, 45), (93, 39), (100, 33)]

# Najlepsza trasa (kolejność odwiedzanych miast)
best_route = [1, 0, 4, 7, 3, 8, 6, 2, 9, 5]

# Rysowanie miast
x_coords = [cities[i][0] for i in best_route]
y_coords = [cities[i][1] for i in best_route]

# Dodajemy punkt początkowy, żeby zamknąć trasę
x_coords.append(cities[best_route[0]][0])
y_coords.append(cities[best_route[0]][1])

# Tworzymy wykres
plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, 'o-', label="Trasa komiwojażera")
plt.scatter(x_coords, y_coords, color='red')

# Dodajemy etykiety dla miast
for i, city in enumerate(best_route):
    plt.text(cities[city][0], cities[city][1], f'Miasto {city}')

plt.xlabel("Współrzędna X")
plt.ylabel("Współrzędna Y")
plt.title("Najlepsza trasa komiwojażera")
plt.legend()
plt.grid(True)
plt.show()
