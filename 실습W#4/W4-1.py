'''
작성자: vvvv1111vvvv
작성일: 2021.09.30

1. 목적 : 스택을 활용하는 방법에 대해 알아본다.
2. 문제 : p4.1 : 사용자로부터 문자열을 읽고
이것을 역순으로 출력하는 프로그램을 작성하라
3. 방법 : 4.2절에서 구현한 Stack 클라스를 사용

알고리즘:
1. 사용자로부터 문자열을 키보드로 입력받는다.
2. 입력받은 각 문자열을 스택에 push()한다.
3. 스택으로부터 문자를 연산자중복을 역순으로 이용해 화면에 출력한다.
'''
class Stack:                    # Stack 클라스를 만든다.
    def __init__(self):         # 생성자
        self.top = []           # 스택 : 공백 리스트
    def isEmpty(self):
        return len(self.top)==0
    def size(self):
        return len(self.top)
    def clear(self):
        self.top=[]
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

    def __str__(self):              # 연산자 중복 사용
        return str(self.top[::-1])  # 스택을 역순으로 출력

# 1. 사용자로부터 문자열을 키보드로 입력받는다.
newStack=Stack()
a = input()
n=0
# 2. 입력받은 각 문자열을 스택에 push()한다.
for i in a:
    newStack.push(i)
    n=n+1

# 3. 스택으로부터 문자를 연산자중복을 이용해 역순으로 화면에 출력한다.
print(' 스택 push %d회의 역순: %s' %(n, newStack))
