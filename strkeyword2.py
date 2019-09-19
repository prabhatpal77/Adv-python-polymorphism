# __str__ as a method.
class X:
    def display(self):
        print("welcome")
    def __str__(self):
        return "prabhat pal"
x1=X()
print(x1)
x1.display()
x2=X()
print(x2)
x2.display()
