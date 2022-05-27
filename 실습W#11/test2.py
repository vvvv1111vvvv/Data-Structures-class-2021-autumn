def topological_sort_AM(vertex, graph) :
    n = len(vertex)
    inDeg = [0] * n             

    for i in range(n) :
        for j in range(n) :
            if graph[i][j] > 0 :
                inDeg[j] += 1   

    vlist = []                  
    for i in range(n) :
        if inDeg[i]==0 : 
            vlist.append(i)

    while len(vlist) > 0 :      
        v = vlist.pop()         
        print(vertex[v], end=' ')  

        for u in range(n) :
            if v != u and graph[v][u] > 0 :
                inDeg[u] -= 1       
                if inDeg[u] == 0 :  
                    vlist.append(u) 

vertex = ['A', 'B', 'C', 'D', 'E', 'F' ]
graphAM = [ [ 0,   0,   1,   1,   0,   0 ],
            [ 0,   0,   0,   1,   1,   0 ],
            [ 0,   0,   0,   1,   0,   1 ],
            [ 0,   0,   0,   0,   0,   1 ],
            [ 0,   0,   0,   0,   0,   1 ],
            [ 0,   0,   0,   0,   0,   0 ] ]
print('topological_sort: ')
topological_sort_AM(vertex, graphAM)
print()