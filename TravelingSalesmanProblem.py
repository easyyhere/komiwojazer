import random
import numpy as np
from deap import base, creator, tools, algorithms

# Funkcja do obliczenia dystansu między dwoma miastami
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Funkcja celu (fitness) - minimalizacja długości trasy
def fitness_function(individual, cities):
    total_distance = 0
    for i in range(len(individual)):
        city1 = cities[individual[i]]
        city2 = cities[individual[(i + 1) % len(individual)]]
        total_distance += distance(city1, city2)
    return total_distance,

# Konfiguracja algorytmu genetycznego
def main():
    # Współrzędne 10 miast
    cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(10)]

    # Tworzymy typ minimalizujący, bo chcemy minimalizować dystans
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # -1.0 oznacza minimalizację
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()

    # Osobnik (individual) to permutacja miast
    toolbox.register("indices", random.sample, range(len(cities)), len(cities))
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Rejestracja operacji genetycznych
    toolbox.register("mate", tools.cxOrdered)  # Krzyżowanie typu ordered (zachowuje permutację)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)  # Mutacja przez zamianę miejsc
    toolbox.register("select", tools.selTournament, tournsize=3)  # Selekcja turniejowa
    toolbox.register("evaluate", fitness_function, cities=cities)  # Funkcja oceny

    # Inicjalizacja populacji
    population = toolbox.population(n=300)  # Populacja składająca się z 300 osobników

    # Algorytm ewolucyjny (EA Simple)
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=200, verbose=False)

    # Znalezienie najlepszego rozwiązania
    best_individual = tools.selBest(population, k=1)[0]
    print(f"Najlepsza trasa: {best_individual}")
    print(f"Długość trasy: {fitness_function(best_individual, cities)[0]}")

    # Wypisz współrzędne miast dla wizualizacji
    for i, city in enumerate(best_individual):
        print(f"Miasto {i}: {cities[city]}")

if __name__ == "__main__":
    main()
