import matplotlib.pyplot as plt
import numpy as np

# Dane symulacyjne: Fitness dla 10 uruchomień
generations = np.arange(1, 201)  # 200 pokoleń
best_fitness = np.random.uniform(290, 300, len(generations))  # Najlepsze wartości fitness
worst_fitness = np.random.uniform(310, 330, len(generations))  # Najgorsze wartości fitness
mean_fitness = (best_fitness + worst_fitness) / 2  # Średnie wartości fitness
std_dev = np.random.uniform(2, 5, len(generations))  # Odchylenie standardowe

# Wykres wyników
plt.figure(figsize=(12, 8))

# Najlepszy fitness
plt.plot(generations, best_fitness, label="Najlepszy fitness", color="blue", linestyle="-", linewidth=1.5)

# Najgorszy fitness
plt.plot(generations, worst_fitness, label="Najgorszy fitness", color="red", linestyle="--", linewidth=1.5)

# Średni fitness z odchyleniami standardowymi
plt.plot(generations, mean_fitness, label="Średni fitness", color="green", linestyle="-.", linewidth=1.5)
plt.fill_between(
    generations,
    mean_fitness - std_dev,
    mean_fitness + std_dev,
    color="green",
    alpha=0.2,
    label="Odchylenie standardowe",
)

# Dostosowanie wykresu
plt.title("Postęp algorytmu genetycznego podczas ewolucji", fontsize=16)
plt.xlabel("Pokolenia", fontsize=14)
plt.ylabel("Wartość fitness (długość trasy)", fontsize=14)
plt.legend(fontsize=12)
plt.grid(alpha=0.6)
plt.tight_layout()

# Zapis wykresu do pliku
plt.savefig("algorytm_genetyczny_wyniki.png")
plt.show()
