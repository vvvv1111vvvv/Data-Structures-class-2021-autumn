'''
작성자: vvvv1111vvvv
작성일: 2021.10.07

1. 목적: 큐와 덱을 활용하는 방법을 실습한다.
2. 문제: 2개의 스택을 사용하여 큐를 구현하라
3. 방법: 2 개의 스택 간에 element를 이동시킨다.

알고리즘:
아래의 알고리즘을 반복한다.
1. 문자를 키보드로부터 입력받는다.
2. 입력받은 문자를 스택#1에 삽입한다.
3. 만약 스택 #2가 비어있다면 스택 #1의 모든 element를 스택에 한 개씩 pop(-1)하여 모두 옮긴다.
4. 출력 요청이 들어오면 스택#2의 element를 pop(-1)하여 출력한다.
'''

class stack:                #스택 클래스
    def __init__(self):
        self.top=[]
    def isEmpty(self):
        return self.size()==0
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    def clear(self):
        self.top=[]
    def size(self):
        return len(self.top)
a = stack()                         #stack #1
b = stack()                         #stack #2

while True:
    #1. 문자를 키보드로부터 입력받는다.
    print("입력을 원하시나요 ? : O X")
    y= input()
    if y=='O':
        x=input("문자를 입력하세요")

    #2. 입력받은 문자를 스택#1에 삽입한다.
        a.push(x)

    #3. 만약 스택 #2가 비어있다면 스택 #1의 모든 element를 스택에 한 개씩 pop(-1)하여 모두 옮긴다.
    if b.isEmpty():
        for i in range(0,a.size()):
            b.push(a.pop())

    #4. 출력 요청이 들어오면 스택#2의 element를 pop(-1)하여 출력한다.
    print("출력을 원하시나요 ? : O X")
    y= input()
    if y=='O':
        print(b.pop())
