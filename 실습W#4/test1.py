class Stack:
    def __init__(self): #생성자
        self.top=[]     # 데이터 맴버 top의 정의 및 초기화 (스택-공백리스트)
    def isEmpty(self):
        return len(self.top)==0
    def size(self):
        return len(self.top)
    def claer(self):
        self.top=[]
    def push( self, item ):
        self.top.append(item)
    def pop( self ):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek( self ):
        if not self.isEmpty():
            return self.top[-1]
    def __str__( self ):
        return str(self.top[::-1])



 # 1. Stack 클래스의 객체 odd 와 even 을 생성한다.
odd = Stack()      # 홀수 저장을 위한 스택
even = Stack()     # 짝수 저장을 위한 스택
for i in range( 10 ):
    if i % 2 == 0:
        odd.push(i)
    else:
        even.push(i)
print(" 스택 even 5회 : ", even)
print(" 스택 odd 5회 : ", odd)
print("스택 even   peek: ", even.peek())
print("스택 odd   peek", odd.peek())

for i in range(2):
    even.pop()
    odd.pop()
print("스택 even 의 pop 2회 : ", even)
print("스택 odd의 pop 2회 : ", odd)
print(odd.top[4::-1])
