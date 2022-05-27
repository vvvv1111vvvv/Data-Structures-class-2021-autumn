class Bag:
    def __init__(self):
        self.bag=[]
    def insert(self,stuff):
        self.bag.append(stuff)
    def remove(self,stuff):
        self.bag.remove(stuff)
myBag=Bag()
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print("내 가방속의 물건:", myBag.bag)
myBag.remove('빗')
print("내 가방속의 물건:", myBag.bag)
