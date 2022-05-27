'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.09.30

1. 목적 : 스택을 활용하는 방법에 대해 실습한다.
2. 문제 : p4.5 : 4.4절의 코드를 수정하여 사용자로부터 직접 중위표기 수식을 입력받아 이를 처리하여 결과를 출력하는 프로그램을 작성하라

3. 방법 : 4.4절 에서 만든 후위표기식 연산 프로그램과 중위표기 수식의 후위식 변환 프로그램을 활용
         
알고리즘 : 
1. 중위 표기식을 키보드로 입력받는다.
2. 중위 표기식의 후위 표기 변환함수 Infix2postfix()를 이용해 입력받은 식을 후위 표기식으로 변환
3. 후위 표기식의 연산 함수 evalPostfix()를 이용해 입력받은 후위표기식을 연산 한 뒤 결과를 반환
4. 계산 결과를 출력
'''

class Stack:                    # Stack 클라스 생성
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

def evalPost(expr):
    '''
    함수명 : evalPost()
    목적 : 후위 표기식 수식의 계산
    입력 : 후위 표기식 수식 (리스트)
    returns : 후위 표기식 수식의 계산결과
    '''
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'): s.push(val1 + val2)
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1*val2)
            else: s.push(val1/val2)
        else: s.push(float(token))
    return s.pop()

def precedence(op):
    '''
    함수명 : precedence()
    목적 : 연산자의 우선 순위 반환
    입력 : 연산자
    returns : 연산자의 우선 순위 level
    '''
    if op == '(' or op==')': return 0
    elif op in '+-' : return 1
    elif op in '*/' : return 2
    else : return -1


def Infix2Postfix(expr):
    '''
    함수명 : Infix2postfix()
    목적 : 중위 표기식 수식의 후위 표기식 변환
    입력 : 중위 표기식 수식 (리스트)
    returns : 후위 표기식 수식 (리스트)
    '''
    s1= Stack()                          # 괄호와 연산자 저장 스택
    output = []                          # 후위 표기식 출력 리스트
    for term in expr:           
        if term in '(':                  # 왼쪽 괄호이면
            s1.push('(')    
        elif term in ')':                # 오른쪽 괄호이면
            while not s1.isEmpty():
                op=s1.pop()
                if op=='(': break        # 왼쪽 괄호가 나올 떄까지
                else:                    # 스택에서 연산자를 꺼내 output에 추가
                    output.append(op)
        elif term in '+-*/':             # 연산자이면
            while not s1.isEmpty():      # 우선 순위가 높거나 같은 연산자를
                op = s1.peek()           # 스택에서 꺼내어 output에 추가 
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s1.pop()
                else: break
            s1.push(term)                # 스택의 마지막에 현재 연산자를 삽입
        else:                            # 피연산자 이면
            output.append(term)          # output에 추가

    while not s1.isEmpty():              # 처리가 끝났으면 스택의 남은 항목을
        output.append(s1.pop())          # 모두 output에 추가

    return output
        
        
# 1. 중위 표기식을 키보드로 입력받아 리스트로 변경한다.
a=list((input().split()))

# 2. 중위 표기식의 후위 표기 변환함수 Infix2postfix()를 이용해 입력받은 식을 후위 표기식으로 변환
postfix = Infix2Postfix(a)

# 3. 후위 표기식의 연산 함수 evalPostfix()를 이용해 입력받은 후위표기식을 연산 한 뒤 결과를 반환
result = evalPost(postfix)

# 4. 계산 결과를 출력
print("중위표기 : ", a)
print("후위표기 : ", postfix)
print("계산결과 : ", result)