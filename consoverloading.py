# Constructor overloading:- The concept of defining multiple constructor with the same number parameters are different number of parameters
# within a class is known as aa constructor overloading.
class X:
    def __init__(self):
        print("in no parameter constructor of x")
    def __init__(self, a, b):
        print("in two parameter constructor of x")
    def __init__(self, a):
        print("in one parameter constructor of x")
x1=X(1000)
x2=X()
