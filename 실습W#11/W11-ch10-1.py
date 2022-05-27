'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.18

1. 목적: 그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 10.1: 인접행렬로 표현된 그래프에 대한 깊이우선탐색 알고리즘을 구현하라
3. 방법 : 10.3절의 함수와 테스트 코드를 응용한다.

알고리즘
#1.  인접행렬로 그래프를 정의한다.
#2. 깊이 우선 탐색함수 dfs()를 정의한다.
#3. vertex가 방문했는지 여부를 나타내는 리스트 visited와 깊이우선 탐색에 사용할 스택 vlist를 정의한다.
#4. 탐색 시작점를 스택에 삽입한 뒤, 스택이 공백이 될 때까지,
    #4-1. 스택의 마지막 항목을 pop()한다.
    #4-2. vertex를 방문 하지 않았으면 vertex의 값을 출력하고, 방문으로 표기한다.
    #4-3. vertex에 연결된 엣지 중, 방문하지 않은 vertex의 인덱스를 스택에 삽입한다.
'''
def dfs(vertex,graph,start):    #깊이우선 탐색 알고리즘
    visited=[False]*len(vertex)  #방문 여부를 확인하는 리스트
    vlist=[]                    #깊이우선탐색에 사용할 스택
    vlist.append(start)         # 탐색 시작점 'A'의 인덱스 를 스택에 삽입
    while len(vlist)>0:         #스텍이 공백이 될 때까지 실행
        v=vlist.pop()           #스택의 마지막 항목을 pop()
        if visited[v] == False:     #vertex를 방문하지 않았으면
            print(vertex[v],end=' ')    #방문한 vertex를 출력
            visited[v]= True        #방문했다고 변경
            for i in range(len(vertex)):   #vertex 중에서
                if graph[v][i]==1:          #연결이 존재할 때
                    if visited[i]==False:   #방문하지 않았으면
                        vlist.append(i)     #스텍에 vertex의 인덱스를 삽입



vertex=['A','B','C','D','E','F','G','H']
adjMat=[[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]
dfs(vertex,adjMat,0)        #dfs함수 호출, 0:start가 'A'에서 시작함을 뜻한다.
