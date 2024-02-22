#Name: Mubtasim Fuad Mahde
#ID: 21201624
from numpy.random import randint
import random
import numpy as np
def genetic_algorithm(population,iteration):
    global data
    i = 0
    while i != iteration:
        population = sorted(population, key=lambda x: x[0]) #sorting to get the fittest players
        x,y = selection(population[:len(population)]) # taking best 10% of population for generating new generation
        x = crossover(x,y)
        x = mutation(x)
        population[-1] = [fitness_function(x),x]
        #print(population[:5])
        if population[0][0] == 0:
            return population[0][1]
        i+=1
    return '-1'
        
def crossover(x,y): # takes a pair of strings and perform crossover
    global data
    i = random.randint(0,len(data)-1)
    x = x[:i]
    y = y[i:]
    x = x+y
    return x
    
def mutation(x): #takes a string and randomly chooses a bit to mutate
    global data
    i = random.randint(0,len(data)-1)
    if x[i] == '0':
        x = x[:i]+'1'+x[i+1:]
    else:
        x = x[:i]+'0'+x[i+1:]
    return x

def selection(population):
    i = random.randint(0,len(population)-1) #generate a random index
    j = random.randint(0,len(population)-1) #generate a random index
    while i == j: 
        j = random.randint(0,len(population)-1) #generate a random index for j if i and j are equal
    return population[i][1],population[j][1]

def fitness_function(x): # the fitness function is the total run of the selected candidates for a string
    global data,target
    score = 0
    for i in range(len(x)):
        if x[i] == '1':
            score += data[i][1]
    return abs(score-target) # a minimization problem with target 0 for optimal solution or close to optimal solution

def population_generator(length,size): #generate random population and their target score 
    population = randint(0, 2**length, size)
    num_bits = 8-length
    binary_score = np.unpackbits(population.astype(np.uint8)[:, np.newaxis], axis=1)[:,num_bits:]
    binary_score_strings = [''.join(map(str, row)) for row in binary_score]
    score = []
    for i in binary_score_strings:
        score.append(fitness_function(i))
    population = list(zip(score, binary_score_strings))
    population = sorted(population, key=lambda x: x[0])
    return population

#hyperParameters can be tuned for best results (wait 5 seconds for full result)
size = 20 #population size
iteration = 10000 #number of iterations


global data,target
file = open('Lab - 2\input_file_1.txt', 'r') #please change the file path as per requirements
data = file.readlines()
for i in range(len(data)):
    x = data[i].split()
    x = [x[0],int(x[1])]
    data[i] = x
target = int(data[0][1])  
data = data[1:]
population = population_generator(len(data),size)
print([tup[0] for tup in data])
print(genetic_algorithm(population,iteration))

file = open('Lab - 2\input_file_2.txt', 'r') #please change the file path as per requirements
data = file.readlines()
for i in range(len(data)):
    x = data[i].split()
    x = [x[0],int(x[1])]
    data[i] = x
target = int(data[0][1]) 
data = data[1:]
population = population_generator(len(data),size)
print([tup[0] for tup in data])
print(genetic_algorithm(population,iteration))

file = open('Lab - 2\input_file_3.txt', 'r') #please change the file path as per requirements
data = file.readlines()
for i in range(len(data)):
    x = data[i].split()
    x = [x[0],int(x[1])]
    data[i] = x
target = int(data[0][1]) 
data = data[1:]
population = population_generator(len(data),size)
print([tup[0] for tup in data])
print(genetic_algorithm(population,iteration))

