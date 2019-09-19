# Even though we override super class properties within the subclass we can access the super class properties
# within the subclass by using super() statement.
# An example of super()
class X:
    def m1(self):
        print("in m1 of x")
    def m2(self):
        print("in m2 of x")
class Y(X):
    def m1(self):
        print("in m of y")
    def m3(self):
        print("in m3 of y")
    def display(self):
        self.m1()
        self.m2()
        self.m3()
        super().m1()
y1=Y()
y1.display()
