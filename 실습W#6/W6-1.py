'''
작성자 : vvvv1111vvvv
작성일 : 2021.10.15

1. 목적: 연결된 구조를 활용하는 방법에 대해 실습한다.
2. 문제 : 연결된 스택을 활용하여 주어진 문자열이 회문인지 아닌지 결정하는 프로그램을 작성하라

3. 방법 : 1. p6.2절의 연결된 스택 알고리즘을 활용한다.
          2. 문자열을 입력하면 스페이스, 구두점, 대소문자의 차이는 무시하고
          연결된 스택에 삽입한다. 연결된 스택에서 문자열을 다시 꺼내면서 입력한 문자열과
          하나씩 맞춰본다.
알고리즘:
1. 문자열을 키보드로부터 입력받는다.
2. 입력받은 문자열의 대소문자를 제외한 부분을 탈락시킨다.
3. 소소문자를 대문자로 처리한다.
4. 스택에 변환된 문자열을 삽입한다.
5. 변환된 문자열과 스택에 삽입된 문자열을 하나씩 비교한다.
'''

class Node:     #단순연결을 위한 노드
    def __init__(self,elem,link=None):      #생성자 디폴트 인수 사용
        self.data = elem                    #데이터 멤버 생성 및 초기화
        self.link= link                     #링크 생성 및 초기화

class LinkedStack:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        return self.top==None
    def clear(self):
        self.top=None
    def push(self, item):           #여기서 링크 연결이 생긴다.
        n=Node(item,self.top)
        self.top=n
    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top=self.top.link
            return data
    def peek(self):
        if not self.isEmpty:
            return self.top.data
    def size(self):
        n=self.top
        count=0
        while not n == None:
            n=n.link
            count+=1
        return count
    def display(self, msg='LinkedStack:'):
        print(msg, end="")
        node = self.top
        while not node == None:
            print(node.data)
            node=node.link
        print()

import re
def a(x):
    p=re.compile('[a-zA-Z0-9]')
    result = p.findall(x)
    return result

s=LinkedStack()
b=LinkedStack()

#1. 문자열을 키보드로부터 입력받는다.
stringA=input()

#2. 입력받은 문자열의 대소문자를 제외한 부분을 탈락시킨다.
stringA=a(stringA)

#3. 소소문자를 대문자로 처리한다.
for i in range(int(len(stringA))):
    stringA[i]=stringA[i].upper()

#4. 스택에 변환된 문자열을 삽입한다.
for i in stringA:
    s.push(i)

#5. 변환된 문자열과 스택에 삽입된 문자열을 하나씩 비교한다.
num=len(stringA)
for i in range(0,num):
    if stringA.pop(0)!=s.pop():
        print("회문이 아닙니다.")
        quit()
print("회문입니다.")
