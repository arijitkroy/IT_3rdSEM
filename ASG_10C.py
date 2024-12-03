class B:
    def __init__(self, n1):
        self.val1 = n1

class C(B):
    def __init__(self, n1, n2):
        super().__init__(n1)
        self.val2 = n2
        print("Class C object created")
    def show(self):
        print(f"Showing Class C with {self.val1}, {self.val2}")

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = C(a, b)
c.show()