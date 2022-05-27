'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.25

1. 목적: 가중치그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 11.2: 11.3절의 kruskal의 최소비용신장트리코드를 수정하여 구해진 MST의 가중치
        합을 출력하라
3. 방법 : 11.3절의 함수와 테스트 코드를 응용한다.

#최소비용신장트리 (MST): 1. 그래프의 모든정점들은 연결한다.
                        2. 가중치 합이 최소
                        3. 사이클 없이 N-1개의 간선

알고리즘
#1. 인접행렬을 이용해 그래프를 구현한다.
#2. Kruskal의 최소신장트리 알고리즘함수 MSTKruskal()를 호출한다.
    #2-1. 변수 vsize에 정점의 개수를 저장, 정점 집합 초기화 init_set()호출, 간선리스트를 빈리스트로 선언
    #2-2. 모든간선을 간선리스트에 추가 (튜플로 간선과 가중치를 eList에 저장, i,j 는 인덱스)
    #2-3. 간선리스트의 가중치를 내림차순으로 정렬: 람다함수 사용
    #2-4. 가중치의 합을 저장하는 변수 sum=0, 간선의 수를 저장하는 변수 edgeAccepted=0 선언
    #2-5. 간선의 개수가 정점의 개수보다 1 작을 동안 반복
        #2-5-1.  가중치가 가장 작은 간선의 두 정점이 속한 집합을 비교한다. find()호출
        #2-5-2. 두 정점이 속한 집합이 다르면 "간선추가 : (vertex1,vertex2, 가중치)" 출력
        #2-5-3. 가중치의 합을 추가한다.
        #2-5-4. 두 정점을 포함하는 집합을 합한다 union()호출, 간선의 수를 1 추가한다.
    #2-6. 가중치의 합을 출력
'''
parent=[]       #각노드의 부모노드 인덱스
set_size=0      #전체 집합의 개수
def init_set(nsets):
    '''
    집합 초기화 함수(모든 정점들이 자신의 트리의 루트노드가 되도록한다.)
    입력: 집합의 크기
    출력: 없음
    '''
    global set_size,parent  #전역변수 사용
    set_size=nsets          #집합의 크기
    for i in range(nsets):   #집합의 크기만큼
        parent.append(-1)   #각각이 고유집합(부모가 -1)
def find(id):
    '''
    정점 id가 속한 집합을 찾는 함수(id가 속한 트리의 루트노드 인덱스를 반환)
    입력: 정점의 id
    반환: id
    '''
    while (parent[id]>=0):  #연결된 집합의 부모가 존재하는 동안
        id=parent[id]       #id를 부모의 id로 갱신
    return id               #최종 id를 반환 (트리의 맨위의 노드 id)
def union(s1,s2):
    '''
    두 집합을 병합 (s1을 s2로)
    입력: s1, s2 (인덱스값)
    출력: 없음
    '''
    global set_size,parent  #전역변수 사용
    parent[s1]=s2           #s1을 s2에 병합 (s1번째 인덱스가 s2의 인덱스를 저장하는것으로 구현)
    set_size-=1



def MSTKruskal(vertex,adj):
    '''
    Kruskal의 최소비용신장트리 프로그램
    입력: 정점리스트,입력행렬리스트
    출력: 없음
    '''
    vsize=len(vertex)   #정점의 개수
    init_set(vsize)     #정점 집합 초기화// 모든정점이 각각 고유의 집합이 되도록 한다.
    eList=[]            #간선 리스트

    for i in range(vsize-1):    #모든간선을 간선리스트에 추가(삼각형)
        for j in range(i+1,vsize):
            if adj[i][j]!=None:
                eList.append((i,j,adj[i][j])) #튜플로 간선과 가중치를 eList에 저장, i,j 는 인덱스
    
    #간선리스트의 가중치를 내림차순으로 정렬: 람다함수 사용
    eList.sort(key=lambda e:e[2],reverse=True)  #sort key = e[2], reverse연산을 한다.
    sum=0       # 가중치의 합
    edgeAccepted=0  #간선의 수를 저장하는 변수 (maximum = vertex-1)
    while (edgeAccepted < vsize-1):
        e=eList.pop(-1)     # e : 가중치가 가장 작은 간선
        uset = find(e[0])       #두 정점이 속한 집합번호
        vset  = find(e[1])
        if uset != vset:        #두 정점이 속한 집합이 다르면
            print("간선추가: (%s,%s,%d)" %          #간선추가 (vertex1,vertex2, 가중치) 출력
                 (vertex[e[0]],vertex[e[1]],e[2]))
            sum+=e[2]
            union(uset,vset)    #두 정점을 포함하는 집합을 합한다,
            edgeAccepted +=1    #간선의 수를 1 추가한다.
    print("가중치의 합: %d" %(sum))
vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]    

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)      #MSTKruskal 함수 호출, 매개변수 vertex,weight










