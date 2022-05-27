'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.18

1. 목적: 그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 10.2: 인접행렬로 표현된 그래프에 대한 너비우선탐색 알고리즘을 구현하라, 단 큐로는 파이썬의 queue모듈의 Queue클래스를 사용하라.
3. 방법 : 10.3절의 함수와 테스트 코드를 응용한다.

알고리즘
#1.  인접행렬로 그래프를 정의한다.
#2. 너비 우선 탐색함수 bfs()를 정의한다.
#3. vertex가 방문했는지 여부를 나타내는 리스트 visited와 깊이우선 탐색에 사용할 큐 q를 정의한다.
#4. 탐색 시작점를 큐에 삽입한 뒤, 큐가 공백이 될 때까지,
    #4-1. 스택의 마지막 항목을 get()한다.
    #4-2. vertex를 방문 하지 않았으면 vertex의 값을 출력하고, 방문으로 표기한다.
    #4-3. vertex에 연결된 엣지 중, 방문하지 않은 vertex의 인덱스를 큐에 삽입한다.
'''
import queue

def bfs(vertex,graph,start):
    q=queue.Queue()      #너비우선탐색에 사용할 큐
    visited=[False]*len(vertex)     #vertex의 방문여부를 저장할 리스트
    q.put(start)       #탐색 시작점 'A'의 인덱스를 큐에 삽입
    while q.qsize()!=0:              #큐가 공백이 아닐 때까지
        v=q.get()

        if visited[v] ==False:
            print(vertex[v],end=' ')    #방문한 vertex를 출력
            visited[v]= True        #방문했다고 변경
            for i in range(len(vertex)):   #vertex 중에서
                if graph[v][i]==1:          #연결이 존재할 때
                    if visited[i]==False:   #방문하지 않았으면
                        q.put(i)     #스텍에 vertex의 인덱스를 삽입




vertex=['A','B','C','D','E','F','G','H']
adjMat=[[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]
bfs(vertex,adjMat,0)        #bfs함수 호출, 0:start가 'A'에서 시작함을 뜻한다.
