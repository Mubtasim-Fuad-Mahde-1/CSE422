import heapq
d = {}
file = open('C://Users//21201624//Desktop//CSE422//Lab - 1//Input_file.txt','r')
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
def a_star_search(d,goal):
    p = []
    parent = {}
    key = list(d.keys())[0]
    h = d[key][0]
    g = 0
    heapq.heappush(p,(h,key))
    while True:
        print(p)
        f,key = heapq.heappop(p)
        g = f - d[key][0]
        for i in range(1,len(d[key])):
            child,g = d[key][i]
            f = g + d[child][0]
            heapq.heappush(p,(f,child))
        if key == goal:
            break
a_star_search(d,goal)