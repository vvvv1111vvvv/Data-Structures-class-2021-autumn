class Polinominal:
    def __init__(self):
        self.equa=[]

    def read_poly(self):
        n=int(input("다항식의 최고 차수를 입력하세요"))
        print(n)
        for i in range(n,-1,-1):
            print("x^%d의 계수 : "%(i))
            x=int(input())
            self.equa.append(x)
        print(self.equa)
    def insert(self,pos,elem):self.insert(pos,elem)
    def degree(self):
        return len(self.equa)-1 
    
    def evaluate(self,scalar):
        s=0
        for i in range(len(self.equa)-1,-1,-1):
            s+=self.equa[len(self.equa)-1-i]*scalar**i
        return s
    def add(self,rhs):
        c=Polinominal()
        if len(self.equa)>= len(rhs.equa):
            for i in range (-1,-len(rhs.equa)-1):
                c.equa.insert(0,self.equa[i]+rhs.equa[i])
                print(c.equa)
            for i in range (-len(rhs.equa)-1,-len(self.equa)-1):
                c.equa.insert(0,self.equa[i])
            return c
#        else:
#            for i in range (-1,-len(self.equa)-1):
#                c.equa[i]=self.equa[i]+rhs.equa[i]
#            for i in range (-len(self.equa)-1,-len(rhs.equa)-1):
#                c.equa[i]=rhs.equa[i]

    def display(self):
        for i in range(len(self.equa),-1):
            print(a.equa[i],"x^%d"%(i))

a=Polinominal()
b=Polinominal()

a.read_poly()
print("coef of a : ",a.equa)
b.read_poly()
print("coef of b : ",b.equa)
a.evaluate(4)
a.display("A(X) = ")

print(a.evaluate(4))

print(a.add(b).equa)