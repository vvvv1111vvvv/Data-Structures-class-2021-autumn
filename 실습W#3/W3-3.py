class Set: # 집합 클래스
    def __init__ (self):    # 생성자 함수   
        self.items=[]       #원소를 저장하기 위한 리스트 생성
    def contains(self, item):   #메소드(멤버 함수) self로 참조되며, item 을 인수로 갖는다.
        global i            #전역변수 i
        for i in range (0,len(self.items)): # 입력받은 item과 Set의 원소 중 동일한 것이 있는 지 확인한다
            if self.items[i]==item: # Set 내부에 동일한 원소가 존재하면 
                return True #True 를 리턴
        return False # Set내부에 동일한 원소가 존재하면 False 를 리턴
    def delete(self, item):#delete 메소드 함수 self를 참조, item 을 인수로 갖는다.
        if self.contains(item)==True: #Self가 item 을 원소로 갖고 있으면 해당 원소를 꺼낸다.
            self.items.pop(i)
    def insert(self,item): # 리스트와 달리 position이 없다.
        if self.contains(item)==False: #Self가 item 을 원소로 갖고 있지 않으면 리스트 self의 마지막에 item을 추가한다.
            self.items.append(item)
    def union(self,SetB): #메소드(멤버함수) 두 set의 합집합을 구한다.
        SetC=Set()  # Set클래스의 객체 SetC를 생성한다. 
        SetC.items=list(self.items) # SetA의 원소를 SetC에 복사한다.
        for j in range(0,len(SetB.items)): # for문을 활용해 SetB의 원소들중 SetA에 없는 것을 append를 이용해 SetC에 추가한다.
            if self.contains(SetB.items[j])==False:
                SetC.items.append(SetB.items[j])
        return SetC #SetC를 리턴한다.
    def intersect(self, SetB): #메소드(멤버함수) 두 set의 교집합을 구한다.
        SetC=Set()  # Set클래스의 객체 SetC를 생성한다
        for j in range (0, len(SetB.items)):# for 문을 활용해 SetA가 SetB와 공통으로 contain 하고 있는 원소를 SetC에 append 한다.
            if self.contains(SetB.items[j])==True:
                SetC.items.append(SetB.items[j])
        return SetC         #SetC를 리턴한다.
    def difference(self, SetB):  #메소드(멤버함수) 두 set의 차집합을 구한다.
        SetC=Set()  # Set클래스의 객체 SetC를 생성한다
        for j in range (0, len(self.items)):  # SetA에서 SetB에 포함되지 않은 원소들을 SetC에 append한다.
            if SetB.contains(self.items[j])==False:
                SetC.items.append(self.items[j])
        return SetC     #SetC를 리턴한다.

    def __sub__(self,SetB): # 연산자 재정의
        SetC=Set()  # Set클래스의 객체 SetC를 생성한다
        for j in range (0, len(self.items)):  # SetA에서 SetB에 포함되지 않은 원소들을 SetC에 append한다.
            if SetB.contains(self.items[j])==False:
                SetC.items.append(self.items[j])
        return SetC  #SetC를 리턴한다.

    def isSubsetOf(self, otherset): #메소드 : self set이 otherset의 부분집합인지 구한다.
        n=0
        for j in range (0, len(self.items)):# self set의 모든 원소가 otherset의 원소인지 확인한다.
            if otherset.contains(self.items[j])==True:
                n+=1        #self set의 원소가 otherset의 원소일 경우 n+=1
        if n==len(self.items): #n이 self set의 원소의 수와 같다면 True를 리턴
            return True
        else:           #아닐 경우 False를 리턴
            return False
            

SetA=Set() # SetA는 클래스 Set 객체
SetB=Set() # Setㅠ는 클래스 Set 객체

SetA.insert('사과나무') #Set 클래스의 insert 메소드를 호출한다.
SetA.insert('lion')  
SetA.insert('Grape')
SetA.insert('고구마')
SetA.insert('수박')
print("Set A : ",SetA.items) #SetA의 원소를 출력한다.

SetB.insert('코끼리')
SetB.insert('사과나무')
SetB.insert('수박바')
SetB.insert('상어바')
print("Set B : ",SetB.items)   #SetA의 원소를 출력한다.

print("합집합 : ", SetA.union(SetB).items) #SetA와 SetB의 합집합을 출력한다.
print("교집합 : ", SetA.intersect(SetB).items)   #SetA와 SetB의 교집합을 출력한다.
print("차집합 : ",SetA.difference(SetB).items) #SetA의 SetB에 대한 차집합을 출력한다.
print("차집합 : ",(SetA-SetB).items) #SetA의 SetB에 대한 차집합을 연산자 중복을 이용해 출력한다.
print(SetA.isSubsetOf(SetB)) #SetA가 SetB의 부분집합인 지 검사한뒤 True False를 출력