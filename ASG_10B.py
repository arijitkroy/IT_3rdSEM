class B:
    def __init__(self, n):
        self.val1 = n
        print("Class B object created")
    def show(self):
        print("Showing Class B object having value ", self.val1)

n = int(input("Enter number: "))
b = B(n)
b.show()