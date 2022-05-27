'''
작성자 : vvvv1111vvvv
작성일 : 2021.09.30

1. 목적 : 스택을 활용하는 방법에 대해 실습한다.
2. 문제 : p4.3 : 4.3절의 괄호검사 프로그램을 다음과 같이 확장하라
                (1) 소스코드 파일을 읽어 검사하는 프로그램을 완성하라
                (2) 괄호 매칭이 실패하면 조건 1~3중 어떤 조건을 위반했는지 출력할 수 있도록 하라. 에러코드 반환
                (3) 괄호 매칭이 실패한 위치를 라인수, 문자수로 나타내어 출력하라.
3. 방법 : 4.3 절의 괄호검사 프로그램과 3.4절의 라인편집기 프로그램을 활용
알고리즘 :
1. 파일을 연 뒤 readlines() 함수를 사용해 라인별로 읽은 리스트를 생성
2. 리스트의 모든 문자열에 대해 괄호검사 실행
3. 괄호매칭이 실패하면 (에러코드와 라인수, 문자수)를 반환합니다.
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


def checkBrackets(lines):
    '''
    함수명 : checkBrackets(lines)
    목적 : 소스코드 파일의 괄호 검사 및 에러 여부
    입력 : lines : 소스코드 파일 각 line 문자열의 리스트
    returns : 에러코드 0~3, 에러 라인의 위치(세로), 에러 문자의 위치(가로)
    '''
    stack=Stack()
    i=0                                 # i : 라인의 위치
    for line in lines:                  # lines : 각 line의 문자열을 데이터로 갖는 리스트
        j=0                             # j : 문자의 위치
        for ch in line:                 # line : 문자열, ch in line : 문자열 line의 ch번째 str
            if ch in ('{', '[', '('):
                stack.push(ch)
            elif ch in (']', '}', ')'):
                if stack.isEmpty():
                    return 2, i, j
                else:
                    left = stack.pop()
                    if (ch=="}" and left != "{") or\
                        (ch=="]" and left != "[") or \
                        (ch == ")" and left != "("):
                        return 3, i, j
            j+=1
        i+=1
    if stack.isEmpty():
        return 0, 'No Error'
    else:
        return 1, 'End point'




#1. 파일을 연 뒤 readlines() 함수를 사용해 라인별로 읽은 리스트를 생성
filename = input(".py 파일의 주소를 입력하세요")
infile = open(filename, 'r' ,encoding='utf-8')
lines= infile.readlines()
infile.close()
#2. 리스트의 모든 문자열에 대해 괄호검사 실행
#3. 괄호매칭이 실패하면 에러코드와 라인수, 위치를 반환합니다.
result = checkBrackets(lines)               # 에러코드와 라인수, 위치가 튜플의 형태로 반환
print(result)
