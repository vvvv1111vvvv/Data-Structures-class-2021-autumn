'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.25

1. 목적: 가중치그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 11.6: 11.4절의 Djikstra의 최단경로 코드를 수정하여 각 경로의 길이(Dist)와 경로(Path)를
                    출력하는 프로그램을 구현하라
3. 방법 : 11.4절의 함수와 테스트 코드를 응용한다.

#Dijkstra의 최단경로 알고리즘: 하나의 시작 정점 v에서 다른 모든 정점까지의 최단경로를 찾는 알고리즘
    시작정점 v : 최단경로 탐색의 시작 정점
    집합 S : 시작 정정 v로부터의 최단 경로가 이미 발견된 정점들의 집합
    dist 배열 : S에 있는 정점만을 거져서 다른 정점으로 가는 최단거리를 기록하는 배열   
                Prim의 MST알고리즘과 유사


알고리즘
#1. 인접행렬을 이용해 그래프를 구현한다.
#2. shortest_path_dijkstra(vertex,weight,start)를 호출한다.
    # 2-1. 정점의 수를 저장하는 변수 vsize생성 및 초기화
    # 2-2. dist, path, found, 리스트의 생성및 초기화
    # 2-3. 시작정점 start : 이미 찾아짐
    # 2-4. 시작 정점의 거리를 0
    # 2-5. 모든 정점에 대해서 반복
        # 2-5-1. 단계별 dist[] 출력
        # 2-5-2. 최소 dist정점 u 탐색을 위해 choose_vertex()함수 호출
            #2-5-2-1. 최소 거리 저장을 위한 변수 min 생성, INF로 초기화
            #2-5-2-2. 최소 거리 정점의 인덱스 저장을 위한 변수 minpos 생성, -1로 초기화
            #2-5-2-2. 모든 정점에 대해 반복
                #2-5-2-2-1. 거리가 min보다 작고, 방문하지 않았다면
                    min=dist[i],minpos=i
            #2-5-2-2. 최소 dist 정점의 인덱스 반환
        # 2-5-3. u는 이제 찾아짐
        # 2-5-4.모든 정점에 대해서 반복
            # 2-5-4-1. 아직 찾아지지 않았으면
                갱신 조건 검사, dist갱신, 이전 정점 갱신
    #2-6. path,dist 반환
#3. 최종경로 출력을 위한 코드
    #3-1. 모든 정점에 대해서 반복
        #3-1-1. start 가 아닐 때
            경로와 거리와 최단경로를 출력
            path[end]가 start가 아닐동안 경로 출력

'''
INF=9999
def choose_vertex(dist,found):
    '''
    S 안에 있지 않은 정점들 중에서 가장 dist값이 작은 정점을 찾는 함수
    입력: dist, found
    반환: minpos (최소 dist의 정점 인덱스)
    '''
    min= INF    #최소 거리 저장을 위한 변수 min, INF로 초기화
    minpos=-1   #최소 거리 정점의 인덱스 저장을 위한 변수 minpos, -1로 초기화
    for i in range (len(dist)): #모든 정점에 대해 반복
        if dist[i]<min and found[i]==False:     #거리가 min보다 작고, 방문하지 않았다면
            min=dist[i]
            minpos=i
    return minpos   #최소 dist 정점의 인덱스 반환

def shortest_path_dijkstra(vtx,adj,start):
    '''
    start 부터 다른 모든 정점까지의 최단경로를 계산하는 함수
    입력: vertex리스트, 입접행렬리스트,  start의 인덱스
    반환: path  (찾아진 최단경로)
    '''
    vsize=len(vtx)      #정점의 수
    dist=list(adj[start])   #dist리스트의 생성및 초기화 / start부터 다른 정점 까지의 최단경로거리를 저장하는 리스트
    path= [start]*vsize     #path리스트의 생성및 초기화 / 바로 이전 정점을 저장하는 리스트 / 바로 이전 정점을 따라 시작점으로 가는 경로가 최단경로다.
    found = [False]*vsize   #found리스트의 생성 및 초기화 / 방문한 정점을 표시하는 리스트 
    found[start]=True       #시작정점 start : 이미 찾아짐
    dist[start]= 0          #시작 정점의 거리 0 

    for i in range(vsize):                  #모든 정점에 대해서 반복
        print("step%2d: " %(i+1), dist)     #단계별 dist[] 출력
        u = choose_vertex(dist,found)       #최소 dist정점 u 탐색
        found[u] = True                     #u는 이제 찾아짐

        for w in range(vsize):              #모든 정점에 대해서 반복
            if not found[w]:                #아직 찾아지지 않았으면
                if dist[u]+adj[u][w]<dist[w]:    #갱신 조건 검사
                    dist[w]=dist[u]+adj[u][w]   #dist갱신
                    path[w]=u                   #이전 정점 갱신
    return path,dist


vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' 	]
weight = [ [0,	    7,		INF,		INF,		3,      10,		INF	],
           [7,		0,	    4,		10,	    2,	    6,	    INF	],
           [INF,	4,		0,		2,		INF,		INF,		INF	],
           [INF,	10,		2,		0,      11,		9,		4   ],
           [3,	    2,	    INF,   	11,		0,      13,		5   ],
           [10,	6,	    INF,		9,      13,		0,		INF	],
           [INF,   INF,		INF,   	4,		5,		INF,		0   ] ]   
print("Shortest Path By Dijkstra Algorithm")
start = 0
path,dist = shortest_path_dijkstra(vertex,weight,start)       #반환된 path,dist리스트
#최종경로 출력을 위한 코드
print("\n\n  start -> dst   Dist   Path")
for end in range(len(vertex)):                              #정점의 개수만큼 반복
    if end != start:                                        #start 가 아닐 때
        print("[최단경로: %s->%s] %s  %s"%                  
            (vertex[start],vertex[end],dist[end], vertex[end]),end='')  #경로와 거리와 최단경로를 출력
        while (path[end]!=start):                   #path[end]가 start가 아닐동안
            print(" <-%s"%vertex[path[end]],end='') # 경로를 출력
            end=path[end]
        print (" <-%s"%vertex[path[end]])