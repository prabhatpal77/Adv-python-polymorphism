# Whenever we define with same name with the same number of parameters or different number of parameters
# within a class then bydefault python interpretor recohnizes last defined method.
class X:
    def m1(self):
        print("in no parameter m1 of x")
    def m1(self, a, b):
        print("in two parameter m1 od x")
    def m1(self, a):
        print("in one parameter m1 of x")
x1=X()
x1.m1(1000)
x1.m1(100, 200)
