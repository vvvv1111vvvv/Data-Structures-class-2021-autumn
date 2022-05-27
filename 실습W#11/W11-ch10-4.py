'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.18

1. 목적: 그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 10.4: 인접행렬로 표현된 그래프에 대해 신장트리를 구하는 함수를 구현하라 (깊이우선탐색)
3. 방법 : 10.5절의 함수와 테스트 코드를 응용한다.

신장트리: 그래프내의 모든 정점을 포함하는 '트리'

알고리즘
#1. 방문여부를 확인하는 리스트visited를 정의, False로 초기화
#2. 신장트리 여부를 확인하는 함수를 호출
#3. 신장트리 여부를 확인하는 함수
    입력: vertex,graph, v, visited
    return : 없음
    #3-1. vertex v를 방문함
    #3-2. vertex 중에서 v와의 edge가 존재하는 i에 대해 vertex i를 방문하지 않았다면
    #3-3. v와 i사이의 간선을 출력, 재귀함수를 호출한다.(입력:vertex, graph,i,visited)
'''


def dfsST(vertex, graph,v,visited):     
    visited[v]=True              #vertex v를 방문함
    for i in range(len(vertex)): #vertex 중에서
        if graph[v][i]==1:       #v와의 edge가 존재하는 i에 대해
            if visited[i]==False:   #vertex i를 방문하지 않았다면
                print("(",vertex[v],vertex[i],')',end=' ')  #v와 i사이의 간선을 출력
                dfsST(vertex, graph,i,visited)              #재귀함수를 호출




vertex1=['A','B','C','D','E','F','G','H']
adjMat1=[[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]
visited=[False]*len(vertex1)        #방문여부를 확인하는 리스트
dfsST(vertex1,adjMat1,0,visited)    #신장트리여부를 확인하는 함수