# Another e.g. of constructor overriding.
class X:
    def __init__(self):
        self.a=1000
        self.b=2000
    def m1(self):
        print("in m1 of X")
class Y(X):
    def __init__(self):
        self.c=3000
        self.d=4000
        super().__init__()
    def m2(self):
        print("in m2 of y")
y1=Y()
y1.m1()
y1.m2()
print(y1.d)
print(y1.c)
print(y1.b)
print(y1.a)
