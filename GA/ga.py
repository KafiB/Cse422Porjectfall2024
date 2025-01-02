import random

population = 100
genome_len = 30
mutation_rate = 0.01  
crossover_rate = 0.7
generations = 200

def random_genome(length):
    return [random.randint(0, 1) for i in range(length)]

def init_population(population_size, genome_len):
    return [random_genome(genome_len) for i in range(population_size)]

def fitness(genome):
    return sum(genome)

def select_parent(population, fitness_values):
    total_fitness = sum(fitness_values)
    pick = random.uniform(0, total_fitness)
    current = 0
    for individual, fitness_value in zip(population, fitness_values):
        current += fitness_value
        if current > pick:
            return individual

def crossover(parent1, parent2):
    if random.random() < crossover_rate:  
        crossover_point = random.randint(1, len(parent1) - 1)
        return (parent1[:crossover_point] + parent2[crossover_point:], 
                parent2[:crossover_point] + parent1[crossover_point:])
    else:
        return parent1, parent2 

def mutate(genome):  
    for i in range(len(genome)):
        if random.random() < mutation_rate:  
            genome[i] = 1 - genome[i]  
    return genome

def genetic_algo():
    pop = init_population(population, genome_len)

    for gen in range(generations):
        fitness_values = [fitness(g) for g in pop]

        new_population = []
        for _ in range(population // 2):
            parent1 = select_parent(pop, fitness_values)
            parent2 = select_parent(pop, fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)])

        pop = new_population
        fitness_values = [fitness(g) for g in pop]
        best_fitness = max(fitness_values)

        print(f"Generation {gen}: Best Fitness = {best_fitness}")

    best_index = fitness_values.index(max(fitness_values))
    best_solution = pop[best_index]
    print(f"Best Solution: {best_solution}")
    print(f"Best Fitness: {fitness(best_solution)}")


genetic_algo()
