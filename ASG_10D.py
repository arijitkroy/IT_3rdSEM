class F:
    def __init__(self, s):
        self.string = s
    def __sub__(self, other):
        s = ""
        for i in self.string:
            if i not in other.string:
                s += i
        return s
        
s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")
x = F(s1)
y = F(s2)
print(f"{s1} - {s2} = {x - y}")