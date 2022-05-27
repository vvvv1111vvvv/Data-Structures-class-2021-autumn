'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.18

1. 목적: 그래프의 개념과 용어를 이해하고, 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 10.5: 인접리스트(딕셔너리와 집합)으로 표현된 그래프에 대해 위상정렬 알고리즘을 구현하라.
        정점의 진입차수를 저장하는 inDeg의 처리가 까다로울 수 있다. inDeg를 딕셔너리로 처리해 보라
3. 방법 : 10.2절의 함수와 테스트 코드를 응용한다.

알고리즘
#1. 인접리스트로 graphf를 표현
#2. 위상정렬을 출력하는 함수 topological_sort_AM(graph)를 호출
#3. topological_sort_AM(graph)
    #3-1. 진입차수 정장을 위한 빈 딕셔너리 inDeg 선언 
        #3-1-1. graph의 Key값을 key로 가지고, value=0인 딕셔너리값 추가
    #3-2. graph의 key와 value krqtdp 대해 key가 어떤 value의 원소이면 진입차수를 1 추가한다.
    #3-3. 진입차수가 0인 vertex의 리스트를 정의, 진입차수가 0안 key들을 vlist에 append()한다.
    #3-4. 진입차수가 0인 vertex의 리스트'의 크기가 0이 아닐 동안  vlist에 저장된 vertex를 1개 꺼낸다.  
    #3-5. graph의 u번째 key에서 반복
        #3-5-1.만약 u가 방금 꺼낸 v와 다르고, v의 진출간선에 u가 존재 한다면
        #3-5-2. 진압차수를 -1 감소, u의 차수가 0이면 vlist에 추가

'''

def topological_sort_AM(graph):
    inDeg={}        #진입차수 저장을 위한 빈 딕셔너리 선언
    for i in graph: #graph의 Key값을 key로 가지고, value=0인 딕셔너리값 추가
        inDeg[i]=0

    for j in graph.values():    #graph의 j번째 value(집합)에서 반복
        for i in graph.keys():  #inDeg의 i번째 key에서 반복
            if i in j:          #만약 key가 value의 원소이면
                inDeg[i]+=1     #진입차수를 1추가
    print(inDeg)                #진입차수를 출력

    vlist=[]                    #진입차수가 0인 vertex의 리스트
    for i in graph:             #진입차수가 0안 key들을 vlist에 append()한다.
        if inDeg[i]==0:
            vlist.append(i)
    while len(vlist)>0:     #'진입차수가 0인 vertex의 리스트'의 크기가 0이 아닐 동안        
        v=vlist.pop()       #vlist에 저장된 vertex를 1개 꺼낸다.
        print(v,end=' ') 
        
        for u in graph:     #graph의 u번째 key에서 반복
            if v!=u:    # 만약 u가 방금 꺼낸 v와 다르고, 
                if u in  graph[v]:      #v의 진출간선에 u가 존재 한다면
                    inDeg[u]-=1     #잔압차수를 -1 감소
                    if inDeg[u]==0: #u의 차수가 0이면
                        vlist.append(u) 





graph={'A':{'C','D'},
        'B':{'E','D'},
        'C':{"D","F"},
        'D':{"F"},
        'E':{"F"},
        'F':{None}}
topological_sort_AM(graph)