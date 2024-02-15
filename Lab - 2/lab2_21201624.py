#Name: Mubtasim Fuad Mahde
#ID: 21201624
from numpy.random import randint
import random
import numpy as np
def genetic_algorithm(data,population,iteration):
    pass

def crossover(x,y,data): # takes a pair of strings and perform crossover
    i = random.randint(1,len(data)-1)
    x1,x2 = x[0:i],x[i:]
    y1,y2 = y[0:i],y[i:]
    x = x1+y2
    return x
    
def mutation(x,data): #takes a string and randomly chooses a bit to mutate
    c = random.choice(0,1)
    if c == 0:
        return x
    i = random.randint(0,len(data)-1)
    if x[i] == 0:
        x[i] = 1
    else:
        x[i] = 0
    return x

def selection(population):
    i = random.randint(0,len(population)) #generate a random index
    j = random.randint(0,len(population)) #generate a random index
    while i == j: 
        j = random.randint(0,len(population)) #generate a random index for j if i and j are equal
    return population[i],population[j]

def fitness_function(x): # the fitness function is the total run of the selected candidates for the string
    global data,target
    score = 0
    for i in range(len(x)):
        if x[i] == '1':
            score += data[i][1]
    return abs(score-target)

def population_generator(length,size): #generate random population and their target score 
    population = randint(0, 2**length, size)
    binary_score = np.unpackbits(population.astype(np.uint8)[:, np.newaxis], axis=1)
    binary_score_strings = [''.join(map(str, row)) for row in binary_score]
    score = []
    for i in binary_score_strings:
        score.append(fitness_function(i))
    population = list(zip(score, binary_score_strings))
    population = sorted(population, key=lambda x: x[0])
    return population

global data,target
file = open('C://Users//mubta//Desktop//CSE422//Lab//CSE422//Lab - 2//input_file_1.txt', 'r')
data = file.readlines()
for i in range(len(data)):
    x = data[i].split()
    x = [x[0],int(x[1])]
    data[i] = x
target = int(data[0][1])
size = len(data) * 5  # hyperparameter denoting initial population size
data = data[1:]
population = population_generator(len(data),size)
print(population)

