# Use of __str__ keyword in python..
class X:
    def display(self):
        print("welcome")
x1=X()
print(x1)
p=x1.__str__()
print(p)
x1.display()
