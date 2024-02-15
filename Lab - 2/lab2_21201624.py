from numpy.random import randint
import numpy as np
import random

file1 = open('C://Users//21201624//Desktop//CSE422//Lab - 2//input_file_1.txt', 'r')
file2 = open('C://Users//21201624//Desktop//CSE422//Lab - 2//input_file_1.txt', 'r')
file3 = open('C://Users//21201624//Desktop//CSE422//Lab - 2//input_file_1.txt', 'r')\


global data
data = file1.readlines()
for i in range(len(data)):
    data[i] = data[i].split()
score = data[0][1] #the target score
data = data[1:] #the list of players and their score

def fitness_func(x):
    global data
    sum = 0
    for i in range(len(x)):
        if x[i] == 1:
            sum += int(data[i][1])
    return sum

def population_to_score(pupulation):
    for i in range(len(population)):
        score = fitness_func(population[i])
        population[i] = (score,population[i])

def mutation():
    global data
    i = random.choice(1,len(data)-1)
    x,y = selection()

def crossover():
    pass

def selection():
    global data
    pass


#hyper parameters
n_population = 50 #number of population generated at initial
population = randint(0,2**len(data),n_population)
population = np.vectorize(np.binary_repr)(population, 8)
population = population_to_score(population)

