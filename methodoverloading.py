# Method Overloading:- The concept of deffining multiple methods with the same name with the same number of parameters ordifferent number
# of classis known as method overloading.
class X:
    def m1(self):
        print("in no parameter m1 of x")
    def m1(self, a):
        print("in one parameter m1 of x")
    def m1(self, a, b):
        print("in two parameter m1 of x")
x1=X()
x1.m1(1000, 2000)
