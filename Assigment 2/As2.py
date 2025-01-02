import random
import time

# Function to parse the DIMACS file
def parse_dimacs(filename):
    try:
        with open(filename, 'r') as file:
            print("File opened successfully!")
            clauses = []
            variables = set()
            for line in file:
                if line.startswith('c') or line.startswith('p'):
                    continue  # Ignore comments and problem line
                clause = list(map(int, line.split()))
                clauses.append(clause[:-1])  # Ignore the trailing 0
                variables.update(abs(lit) for lit in clause)
            return clauses, sorted(variables)
    except FileNotFoundError:
        print("File not found.")
        return [], []

# Hill Climbing Algorithm
def hill_climbing(clauses, variables):
    assignment = {var: random.choice([True, False]) for var in variables}

    def evaluate(assignment):
        return sum(all(assignment[abs(lit)] != (lit < 0) for lit in clause) for clause in clauses)

    current_score = evaluate(assignment)

    while True:
        neighbors = []
        for var in variables:
            neighbor = assignment.copy()
            neighbor[var] = not neighbor[var]
            neighbors.append(neighbor)

        best_neighbor = max(neighbors, key=lambda neighbor: evaluate(neighbor))
        best_score = evaluate(best_neighbor)

        if best_score > current_score:
            assignment = best_neighbor
            current_score = best_score
        else:
            break

    return assignment, current_score

# Genetic Algorithm
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

# Function to run the experiment
def run_experiment(algorithm, clauses, variables, runs=5):
    runtimes = []
    successes = 0
    for _ in range(runs):
        start_time = time.time()
        assignment, score = algorithm(clauses, variables)
        end_time = time.time()
        runtimes.append(end_time - start_time)
        if score == len(clauses):
            successes += 1

    avg_runtime = sum(runtimes) / runs
    std_dev_runtime = (sum((x - avg_runtime) ** 2 for x in runtimes) / runs) ** 0.5
    success_rate = successes / runs

    return avg_runtime, std_dev_runtime, success_rate

# Example usage:
clauses, variables = parse_dimacs('D:/Ai/Assigment 2/3sat_instance.dimacs')

if clauses and variables:
    avg_runtime_hc, std_dev_runtime_hc, success_rate_hc = run_experiment(hill_climbing, clauses, variables)
    avg_runtime_ga, std_dev_runtime_ga, success_rate_ga = run_experiment(genetic_algo, clauses, variables)

    print(f"Hill Climbing - Avg Runtime: {avg_runtime_hc:.4f}, Std Dev: {std_dev_runtime_hc:.4f}, Success Rate: {success_rate_hc:.4f}")
    print(f"Genetic Algorithm - Avg Runtime: {avg_runtime_ga:.4f}, Std Dev: {std_dev_runtime_ga:.4f}, Success Rate: {success_rate_ga:.4f}")
else:
    print("No clauses or variables found.")
