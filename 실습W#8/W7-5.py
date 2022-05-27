'''
작성자 : 박수영 2018930012 07mak8mgt@office.uos.ac.kr
작성일 : 2021.11.04

1. 목적: 탐색을 활용하는 방법에 대해 실습한다.
2. 문제 : 실습 7.5 : 7.7절에서 구현한 순차탐색 맵을 수정하여 이진탐색 맵으로 구현하라 

3. 방법 : 7.5절에서 구현한 리스트를 이용한 순차 탐색 맵을 수정하여 
        정렬 시킨다, 이진탐색 맵으로 변경한다.
          
알고리즘:
#1. 삽입연산: 엔트리 삽입 시 킷값에 따라 위치를 찾아 삽입 
#2. 삭제연산 : 순서탐색 맵과 동일                       
#3. 탐색연산 : binaty_search() function을 사용한다.    
#4. 
'''
class Entry :
    '''
        이름: 엔트리 클래스
        목적: 헤시 맵 구현을 위해 사용, 맵은 엔트리의 집합       
    '''                          
    def __init__(self,key,value):
        self.key = key              # key값
        self.value=value            # value 값

    def __str__(self):              #overriding (객체를 문자열로 전환)
        return str("%s:%s"%(self.key,self.value))



class BinaryMap:
    '''
    이름: 이진탐색 맵 클래스
    목적: 데이터 맴버로 엔트리를 저장할 테이블
    '''
    def __init__(self):
        self.table=[]         #맵의 레코드 테이블

    def size(self): return len(self.table)

    def display(self,msg):
        print(msg)
        for entry in self.table:
            print(" ",entry)

    def insert(self,key,value):
        x=Entry(key,value)
        a=self.hashFn(key)
        if self.size()==0:
            self.table.insert(0,x)
        else:
            for i in range (0,self.size()):
                if self.hashFn(self.table[i].key)<=a:
                    if i==self.size()-1 or self.hashFn(self.table[i+1].key)>=a:
                        self.table.insert(i+1,x)
                        return
                    continue
                elif self.hashFn(self.table[0].key)>=a:
                    self.table.insert(0,x)
                    
        

    def hashFn(self, key):
        '''
        이름: key를 입력받아 주소를 계산해 반환하는 해시함수
        방법: 문자열 key 를 입력받아 각문자의 코드 값을 모두 더하고
                이를 테이블 크기 100으로 나머지 연산
        '''
        sum=0
        for c in key:
            sum=sum+ord(c)

        return sum%100

    def BinarySearch(self, key):
        '''
        이름 : BinarySearch()
        목적 : 입력받은 key 값을 hashFn()을 이용해 변환한 뒤, 동일한 인덱스를 찾아 반환 
        '''
        low= 0
        high=self.size()-1
        i=self.hashFn(key)
        while (low<=high):
            middle = (low+high)//2
            a=self.table[middle].key
            if i == self.hashFn(a):
                return self.table[middle]

            elif (i>self.hashFn(a)):
                low=middle+1

            else : high = middle-1
        return None

    def delete(self,key):
        for i in range (self.size()):
            if self.hashFn(key)==self.hashFn(self.table[i].key):
                self.table.pop(i)
                return 
map=BinaryMap()
map.insert('data','자료')
map.insert('sturcture','구조')
map.insert('Binary search','이진탐색')
map.insert('gamer','게이머')
map.insert('arrary','정렬')
map.display('나만의 단어장 : ')

print('탐색 :gamer -->', map.BinarySearch('gamer'))
print('탐색: arrary -->', map.BinarySearch("arrary"))
print("탐색: sturcture-->", map.BinarySearch('sturcture'))

map.delete("arrary")
map.display("나만의 단어장:")


