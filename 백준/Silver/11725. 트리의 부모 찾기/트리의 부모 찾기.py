import sys
sys.setrecursionlimit(10**6)

def dfs(node, graph, visited, parent):
    visited[node] = True
    for other_node in graph[node]:
        if not visited[other_node]:
            parent[other_node] = node
            dfs(other_node, graph, visited, parent)


node = int(input())
graph = [[] for _ in range(node+1)]

visited = [False] * (node+1)
parent = [0] * (node+1)

for _ in range(node-1):
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1)

dfs(1, graph, visited, parent)

for i in range(2, node + 1):
    print(parent[i])