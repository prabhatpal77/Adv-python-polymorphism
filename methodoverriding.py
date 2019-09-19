# Method overriding:- The concept of deffining muliplt methods with the same name with the same number of parameters
# one method is in superclass and another is in subclass is known as a method overriding.
class X:
    def m1(self):
        print("in m1 of x")
    def m2(self):
        print("in m2 of x")
class Y(X):
    def m2(self):
        print("in m2 of y")
    def m3(self):
        print("in m3 of y")
y1=Y()
y1.m1()
y1.m2()
y1.m3()
x1=X()
x1.m1()
x1.m2()
