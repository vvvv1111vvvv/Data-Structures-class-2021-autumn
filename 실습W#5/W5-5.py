'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.10.08

1. 목적: 스택을 활용하는 방법에 대해 실습한다.
2. 문제 : p5.5절을 참고하여 정렬된 배열을 이용한 우선순위 큐를 구현하라

3. 방법 : p5.5점을 알고리즘을 활용해 정렬된 배열을 삽입했을때의 우선순위 큐를 구현한다.
알고리즘:
1. 정렬된 배열을 정의한다.
2. 우선순위 큐 클래스를 만든다.
3. 정렬된 배열을 우선순위 큐에 삽입한다.
4. 우선순위 큐에서 출력한다.
'''
class PriorityQueue():          #우선순위 큐 클래스
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
a=[144,123,94,65,50,49,38,21,16,14,2,0] #정렬된 배열
b=PriorityQueue()

#3. 정렬된 배열을 우선순위 큐에 삽입한다.
for i in a:
    b.enqueue(i)
#4. 우선순위 큐에서 출력한다.
for i in range(4):
    print(b.dequeue())