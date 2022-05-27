'''
작성자: vvvv1111vvvv
작성일: 2021.10.07

1. 목적: 큐와 덱을 활용하는 방법을 실습한다.
2. 문제: 큐를 활용해 피보나치 수열을 계산하는 프로그램을 작성
3. 방법: 길이가 3인 원형 큐를 만들어 front 부터 2개의 합을 rear에 삽입하는 연산을 반복한다.

알고리즘:
1. 수를 키보드로부터 입력받는다.
2. 길이가 3인 원형 큐를 만든다.
3. 입력한 수 번째 피보나치항을 찾기 위해 front 2개를 더한 값을 rear 다음에 삽입하는 연산을 n-1번 반복한다.
4. rear의 값을 출력한다.
'''
max_size=3
class CircularQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.items=[0]*max_size
    def isEmpty(self):
        return self.front==self.rear
    def clear(self):
        self.items=[]
    def isFull(self):
        return self.front==(self.rear+1)%max_size
    def enqueue(self,item):
        if not self.isFull():
            self.rear=(self.rear+1)%max_size
            self.items[self.rear]=item
    def dequeue(self):
        if not self.isEmpty():
            self.front= (self.front+1)%max_size
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.item[(self.front+1)%max_size]
#1. 수를 키보드로부터 입력받는다.
n= int(input())
#2. 길이가 3인 원형 큐를 만든다.
q=CircularQueue()
q.enqueue(0)
q.enqueue(1)
#3. 입력한 수 번째 피보나치항을 찾기 위해 front 2개를 더한 값을 rear 다음에 삽입하는 연산을 n-1번 반복한다.
for i in range(n-1):
    z=q.items[(q.front+1)%max_size]+q.items[(q.front+2)%max_size]
    q.dequeue()
    q.enqueue(z)
#4. rear의 값을 출력한다.
print(q.items[q.rear])
