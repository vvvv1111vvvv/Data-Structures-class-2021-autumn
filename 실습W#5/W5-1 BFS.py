'''
작성자: vvvv1111vvvv
작성일: 2021.10.07

1. 목적: 큐와 덱을 활용하는 방법을 실습한다.
2. 문제: p5.1: 스텍이나 큐를 직접 구현할 필요 없이 파이썬의 큐모듈을 이용해 미로탐색 프로그램을 구현할 수 있다.
         5.3절의 코드를 수정하여 파이썬의 큐 모듈을 이용한 깊이우선탐색과 너비우선탐색 함수를 구현하라
3. 방법: 5.3절의 코드를 수정하여 활용한다.

알고리즘: 너비우선탐색
1. 파이썬의 큐모듈을 불러온다.
2. 위치 x,y가 움직일 수 있는 공간 인지 확인하는 함수 isValidpos()를 만든다.
    2-1. 튜플(x,y)를 입력 받는다.
    2-2. 만약 x또는 y가 map 의 바깥으로 벗어나면 False를 리턴하고, (x,y)의 위치에 '0' 또는 'x'가 있다면 True를 리턴한다.
3.  너비우선탐색함수 BFS()를 만든다.
    3-1. 미로를 탐색할 때, 각 위치를 저장할 큐를 큐 모듈을 이용해 만든다.
    3-2. 큐에 시작위치 (0,1)을 삽입한다.
    3-3. Q가 비어있지 않는동안 while 문으로 반복한다.
        3-3-1. Q에서 get()한뒤 (x,y)튜플에 삽입하고, 출력한다.
        3-3-2. 만약 map[y][x]가 'x'라면 return True 하여 반복문을 마친다.
        3-3-3. 그렇지 않으면 현재위치 (x,y) '.'을 삽입하고, (x,y)에 대해 상,하,좌,우로 한 칸 씩 이동 한 값을 isValidpos()로 검사하고, True이면 해당 위치를 Q에 put한다.
    3-4 만약 모든 탐색이 끝났는데 'x'에 도달하지 못했으면, return False 한다.
4. map을 리스트를 이용해 만든다.
5. map_size를 정의한다.
6. 함수 BFS()를 호출하고 결과를 Return 받아 참이면, 미로탐색성공을 ,거짓이면 미로탐색 실패를 출력한다.
'''

import queue        #queue모듈을 포함
def isValidpos(x,y,map_size=6):
    if x<0 or y<0 or x>=map_size or y>=map_size:
        return False
    else:
        return map[y][x]=='0' or map[y][x]=='x'

def BFS():
    q=queue.Queue(maxsize=20)         #queue모듈의 Queue함수 q
    q.put((0,1))             #queue 모듈에서 enqueue()

    print("BFS : ")
    while not q.empty() :
        x,y=q.get()
        print((x,y),end='-->')
        if map[y][x]=='x':
            return True
        else:
            map[y][x]='.'
            if isValidpos(x+1,y): q.put((x+1,y)) # 우
            if isValidpos(x-1,y): q.put((x-1,y)) # 좌
            if isValidpos(x,y+1): q.put((x,y+1)) # 상
            if isValidpos(x,y-1): q.put((x,y-1)) # 하

    return False


map=[['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']]
maze_size=6
result=BFS()
if result :print(" --> 미로탐색 성공")
else : print(' --> 미로탐색 실패')
