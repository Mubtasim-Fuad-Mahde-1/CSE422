#Name: Mubtasim Fuad Mahde
#ID: 21201624
import random
import math

id = input('Enter Your ID:')  # Take user input for ID
id = id.replace('0', '8')
minimum = int(id[4])  # 5th digit
maximum = math.ceil((int(id[-1]) * 10 + int(id[-2])) * 1.5)  # finding max
target = int(int(id[-1]) + int(id[-2]) * 10)  # finding target
terminal = random.sample(range(minimum, maximum), 8)
S = int(id[3])

def max_func(s, a, b):
    if len(s) == 1: #if leaf node then return utility
        return s[0] #return utlity and set V' of parent node
    else:
        s1, s2 = s[:int(len(s) / 2)], s[int(len(s) / 2):]
        val = -10000 # V is negative inf for max node
        alternate = min_func(s1,a,b) #V' for max node 
        if alternate > val: # if V' > V : V = V' for max (best alternate)
            val = alternate
        if alternate >= b: # if V' >= b : return V (pruning )
            return val
        if alternate > a: # if V' > a : a = V' (updating a)
            a = alternate
        alternate = min_func(s2,a,b)
        if alternate > val:
            val = alternate
        if alternate >= b:
            return val
        if alternate > a:
            a = alternate
    return val #default return is V


def min_func(s, a, b):
    if len(s) == 1:
        return s[0]
    else:
        s1, s2 = s[:int(len(s) / 2)], s[int(len(s) / 2):]
        val = 10000 # V is positive inf for min node
        alternate = max_func(s1,a,b) # V' for min node
        if alternate < val: # best alternate
            val = alternate
        if alternate <= a: # pruning
            return val
        if alternate < b: # updating b
            a = alternate
        alternate = max_func(s2,a,b)
        if alternate < val:
            val = alternate
        if alternate <= a:
            return val
        if alternate < b:
            a = alternate
    return val #default return is V


def alpha_beta_algo(s, a, b): 
    return max_func(s, a, b)

print('Generated List =',terminal,'Shuffled for',S,'times')
count = 0
for i in range(S):
    random.shuffle(terminal)
    a = -10000
    b = 10000
    result = alpha_beta_algo(terminal, a, b)
    if result >= target:
        count+=1
    print(result)
print('Optimus Prime won ('+str(count)+') times and Megatron won ('+str(S-count)+') times')
