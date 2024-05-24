file = open('./data.txt', 'r')
No, Mo = None, None
graphs = []
source = None
unique = []
for i in file:
    if len(i.split()) == 2:
        No, Mo = i.split()
    elif len(i.split()) == 1:
        source = i.split()[0]
    else:
        lists =  i.split()
        if lists[0] not in unique:
            unique.append(lists[0])
        if lists[1] not in unique:
            unique.append(lists[1])
        lists[2] = int(lists[2])
        graphs.append(lists)


No = int(No)
Mo = int(Mo)
# print(No)
# print(Mo)
# print(unique)
# print(graphs)
# print(source)