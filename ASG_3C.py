a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
if a != 0:
    d = b**2 - 4*a*c
    if d == 0:
        root = (-b)/(2*a)
        print(f"Equation has real and equal roots: {root:0.3f}")
    elif d > 0:
        root1 = ((-b)+(d**0.5))/(2*a)
        root2 = ((-b)-(d**0.5))/(2*a)
        print(f"Equation has real and distinct roots: {root1:0.3f} and {root2:0.3f}")
    else:
        root1 = ((-b)+(d**0.5))/(2*a)
        root2 = ((-b)-(d**0.5))/(2*a)
        print(f"Equation has imaginary roots: {root1:.3f} and {root2:.3f}")
else:
    print("Equation is not quadratic")