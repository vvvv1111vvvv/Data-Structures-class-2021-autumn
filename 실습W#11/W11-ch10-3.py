'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.18

1. 목적: 그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 10.3: 인접행렬로 표현된 그래프에 대한 연결성분검사 알고리즘을 구현하라, 단 너비우선탐색을 이용하라
3. 방법 : 10.2절의 함수와 테스트 코드를 응용한다.

알고리즘
#1. queue모듈을 import하여 Queue 큐를 사용한다.
#2. 연결성분검사 함수 find_connected_component()를 정의한다.  
    #2-1. 방문여부를 확인하는 리스트  visited 를 정의
    #2-2. 부분그래프별로 vertex를 저장하는 리스트 colorlist를 정의
    #2-3. vertex에 대하여 연산을 반복한다.
        #2-3-1. vertex를 방문하지 않았을 때, 큐에 v를 삽입한다. 부분그래프를 저장하는 공백리스트 color을 정의
        #2-3-2. 큐가 공백이 아닐 때까지 반복한다.
            #2-3-2-1. vertex를 방문하지 않았을 때, 방문했다고 변경한뒤, color에  vertex값을 저장
            #2-3-2-2. vertex 중에서 연결이 존재할 때 방문하지 않았으면 스텍에 vertex의 인덱스를 삽입
    #2-4. colorList에 color을 append한다.
#4. colorList의 개수와 성분을 출력
'''
import queue

def find_connected_component(vertex,graph):
    q=queue.Queue()      #너비우선탐색에 사용할 큐
    visited=[False]*len(vertex)     #vertex의 방문여부를 저장할 리스트
    colorList=[]                    #부분그래프별 vertex리스트


    for v in range(len(vertex)):
        if visited[v]==False:       #vertex를 방문하지 않았을 때
            q.put(v)           #탐색 시작점 v의 인덱스를 큐에 삽입
            color=[]
            while q.qsize()!=0:              #큐가 공백이 아닐 때까지
                v=q.get()
                if visited[v]==False:
                    visited[v]= True        #방문했다고 변경
                    color.append(vertex[v])
                    for i in range(len(graph)):   #vertex 중에서
                        if graph[v][i]==1:          #연결이 존재할 때
                            if visited[i]==False:   #방문하지 않았으면
                                q.put(i)     #스텍에 vertex의 인덱스를 삽입

            colorList.append(color)

    print("연결 성분의 개수 : %d" %len(colorList))    #연결성분의 개수를 출력
    print(colorList)    #방문한 연결성분을 출력

            

vertex1=['A','B','C','D','E','F','G','H']
adjMat1=[[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]

vertex2=['A','B','C','D','E']
adjMat2=[[0,1,1,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [0,0,0,0,1],
        [0,0,0,1,0]]
find_connected_component(vertex1,adjMat1)        #연결성분검사함수 호출 
find_connected_component(vertex2,adjMat2)        #연결성분검사함수 호출