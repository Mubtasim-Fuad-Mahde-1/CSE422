import heapq
d = {}
file = open('C://Users//mubta//Desktop//CSE422//Lab//CSE422//Lab - 1//Input_file.txt','r')
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].split() #split each line based on spaces
for i in lines:
    key = i[0] # parent node
    h = int(i[1]) # parent node heuristics
    if h == 0:
        goal = key # if parent node huristic is 0 then this is the goal node
    d[key] = [int(h)]
    for j in range(2,len(i),2):
        d[key].append((i[j],int(i[j+1]))) # putting the child with path in dict
print(d)
def a_star_search(d,goal):
    p = [] #priorityqueue
    parent = {} #parent dict
    key = list(d.keys())[0] #cahnge this value to set the starting point from any graph node
    h = d[key][0]
    g = 0
    heapq.heappush(p,(h,key)) #push starting node
    parent[key] = (g,None)
    while True:
        f_parent,key = heapq.heappop(p) #pop queue
        g_parent = f_parent - d[key][0]
        for i in range(1,len(d[key])): # expand popped node
            child,g = d[key][i]
            f = g_parent + g + d[child][0]
            heapq.heappush(p,(f,child)) #insert child of parent node
            if child not in parent.keys(): 
                parent[child] = (g+g_parent,key)
            else:
                if parent[child][0] >= g+g_parent: # check if nodes with lower function value present or not
                    parent[child] = (g+g_parent,key) #if present and higher than current value then replace
        if key == goal: #goal test after expanding
            if f_parent <= p[0][0]:
                break
    return parent
parent = a_star_search(d,goal) #returns parent dictionary containing path costs
cost = parent[goal][0]
key = goal
path = ''
while True: # concatinate the path 
    path = '->'+parent[key][1]+path
    key = parent[key][1]
    if parent[key][1] == None:
        break
path += '->'+goal
print('Path:',path[2:]) #printing path and cost
print('Total Distance:',cost,'km')