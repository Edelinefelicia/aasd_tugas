from testingread import source1, graph, No, Mo
N = No  # Banyak vertex
M = Mo # Banyak edge
edges = graph
S = source1 # Titik awal / sumber
target_distance = 2024

def dfs(graph, current, target_distance, current_distance):
    global list_visited_return
    stack = [(current,[current],current_distance)]
    while stack:
        current, list_visited , current_distance = stack.pop()
        if current_distance == target_distance:
            list_visited_return = list(map(str,list_visited))
            return True
            break
        if current_distance > target_distance:
            continue

        for neighbor, weight in graph[current]:
            if neighbor not in list_visited :
                stack.append((neighbor,list_visited+[neighbor],current_distance+weight))

if (dfs(edges, S, target_distance, 0)):
    print(" -> ".join(list_visited_return))

else:
    print("Tidak ada vertex yang memiliki jarak 2024 dari vertex", S)

