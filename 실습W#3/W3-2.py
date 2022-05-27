

class ArrayList:
    def __init__(self): #생성자 
        self.items = []  #클래스 변수 선언 및 초기화
    def insert(self,pos,elem): 
        self.items.insert(pos,elem)
    def delete(self,pos):
        return self.items.pop(pos)
    def isEmpty(self):
        return self.size()
    def getEntry(self,pos):
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):            #메소드 정의
        self.items=[]
    def find(self,item):
        return self.items.index(item)
    def replace(self,pos,elem):
        self.items[pos]=elem
    def sort(self):
        self.items.sort()
    def marge(self,lst):
        self.items.extend(lst)
    def display(self, msg='ArrayList: '):
        print(msg, self.size(), self.items) 






def myLineEditor():  #라인 편집기 주 함수
    list = ArrayList()  #ArrayList의 객체인 list 생성 
    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f=찾기, q-종료 => ")
        if command == 'i':      #삽입연산
            pos = int(input(" 입력행 번호: "))      #삽입할 행번호 입력
            str = input(" 입력한 내용: ")        #삽입할 행내용 입력
            list.insert(pos, str)           #insert 메소드로 삽입
        elif command == 'd':                #행삭제
            pos = int(input(" 삭제행 번호: "))  #삭제할 행번호 입력
            list.delete(pos)                    #delete 메소드로 삭제
        elif command == 'r':                #행 내용 변경 메소드
            pos = int( input (" 변경행 번호: "))    #변경할 행 번호 입력
            str = input(" 변경행 내용: ")       #변경할 행 내용 입력
            list.replace(pos, str)              #replace 로 변경
        elif command == 'q' : return        #프로그램 종료
        elif command == 'p' :               #문서 출력  
            print('Line Editor')
            for line in range(list.size()): #모든 라인에 대해 for문
                print('[%2d]' %line, end='') #라인 번호 출력
                print(list. getEntry(line)) # 행내용 출력
            print()                         #한줄 띄움
        elif command == 'l':             #파일 입력 메소드
            filename = input("경로를 입력하시오") #원하는 파일의 경로를 입력/ 주의사항; 경로에서 역슬레쉬 대신 슬래쉬 사용
            infile = open(filename , "r" ,encoding='utf-8') #읽기전용, 유니코드인코딩
            lines = infile.readlines()      #파일의 모든 내용 읽음
            for line in lines:          #읽은 각행에 데헤
                list.insert(list.size(), line.rstrip('\n')) 
            infile.close()                      #파일 닫기
        elif command == 's':                            #파일 저장 메소드
            filename = input("경로를 입력하시오")   #원하는 파일의 경로를 입력
            outfile = open(filename , "w" ,encoding='utf-8') #파일 열기 쓰기모드
            for i in range(list.size()):
                outfile.write(list.getEntry(i)+'\n')
            outfile.close()                             #파일 닫기
        elif command == 'f':                    #문자열 찾기 메소드
            filename = input("경로를 입력하시오")
            f = open(filename , "r" ,encoding='utf-8')
            a=input("찾고자하는 문자열을 입력하세요")
            lines = f.readlines()   #파일의 모든 내용을 읽은뒤 각 라인마다 입력한 문자열이 있는지 확인/ 출력
            for line in lines:
                if a in line : print(line)


myLineEditor() #라인편집기 함수 호출
