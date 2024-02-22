#Name: Mubtasim Fuad Mahde
#ID: 21201624
import random
import math
#id = input('Enter Your ID:')
id = '21201624'
id = id.replace('0','8')
min = int(id[4]) #5th digit
max = math.ceil((int(id[-1])*10+int(id[-2]))*1.5) #fidning max
target = int(int(id[-1])+int(id[-2])*10) # finding target
terminal = random.sample(range(min,max), 8)
S = int(id[3]) # iterations of tests
def alpha_beta_algo(terminal,a,b): # min max for range
    if len(terminal) == 1:
        return
    if a >= b:
        return a,b
    terminal_A,terminal_B = terminal[:int(len(terminal)/2)],terminal[int(len(terminal)/2):]
    alpha_beta_algo(terminal_A)
    alpha_beta_algo(terminal_B)
    print(terminal_A,terminal_B)

for i in range(1):
    random.shuffle(terminal)
    print(terminal)
    a = -float('inf')
    b = float('inf')
    print(a,b)
    result = alpha_beta_algo(terminal,a,b)