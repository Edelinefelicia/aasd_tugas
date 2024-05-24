file = open('./data.txt', 'r')
No, Mo = None, None
graphs = []
source1 = None
for i in file:
    if len(i.split()) == 2:
        No, Mo = list(map(int,i.split()))
    elif len(i.split()) == 1:
        source1 = int(i.split()[0])
    else:
        lists =  list(map(int,i.split()))
        graphs.append(lists)

graph = {i: [] for i in range(1, No + 1)}
for p1, p2, d in graphs:
    graph[p1].append((p2, d))
    graph[p2].append((p1, d))
