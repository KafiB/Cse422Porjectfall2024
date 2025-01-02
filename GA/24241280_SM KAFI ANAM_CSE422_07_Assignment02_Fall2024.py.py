#Genetin Algorithm

#Task - 1
print("Task-1")

import random

file1 = open("D:\Ai\GA\input.txt","r")
lines = file1.readlines()

N = int(lines[0].split()[0])  
T = int(lines[0].split()[1])  
course_list = [lines[i + 1].strip() for i in range(N)]

population_size = 10
mutation_rate = 0.1

def generate_population(size, N, T):
    population = []
    for _ in range(size):
        genome = [random.randint(0, 1) for _ in range(N * T)]
        population.append(genome)
    return population

def fitness(chromosome):
    overlap_penalty = 0
    consistency_penalty = 0

    for t in range(T):
        timeslot_start = t * N
        timeslot_end = (t + 1) * N
        timeslot = chromosome[timeslot_start:timeslot_end]
        scheduled_courses = sum(timeslot)
        if scheduled_courses > 1:
            overlap_penalty += (scheduled_courses - 1)

    course_schedule_count = [0] * N
    for t in range(T):
        timeslot_start = t * N
        timeslot_end = (t + 1) * N
        timeslot = chromosome[timeslot_start:timeslot_end]
        for idx in range(len(timeslot)):
            is_scheduled = timeslot[idx]
            if is_scheduled == 1:
                course_schedule_count[idx] += 1

    for count in course_schedule_count:
        if count != 1:
            consistency_penalty += (count - 1)

    total_penalty = overlap_penalty + consistency_penalty
    fitness_value = -total_penalty
    return fitness_value

def select_parents(population, fitness_values):
    min_fitness = min(fitness_values)
    if min_fitness < 0:
        shifted_fitness_values = []
        for f in fitness_values:
            shifted_value = f + abs(min_fitness) + 1
            shifted_fitness_values.append(shifted_value)
        fitness_values = shifted_fitness_values
    parents = random.choices(population, weights=fitness_values, k=2)
    return parents

def single_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(genome, mutation_rate):
    for i in range(len(genome)):
        if random.random() < mutation_rate:
            genome[i] = 1 - genome[i]
    return genome

def genetic_algorithm(N, T, course_list, population_size, mutation_rate):
    population = generate_population(population_size, N, T)
    for i in range(population_size):
        fitness_values = [fitness(genome) for genome in population]
        
        best_fitness = max(fitness_values)
        if best_fitness == 0:  
            break
        
        new_population = []

        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness_values)
            child1, child2 = single_point_crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))
        population = new_population[:population_size]

    best_genome = population[fitness_values.index(max(fitness_values))]
    return best_genome, fitness(best_genome)

best_genome, best_fitness = genetic_algorithm(N, T, course_list, population_size, mutation_rate)

print("Best Chromosome:", "".join(map(str, best_genome)))
print("Fitness Value:", best_fitness)

print("Taks-2")
def generate_population(size, N, T):
    return [[random.randint(0, 1) for _ in range(N * T)] for _ in range(size)]

population = generate_population(population_size, N, T)
parent1, parent2 = random.sample(population, 2)

def two_point_crossover(parent1, parent2):
    length = len(parent1)
    point1, point2 = sorted(random.sample(range(length), 2)) 
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return child1, child2, point1, point2

child1, child2, point1, point2 = two_point_crossover(parent1, parent2)

print("Parent 1:  ", "".join(map(str, parent1)))
print("Parent 2:  ", "".join(map(str, parent2)))
print(f"1st Point: {point1}, 2nd Point: {point2}")
print("Offspring 1:", "".join(map(str, child1)))
print("Offspring 2:", "".join(map(str, child2)))
