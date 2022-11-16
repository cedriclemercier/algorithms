

graph = {
    '1' : ['2'],
    '2' : ['7', '4'],
    '3' : ['4'],
    '4' : ['6'],
    '5' : ['4', '3'],
    '6' : [],
    '7' : ['5']
}


def DFS(graph, s):
    visited = set()
    
    if s not in visited:
        print(s, "-->", end="")
        visited.add(s)
        for neighbor in graph[s]:
            DFS(graph, neighbor)
            
            
DFS(graph, '1')