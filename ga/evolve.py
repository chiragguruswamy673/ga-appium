# ga/evolve.py
from deap import base, creator, tools
from ga.chromosome import random_chromosome
from ga.fitness import run_sequence
import random

random.seed(42)
POP, GENS, CX_PB, MUT_PB = 12, 10, 0.6, 0.3

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("individual", lambda: creator.Individual(random_chromosome()))
toolbox.register("population", tools.initRepeat, list, toolbox.individual, n=POP)

def evaluate(ind):
    score = run_sequence(ind)
    ind.fitness.values = (score,)
    return ind.fitness.values

def mutate(ind):
    if random.random() < 0.5 and len(ind) > 0:
        ind[random.randrange(len(ind))] = random_chromosome(1)[0]
    else:
        ind.append(random_chromosome(1)[0])
    return (ind,)

def evolve():
    pop = toolbox.population()
    history = []
    for g in range(GENS):
        for ind in pop:
            evaluate(ind)
        max_fit = max(i.fitness.values[0] for i in pop)
        avg_fit = sum(i.fitness.values[0] for i in pop) / len(pop)
        history.append((g, max_fit, avg_fit))
        offspring = tools.selTournament(pop, k=len(pop), tournsize=3)
        offspring = list(map(toolbox.clone, offspring))
        for i in range(1, len(offspring), 2):
            if random.random() < CX_PB:
                tools.cxTwoPoint(offspring[i-1], offspring[i])
        for mut in offspring:
            if random.random() < MUT_PB:
                mutate(mut)
        pop[:] = offspring
    best = tools.selBest(pop, k=3)
    return best, history