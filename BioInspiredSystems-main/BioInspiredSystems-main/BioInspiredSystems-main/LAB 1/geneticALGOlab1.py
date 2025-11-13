import random

# Parameters
POP_SIZE = 4              # Number of chromosomes in the population
CHROMOSOME_LENGTH = 5     # Each chromosome is a string of 5 bits
GENERATIONS = 10          # Number of generations to evolve
MUTATION_RATE = 0.1       # Chance of a bit flipping
CROSSOVER_RATE = 0.7      # Chance of crossover between two parents

# Fitness function: higher value for larger numbers (x^2)
def fitness(x):
    return x ** 2

# Generate a random binary chromosome
def random_chromosome():
    return ''.join(random.choice('01') for _ in range(CHROMOSOME_LENGTH))

# Flip a bit with a given mutation rate
def mutate(chromosome):
    new_bits = []
    for bit in chromosome:
        if random.random() < MUTATION_RATE:
            new_bits.append('1' if bit == '0' else '0')  # Flip the bit
        else:
            new_bits.append(bit)
    return ''.join(new_bits)

# Perform crossover between two parents
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, CHROMOSOME_LENGTH - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
    else:
        child1, child2 = parent1, parent2
    return child1, child2

# Initialize population with random chromosomes
population = [random_chromosome() for _ in range(POP_SIZE)]

# Run the algorithm for a set number of generations
for generation in range(GENERATIONS):
    print(f"Generation {generation + 1}:")

    # Calculate fitness for each chromosome
    fitness_scores = [fitness(int(ch, 2)) for ch in population]
    for ch, score in zip(population, fitness_scores):
        print(f"  {ch} -> Fitness: {score}")

    # Select parents using roulette wheel selection
    total_fitness = sum(fitness_scores)
    probabilities = [score / total_fitness for score in fitness_scores]
    selected = random.choices(population, weights=probabilities, k=POP_SIZE)

    # Create new population using crossover and mutation
    new_population = []
    while len(new_population) < POP_SIZE:
        p1, p2 = random.sample(selected, 2)
        c1, c2 = crossover(p1, p2)
        new_population.append(mutate(c1))
        if len(new_population) < POP_SIZE:
            new_population.append(mutate(c2))

    population = new_population  # Move to next generation
    print("  New Population:", population)
    print()

# Final result
best = max(population, key=lambda ch: fitness(int(ch, 2)))
print(f"Best solution: {best} -> Fitness: {fitness(int(best, 2))}")
