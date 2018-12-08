import random

genetic_cost_all = 0
genetic_cost_local = 0


def fitness(array):
    return 28 - heuristic(array)


def heuristic(array):
    h = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                h = h + 1
            offset = i - j
            if array[i] == array[j] - offset or array[i] == array[j] + offset:
                h = h + 1
    return (h)


def generate_population(num):
    population = list()
    sample_arr = [i for i in range(8)]  # ---- Create an sample arr from [0,7]
    for i in range(num):
        ran_sample_arr = random.sample(sample_arr, 8)  # --------New array with 8 different elements from [0,7]
        population.append(list(ran_sample_arr))  # ------------ add small array into the list
    return sort_by_fitness(population)


# get the "heuristic" from array in population then "compare"
def sort_by_fitness(population):
    # print(population)
    for i in range(len(population)):
        for j in range(i + 1, len(population)):
            if (fitness(population[j]) > fitness(population[i])):
                population[i], population[j] = population[j], population[i]
    return genetic_algorithm(population)  # return the sorted list into the genetic_algorithm


def genetic_algorithm(population):
    global genetic_cost_local
    global genetic_cost_all
    if (fitness(population[0]) == 28):
        print(population[0])
        genetic_cost_all += genetic_cost_local
        genetic_cost_local = 0
        return population[0]  # Return to solution_solved
    else:
        genetic_cost_local += heuristic(population[0])
        return crossover(population)  # return to crossover function


def crossover(population):
    list_of_children = list()
    size = len(population)
    count = 0
    for i in range(int(len(population) * 0.2)):
        population.pop(-1)

    while (count != size):
        random_num = random.randint(0, 7)
        parent_1 = random.choice(population)  # Choose random array for parent_1
        random.shuffle(population)  # ------Randomly scartered population list
        parent_2 = random.choice(population)  # Choose random array for parent_2
        if (parent_1 != parent_2):
            child = parent_1[:random_num] + parent_2[random_num:]  # ----This is a crossover for child
            list_of_children.append(child)
            count += 1
    return mutation(list_of_children)


def mutation(list_of_children):
    mutation_rate = int(len(list_of_children) * 0.4)
    for i in range(mutation_rate):
        child = random.choice(list_of_children)
        list_of_children.remove(child)
        random_index = random.randint(0, 7)
        random_mutation = random.randint(0, 7)
        child[random_index] = random_mutation
        list_of_children.append(child)
    # print(list_of_children)
    try:
        return sort_by_fitness(list_of_children)
    except RecursionError:
        return None


def genetic_call(num):
    solution_solved = 0
    count = 0
    while (count < num):
        if (generate_population(50) != None):
            solution_solved += 1
        count += 1
    print("Genetic Algorithm: ", int((solution_solved / num) * 100), "% solved, Search Cost: ", genetic_cost_all)


genetic_call(10)