
from collections import deque
from collections import defaultdict
def bfs(graph, start, visited, path):
    queue = deque()
    visited[start] = True
    queue.append(start)
    path.append(start)
    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
                path.append(neighbour)

    return path


graph = defaultdict(list)

v, e = map(int, input("Enter the number of nodes and edges: ").split())
print("\nEnter the edges (Adjacent Nodes):")
for i in range(e):
    u, w = input(f"Edge {i+1} (u v): ").split()
    graph[u].append(w)
    graph[w].append(u)
print("\nAdjacency List:")
for node in graph:
    print(node, "->", graph[node])
start = input("\nEnter the start node for BFS: ")
if start not in graph:
    print("Invalid start node!")
else:
    visited = defaultdict(bool)
    path = []

 traversedpath = bfs(graph, start, visited, path)
 print("\nBFS Traversal:", " -> ".join(traversedpath))
