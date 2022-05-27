class A: #클래스 A 생성
    def __init__(self): #클래스 A의 생성자 함수
        self.elem=[] #공백리스트 생성 / self. 으로 참조되는 멤버변수/ 클래스의 속성을 나타낸다

    def insert(self,pos,item): # 멤버함수 self로 참조되며, pos와 item을 입력받는다.
        self.elem.append(item) # 입력 받은 인수 item을 self.elem 리스트의 맨뒤에 추가
        for i in range(len(self.elem)-(pos)-1): # 입력받은 인수 item이 인수 pos자리에 insert 하기 위해서, 'pos'자리 부터 '맨 마지막 자리-1'번째 자리까지 리스트의 값을 append 함수를 이용해 리스트의 맨 뒤에 추가한다. 그뒤 리스트의 값을 remove 한다.
            self.elem.append(self.elem[pos])
            self.elem.remove(self.elem[pos])

    def delete(self,pos):  # 멤버함수 self로 참조되며, pos를 입력받는다.
        self.elem.append(self.elem[pos]) # pos번째 위치에 있는 항목을 리스트의 맨 뒤에 추가
        for i in range(pos,len(self.elem)-1): # pos와 마지막 위치에 있는 숫자를 1씩 앞의 위치에 삽입
            self.elem[i]=self.elem[i+1]
        self.elem.pop(-1);self.elem.pop(-1) # 마지막 위치와 그 앞 위치에 존재하는 pos위치의 수 2개를 꺼낸다.

    def find(self,item): # 메소드, self로 참조, item 을 인수로 가진다.
        for i in range(0, len(self.elem)): #item과 리스트의 i번 째 값을 비교하는 for문 
            if item == self.elem[i]:
                return i    # 제일 먼저 item과 일치하는 리스트의 위치값을 반환 

    def merge(self, lst): # 메소드, self로 참조, lst 을 인수로 가진다.
        for i in range(0,len(lst.elem)): # for문을 사용해 리스트 d1의 뒤에 리스트 d1을 추가한다.
            self.elem.insert(len(self.elem)+i,lst.elem[i])
    

        

a1=A() # append()를 사용한 insert() 구현/ 클래스 A의 객체 a1 생성
a1.insert(0,5);print(a1.elem) # 클래스 A의 멤버함수 a1.insert를 호출 한다.(pos=0, item=5)/ 그 뒤 객체 a1의 리스트를 출력
a1.insert(1,4);print(a1.elem)
a1.insert(0,7);print(a1.elem)
a1.insert(2,2);print(a1.elem)
a1.insert(3,9);print(a1.elem)
a1.insert(1,41);print(a1.elem)
a1.insert(0,44);print(a1.elem)
a1.insert(5,16);print(a1.elem, "\n\n")

b1=A() # pop(-1)를 사용한 delete() 구현/ 클래스 A의 객체 b1 생성
b1.elem=[27, 35, 1, 0, 17, 154] #숫자리스트
b1.delete(4);print(b1.elem)  # 클래스 A의 멤버함수 b1.delete를 호출 한다.(pos=4)/ 그 뒤 객체 b1의 리스트를 출력
b1.delete(1);print(b1.elem) 
b1.delete(2);print(b1.elem) 
b1.delete(0);print(b1.elem,"\n\n") 

c1=A() # index()를 사용하지 않는 find()연산 구현/ 클래스 A의 객체 C1 생성
c1.elem=[27, 35, 1, 0, 17, 154] #숫자리스트
print(c1.find(35)) # 클래스 A의 멤버함수 c1.find()를 호출한다. (item=35)
print(c1.find(27))
print(c1.find(0))
print(c1.find(154))
print(c1.find(1004),"\n\n")

d1=A() # merge()연산을 extend()를 사용하지 않고 구현
d2=A()
d1.elem=[27, 35, 1, 0, 17, 154, 1004] #숫자리스트
d2.elem=['제주도', '울릉도', '서귀포', '백두산'] #문자열 리스트
d1.merge(d2) # 클래스 A의 멤버함수 merge()를 호출한다.
print(d1.elem)
