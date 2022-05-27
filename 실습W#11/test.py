
#신장트리 DFS

def dfs(graph,start,visited=set()):
    if start not in visited:
        visited.add(start)
        #print(start,end='')
        nbr=graph[start]-visited
        for v in nbr:
            if v not in visited:
                print("(",start,v,')',end=' ')
                dfs(graph,v,visited)

graph={'A':{'B','C'},
        'B':{'A','D'},
        'C':{'A',"D","E"},
        'D':{'B',"C","F"},
        'E':{"C","G","H"},
        "F":{'D'},
        "G":{"E","H"},
        "H":{"E","G"}}
dfs(graph,'A')
