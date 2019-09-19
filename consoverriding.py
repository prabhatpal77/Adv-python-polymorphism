# Constructor overriding:- The concept of defining multiple constructor with the same number of parameters
# or defferent number of parameters one is in super class and another sne is subclass is known as a constructor
# overriding.
class X:
    def __init__(self):
        print("in constructor of x")
    def m1(self):
        print("in m1 of x")
class Y(X):
    def __init__(self):
        super().__init__()
        print("in constructor of y")
    def m2(self):
        print("in m2 of y")
y1=Y()
y1.m1()
y1.m2()
