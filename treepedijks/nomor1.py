from read import source, graphs, No, Mo, unique
N,M= No, Mo
list_vertex = unique 
list_per_edges = graphs
table = {}
vertex_value_parent = []
s = source
table[s] = 0
for j in list_vertex:
    if j != str(s) :
        table[j] = 10**9

def appendhasil(angka):
    if (table[min_key]+k[2])<table[k[angka]]:                
        table[k[angka]]=table[min_key]+k[2]
        if(len(vertex_value_parent)==0): #apakah list vertex_value_parent len nya 0
            vertex_value_parent.append([k[angka],table[k[angka]], str(min_key)]) #tujuan , value, parent
        else:
            for isi in vertex_value_parent : #biar gada doble di satu vertex
                if(k[angka]!=isi[0]) and isi == vertex_value_parent[-1]:
                    vertex_value_parent.append([k[angka],table[k[angka]], str(min_key)])
                    break
                if (k[angka]==isi[0]):
                    vertex_value_parent.pop(vertex_value_parent.index(isi))
                    vertex_value_parent.append([k[angka],table[k[angka]], str(min_key)])
                    break

while len(table) >0:
    min_key1 = min(table, key=table.get)
    for k in list_per_edges: #list_per_edges tuh input per baris atau per edge
        min_key = min_key1

        if k[0] == str(min_key) :
            if k[1] not in table:
                continue
            appendhasil(1)

        if k[1]==str(min_key):
            if k[0] not in table:
                continue
            appendhasil(0)
    values = table.pop(min_key)
max = vertex_value_parent[0][1]
hasil_terpendek = vertex_value_parent[0]
for i in vertex_value_parent:
    if (i[1]>max):
        max = i[1]
        hasil_terpendek=i[0]
print(f"Hasil Vertex yang memiliki jalur terpendek paling tinggi: {hasil_terpendek}")
print(f"Hasil total jalurnya: {max}")
