a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
print(f"Maximum is {a if a > b and a > c else b if b > c else c}")