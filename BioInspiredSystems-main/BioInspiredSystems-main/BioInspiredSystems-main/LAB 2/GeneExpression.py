import random

# Parameters
POP_SIZE = 4            # Number of chromosomes in the population
CHROMOSOME_LENGTH = 5   # Length of each chromosome (5 bits)
MUTATION_RATE = 0.1     # Probability of a bit flipping (mutation rate)
CROSSOVER_RATE = 0.7    # Probability of crossover between two parents
GENERATIONS = 10        # Number of generations (iterations)

# Fitness function: f(x) = x^2 (The fitness score is calculated based on the value of X)
def fitness(x):
    return x ** 2  # Fitness is just the square of X

# Convert a binary chromosome (string of 0s and 1s) to decimal (a number)
def binary_to_decimal(chromosome):
    return int(chromosome, 2)  # Convert the binary string to a decimal number

# Mutation: This function flips random bits in a chromosome
def mutate(chromosome):
    new_chromosome = ''
    for bit in chromosome:
        # Flip the bit with the mutation probability
        if random.random() < MUTATION_RATE:
            new_chromosome += '1' if bit == '0' else '0'  # Flip the bit
        else:
            new_chromosome += bit  # Keep the bit the same
    return new_chromosome  # Return the mutated chromosome

# Crossover: This function combines two parent chromosomes to make two children
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:  # If the crossover happens
        point = random.randint(1, CHROMOSOME_LENGTH - 1)  # Random crossover point
        child1 = parent1[:point] + parent2[point:]  # First child
        child2 = parent2[:point] + parent1[point:]  # Second child
        return child1, child2
    else:
        # If no crossover happens, return the parents as children
        return parent1, parent2

# Initial population setup (this is given manually from the table)
population = [
    ('01100', 12, 144),  # Chromosome '01100', X=12, Fitness=144
    ('11001', 25, 625),  # Chromosome '11001', X=25, Fitness=625
    ('00101', 5, 25),    # Chromosome '00101', X=5, Fitness=25
    ('10011', 19, 361)   # Chromosome '10011', X=19, Fitness=361
]

# Run the algorithm for a set number of generations
for generation in range(GENERATIONS):
    print(f"Generation {generation + 1}:")
    
    # Total fitness of the population (sum of all fitness values)
    total_fitness = sum(fitness_val for _, _, fitness_val in population)
    
    # Roulette Wheel Selection: Determine the probability of each chromosome being selected for mating
    probabilities = [fitness_val / total_fitness for _, _, fitness_val in population]
    # Select the chromosomes based on their probabilities
    mating_pool = random.choices(population, probabilities, k=POP_SIZE)

    # Crossover and Mutation: Create the next generation of chromosomes
    offspring = []  # This will store the new population (children)
    for i in range(0, len(mating_pool), 2):
        parent1, parent2 = mating_pool[i], mating_pool[i + 1] if i + 1 < len(mating_pool) else mating_pool[i]
        # Perform crossover between the two parents
        child1, child2 = crossover(parent1[0], parent2[0])
        # Mutate the children (to introduce some randomness)
        offspring.append((mutate(child1), binary_to_decimal(child1), fitness(binary_to_decimal(child1))))
        offspring.append((mutate(child2), binary_to_decimal(child2), fitness(binary_to_decimal(child2))))
    
    # Update the population with the new offspring
    population = offspring

    # Print the population and their fitness after the generation
    print("  Population after crossover and mutation:")
    for chrom, x, fit in population:
        print(f"    Chromosome: {chrom} | X = {x} | Fitness = {fit}")

    # Find the best solution (chromosome with the highest fitness)
    best_solution = max(population, key=lambda x: x[2])  # Get the child with the highest fitness score
    print(f"  Best solution in this generation: Chromosome = {best_solution[0]}, X = {best_solution[1]}, Fitness = {best_solution[2]}")
    print()

# After all generations, print the best solution found
best_overall = max(population, key=lambda x: x[2])
print(f"Best solution after all generations: Chromosome = {best_overall[0]}, X = {best_overall[1]}, Fitness = {best_overall[2]}")

