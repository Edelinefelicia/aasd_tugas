file = open('./data.txt', 'r')
No, Mo = None, None
graphs = []
source = None
for i in file:
    if len(i.split()) == 2:
        No, Mo = list(map(int,i.split()))
    elif len(i.split()) == 1:
        source = i.split()[0]
    else:
        lists =  i.split()
        graphs.append([lists[0],lists[1]])

