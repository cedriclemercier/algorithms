#for each vertex
#set key = infinity
#set pi = NUL

#r.key = 0
#put all vertex into the queue


#white q is not empty
    #u = extract_min
        #for v in adj[u]
            #if v in Q, and w(u, v) < v.key
                #v.pi = u
                #v.key = w(u, v)