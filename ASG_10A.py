class A:
    def __init__(self):
        print("Class A object created")
    def show(self):
        print("Showing Class A")
    def __del__(self):
        print("Object deleted!!!")

a = A()
print(a)
a.show()