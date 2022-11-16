#use adjacency matrix (undirected)
#why undirected?
#use example 1
    #0,1,2,3,4
G = [[0, 2, 2, 5, 3],
    [2, 0, 1, 4, 4],
    [2, 1, 0, 3, 5],
    [5, 4, 3, 0, 4],
    [3, 4, 5, 4, 0]]

#for each vertex
#set key = infinity
INF = 9999
N = 5

#r.key = 0
r   = 0


from heapdict import heapdict

Q = heapdict()
for i in range(N):
    Q[i] = INF
Q[r] = 0

print(f"Queue: {list(Q.keys())}")
u = Q.popitem()[0] # 0 is priority and 1 refers to node
print(f"Queue: {list(Q.keys())}")
u = Q.popitem()[0] # 0 is priority and 1 refers to node
print(f"Queue: {list(Q.keys())}")

# set pi  = NIL
# pi = [None, None, None, None, None]
pi = [None] * 5
# set the pi of r = -1 or anything you like
pi[r] = -1
# print(f"PI: {pi}")

def adj(G, u):
    neighbors = []
    
    return neighbors

# while Q is not empty
while(Q):
    #u = extract_min  (dict has no extract_min)
    u  = Q.popitem()[0]
    
    for v in adj(G, u):
        
        if (v_in_Q(Q,v) and G[u][v] < Q[v]):
            pi[v] = u
            Q[v] = G[u][v]
    
    
    
    
    
# for v in adj[u]
# if v in Q, and w(u, v) < v.key
#v.pi = u
#v.key = w(u, v)

# print(pi)

                
                
#u = extract_min
    #you have to suffer writing your own min function ==> 0(n))
    #proritu queue can do extract_min in 0(log n)
    #we should use heap!!
    #this morning I already, there are three ways
    #from Queu import PriorityQueue(this one easiest, but not a dictionary)
    #import heapq (difficult to use, because you can do something Q[v])
    ##heapq: instead 0:0 1:999 ==> 0.; 999:1
    #import heapdcit (is our hero, asically dictionary + hea[])