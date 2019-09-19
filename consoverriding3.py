# Another example of constructor overriding with many numbers of parameters.
class X:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def m1(self):
        print("in m1 of x")
class Y(X):
    def __init__(self, a, b, c, d):
        self.c=c
        self.d=d
        super().__init__(a, b)
    def m2(self):
        print("in m2 of y")
y1=Y(1000, 2000, 3000, 4000)
y1.m1()
y1.m2()
print(y1.d)
print(y1.c)
print(y1.b)
print(y1.a)
