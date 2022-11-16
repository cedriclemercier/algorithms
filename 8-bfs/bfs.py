

graph = {
    '1' : ['2'],
    '2' : ['7', '4'],
    '3' : ['4'],
    '4' : ['6'],
    '5' : ['4', '3'],
    '6' : [],
    '7' : ['5']
}


def BFS(graph, s):
    visited = list()
    queue = []
    visited.append(s)
    queue.append(s)
    
    while queue:
        u = queue.pop(0)
        
        print(u, "-->", end="")
        
        for neighbor in graph[u]:
            if neighbor not in visited:
                visited.append(neighbor)
                