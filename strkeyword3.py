# __init__ magic method with __str__ magic method.
class X:
    def __init__(self, msg):
        self.msg=msg
    def display(self):
        print("welcome")
    def __str__(self):
        return self.msg
x1=X("prabhat pal")
print(x1)
x1.display()
x2=X("python")
print(x2)
x2.display()
x3=X("django")
print(x3)
x3.display()
