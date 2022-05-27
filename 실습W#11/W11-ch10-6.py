'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.18

1. 목적: 그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 10.6: 연결된 그래프의 간선들 중에서 그 간선을 제거하면 연결이 끊어지는 간선(u,v)을 브리지(bridge)라고 한다.
            주어진 그래프에서 브리지를 찾아 모두 출력하는 함수를 작성하라.

3. 방법 : 10장의 함수와 테스트 코드를 응용한다.

알고리즘
#0. queue모듈과 copy모듈을 import
#1. 인접리스트로 그래프를 정의한다.
#2. 브릿지를 탐색하는 함수 find_bridge()를 호출, (입력: graph)
#3. find_bridge()
    #3-1. 그래프의 key와 진출간선에 대해서 graph를 newgraph에 복사한다.
    #3-2. removed_graph(newgraph,i,k)함수를 호출하여 vertex i와 j사이의 간선이 삭제된 그래프를 반환받는다.
    #3-3. find_connected_component() 함수를 호출하여 연결성분검사를 진행한다. 연결성분이 1이 아니라면,
            i,j 간선 삭제가 그래프의 성분을 나누었으므로 브릿지(i,k)를 출력한다.
#4.
'''

import queue
import copy
def find_bridge(graph):     #브릿지를 출력하는 함수
    for i in graph.keys():          # 그래프의 key와 진출간선에 대해서
        for j in graph[i]:
            for k in j:
                newgraph=copy.deepcopy(graph)
                newgraph=removed_graph(newgraph,i,k)
                if find_connected_component(list(graph.keys()),newgraph)!=1:
                    print("(",i,",",k,")")



def find_connected_component(vertex,graph):
    q=[]      #너비우선탐색에 사용할 큐
    visited=[False]*len(vertex)     #vertex의 방문여부를 저장할 리스트
    colorList=[]                    #부분그래프별 vertex리스트


    for v in range(len(vertex)):
        if visited[v]==False:       #vertex를 방문하지 않았을 때
            q.append(v)           #탐색 시작점 v의 인덱스를 큐에 삽입
            color=[]
            while len(q)!=0:              #큐가 공백이 아닐 때까지
                v=q.pop(0)
                if visited[v]==False:
                    visited[v]= True        #방문했다고 변경
                    color.append(vertex[v])
                    for i in vertex:   #vertex 중에서
                        if i in graph[vertex[v]]:          #연결이 존재할 때
                            if visited[vertex.index(i)]==False:   #방문하지 않았으면
                                q.append(vertex.index(i))     #스텍에 vertex의 인덱스를 삽입

            colorList.append(color)
    return len(colorList)
'''
def find_connected_component(newgraph):
    visited= set()
    colorList=[]

    for vtx in newgraph:
        if vtx not in visited:
            color=dfs_cc(newgraph,[],vtx,visited)
            colorList.append(color)

    return len(colorList)==1
def dfs_cc(newgraph,color,vertex,visited):
    if vertex not in visited:
        visited.add(vertex)
        color.append(vertex)
        nbr=newgraph[vertex]-visited
        for v in nbr:
            dfs_cc(newgraph,color,v,visited)
    return color
'''
def removed_graph(newgraph,key1,key2):     #key1과 key2사이의 간선을 삭제한뒤, 그래프를 반환하는 함수

    s1=newgraph[key1]
    s1.remove(key2)
    newgraph[key1] = s1

    s2=newgraph[key2]
    s2.remove(key1)
    newgraph[key2] = s2
    return newgraph

graph={'A':{'B','D'},
        'B':{'A','D','E','C'},
        'C':{"B","F"},
        'D':{"A",'B','E'},
        'E':{"B",'D'},
        'F':{'C'}}
find_bridge(graph)
