'''
작성자 : vvvv1111vvvv
작성일 : 2021.09.30

1. 목적: 스택을 활용하는 방법에 대해 실습한다.
2. 문제 : p4.2 : 스택을 이용하여 주어진 문자열이 회문인지 아닌지를
          결정하는 프로그램을 스택을 이용하여 작성하라.
3. 방법 : 문자열을 입력하면 스페이스, 구두점, 대소문자의 차이는 무시하고
          스택에 삽입한다. 스택에서 문자열을 다시 꺼내면서 입력한 문자열과
          하나씩 맞춰본다.
알고리즘:
1. 문자열을 키보드로부터 입력받는다.
2. 입력받은 문자열의 대소문자를 제외한 부분을 탈락시킨다.
3. 소소문자를 대문자로 처리한다.
4. 스택에 변환된 문자열을 삽입한다.
5. 변환된 문자열과 스택에 삽입된 문자열을 하나씩 비교한다.
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
def find(a):
    '''
    함수명 : find()
    목적 : 입력받은 문자열의 대소문자를 제외한 부분을 탈락시킨다,
    입력 : 문자열 a
    returns : 문자열 a의 대소문자 만을 데이터로 갖는 리스트
    '''
    p=re.compile('[a-zA-Z0-9]')      # 정규표현식 [a-zA-Z0-9] 을 컴파일해 결과를 객체 p에 돌려준다.
    result = p.findall(a)            # 메소드 findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
    return result

# 1. 문자열을 키보드로부터 입력받는다.
strStack=Stack()
a = input()                      # 대소문자, 공백, 기호를 포함한 문자열


#2. 입력받은 문자열의 대소문자를 제외한 부분을 탈락시킨다.
import re                        # 정규표현식을 지원하는 regular expression 모듈
a = find(a)                      # 대소문자를 포함한 리스트


#3. 소문자를 대문자로 처리한다.
for i in range(0, len(a)):
    a[i] = a[i].upper()          # 소문자를 모두 대문자로 변경한 리스트


#4. 스택에 변환된 문자열을 삽입한다.
for i in a:                      # strStack 스택에 리스트 a의 데이터를 0번째부터 넣는다.
    strStack.push(i)

#5. 변환된 문자열과 스택에 삽입된 문자열을 하나씩 비교한다.
b=[]
for i in range(strStack.size()):
    b.append(strStack.pop())

if a == b :
    print("회문입니다 ")
else:
    print("회문이 아닙니다.")
