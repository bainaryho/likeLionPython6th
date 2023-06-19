# graph = {
#     'A' : ['B', 'C'],
#     'B' : ['A', 'D', 'E'],
#     'C' : ['A', 'F'],
#     'D' : ['B'],
#     'E' : ['B' , 'F'],
#     'F' : ['C', 'E']
# }
#
# visited = set()
#
# def dfs(start_node):
#     stack = [start_node]
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             stack.extend(reversed(graph[node]))
# ex_node = 'A'
# dfs(ex_node)

from collections import deque
graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B' , 'F'],
    'F' : ['C', 'E']
}

visited = set() #방문 노드를 저장할 집합

def bfs(start_node):
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend(graph[node])
ex_node = 'A'
bfs(ex_node)