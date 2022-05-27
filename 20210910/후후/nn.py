class Fourcal:
    def setdata(self,first,second):
        self.first=first    
        self.second=second
    def add(self):
        result = self.first + self.second
        return result
    
a=Fourcal()
b=Fourcal()
a.setdata(4,2)
b.setdata(3,7)
print(a.add())
#print(a.mul())
#print(a.div())
#print(a.sub())