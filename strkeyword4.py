# __str__ and __init__ in a symple application with list. A sorting example of customers.
class Cust:
    cbname="sbi"
    def __init__(self, cname, cadd, cacno, cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
    def __str__(self):
        return self.cname+" "+self.cadd+" "+str(self.cacno)+" "+str(self.cbal)+" "+Cust.cbname
    def deposit(self, wamt):
        self.cbal=self.cbal-wamt
    def display(self):
        print(self.cname)
        print(self.cadd)
        print(self.cacno)
        print(self.cbal)
        print(self.cbname)
c1=Cust("ravana","columbo",1010,100000.00)
c2=Cust("ram","ayodhya",1020,1000.00)
c3=Cust("raju","mumbai",1030,300.00)
lst=[c1, c2, c3]
for p in lst:
    print(p)
lst.sort(key=lambda c:c.cname)
print("after sorting")
for q in lst:
    print(q)
