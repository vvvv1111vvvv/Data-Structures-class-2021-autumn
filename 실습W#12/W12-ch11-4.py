'''
작성자 : vvvv1111vvvv
작성일 : 2021.11.25

1. 목적: 가중치그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 11.4: Prim의 최소비용 신장트리 코드를 수정하여 구해진 MST의 가중치의 합을 출력
3. 방법 : 11.3절의 함수와 테스트 코드를 응용한다.

#최소비용신장트리 (MST): 1. 그래프의 모든정점들은 연결한다.
                        2. 가중치 합이 최소
                        3. 사이클 없이 N-1개의 간선

알고리즘
#1. 인접행렬을 이용해 그래프를 구현한다.
#2. Prim의 최소신장트리 알고리즘함수 MSTPrim()를 호출한다.
    # 2-1. 정점의 크기를 변수 vsize에 저장
    # 2-2. 현재까지 구성된 MST 트리에 속한 정점에서 i번쨰 정점까지의 가장 가까운 거리를 나타내는 리스트 dist를 INF로 초기화
    # 2-3. 선택여부를 확인하는 리스트 selected를 False로 초기화
    # 2-3. dist[0]을 0으로 초기화
    # 2-4. 간선 가중치 출력을 위해, 이전 정점의 인덱스를 저장하는 변수 oldU를 0으로 초기화
    # 2-5. 간선가중치의 합 저장을 위한 변수 sum을 0으로 초기화
    # 2-6. 정점의 수만큼 반복
        # 2-6-1. 현재까지 구성된 MST에서 가장 가까운 거리에 있는 정점의 인덱스를 getMinVertex()함수를 호출하여
                반환. 반환된 값을 u에 저장
                # 2-6-1-1. 최단거리 정점 minv를 0
                # 2-6-1-2. 최단거리 를 INF
                # 2-6-1-3. 모든 정점에 대해 반복
                    # 2-6-1-3-1. 선택이 안되었고 가중치가 가장 작으면
                        # 2-6-1-3-1-1. mindist 갱신, minv 갱신
                # 2-6-1-4. 최단거리의 정점을 반환
        # 2-6-2. selected리스트의 u번째 인덱스의 값을 True로 변경
        # 2-6-3. u번째 정점을 출력
        # 2-6-4. 가중치가 None이 아닐 때
            # 2-6-4-1. u번째 정점과 u-1번째 정점 사이의 가중치를 sum에 더한다.
        # 2-6-5. 정점의 인덱스를 oldU에 저장
        # 2-6-6. 정점 v에 대해서 반복
            # 2-6-6-1. 정점 u,v사이에 간선이 있으면
                # 2-6-6-1-1. 선택되지않았고, 가중치가 이전에 저장된 값보다 작으면
                    # 2-6-6-1-1-1. 정점u,v 사이의 거리가 mst에서  정점v까지의 최단거리
    # 2-7. 정점 가중치의 합 sum 출력
#3.



'''
INF=9999
def getMinVertex(dist, selected):
#현재 트리에 인접한 정점들 중에서 가장 가까운 정점을 찾는 함수
    minv=0
    mindist=INF
    for v in range(len(dist)):  #for all vertex
        if not selected[v] and dist[v]<mindist: #선택이 안되었고 가중치가 가장 작으면
            mindist=dist[v]     #mindist 갱신 (최단거리)
            minv=v              #minv 갱신      (최단거리의 정점)
    return minv     #최단거리의 정점을 반환(인덱스값)




def MSTPrim(vertex,adj):
    vsize=len(vertex)       #정점의 크기
    dist=[INF]*vsize        #현재까지 구성된 MST트리에 속한 정점에서 i번재 정점 까지의 가장 가까운거리를 저장하는 리스트
                            #dist=[INF,INF,INF, ...]로 초기화
    selected = [False]*vsize    #selected=[False, False, False , ...]로 초기화
    dist[0]=0               #dist=[0,INF,INF, ...], vertex 0번째부터 시작("A")
    oldU=0                  #간선 가중치 출력을 위한 인덱스
    sum=0                   #가중치의 합 저장
    for i in range(vsize):  #정점의 수만큼 반복
        u=getMinVertex(dist,selected)   #현재까지 구성된 MST에서 가장 가까운 거리에 있는 정점의 인덱스
        selected[u]=True            #u는 선택됨
        print(vertex[u],end=' ')    #u번째 정점을 출력
        if adj[oldU][u] is not None:    #[A][A]가 None인 case 제외
            sum+=adj[oldU][u]           #추가된 정점과 이전 정점 사이의 가중치를 sum에 더한다.
        oldU=u                      #이전 정점의 인데스
        for v in range(vsize):      #내부루프
            if (adj[u][v] !=None): #정점 u와 정점 v 사이에 간선이 있으면
                if selected!=True and adj[u][v]<dist[v]: #선택되지않았고, 가중치가 이전에 저장된 값보다 작으면
                    dist[v]=adj[u][v]       #정점u,v 사이의 거리가 mst에서  정점v까지의 최단거리
    print("\n정점의 가중치의 합 : %d"%(sum))


vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]
print("MST by Prim's Algorithm")
MSTPrim(vertex,weight)
