class polynominal:
    def __init__(self):
        self.p=[]
    def degree(self):
        return int(input("다항식의 최고 차수를 입력하시오 : "))

    def polynomial(self):
        n=self.degree()
        self.coef=[n+1]
        for i in range(n,-1):
            self.coef[i]=input(("X^%d 의 계수 : ", i))

    #def evaluate
    def display(self):
        print(self.upper(),"(X) = ",end='')
        for i in range (len(self.p),-1):
            print("%f X^%d",self.p[i],i)
            
a=polynominal()
b=polynominal()

a.polynominal()
b.polynominal()
a.display
b.display
#c.display

c=a.add(b)
