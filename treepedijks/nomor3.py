from readno3 import source, graphs, No, Mo
Q =[]
dist={}
lists_max=[]
vertex_sudah_kunjung_tetangga =[]
N,M= No, Mo
list_per_edges = graphs
s = source
dist[s] = 0
Q.append(s)

def plusdistance(angka):
    Q.append(per_edge[angka])
    dist[per_edge[angka]] = dist[Q[0]] + 1
    list_per_edges.remove(per_edge)


while len(Q)>=1:
    # print(Q)
    for per_edge in list_per_edges.copy():
        if(per_edge[0] == Q[0]) and (per_edge[1] not in Q + vertex_sudah_kunjung_tetangga):
            plusdistance(1)
        if(per_edge[1] == Q[0]) and (per_edge[0] not in Q + vertex_sudah_kunjung_tetangga):
            plusdistance(0)

    vertex_sudah_kunjung_tetangga.append(Q.pop(0))

max_value = None
max_key = None

for key, value in dist.items():
    if max_value is None or value > max_value:
        max_value = value
for keys, values in dist.items():
    if values == max_value and keys not in lists_max:
        max_key = keys
        lists_max.append(max_key)

print("Key dengan nilai maksimal:", lists_max)
print("Nilai maksimal:", max_value)


