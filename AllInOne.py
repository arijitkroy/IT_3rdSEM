from math import pi
import numpy as np
import numberCheck as nc
import os

def Asg1A():
    print("MCKVIE", end=" ")
    print("Computer Science & engineering")

def Asg1B():
    r = float(input("Enter radius: "))
    area = pi * r ** 2
    perimeter = 2 * pi * r
    print(f"Area = {area:0.3f}\nPerimeter = {perimeter:0.3f}")

def Asg2A():
    a = input("Variable a = ")
    b = input("Variable b = ")
    a, b = b, a
    print(f"Swap without third variable:\na = {a}\nb = {b}")
    c = a
    a = b
    b = c
    print(f"Swap with third variable:\na = {a}\nb = {b}")

def Asg2B():
    basic_pay = float(input("Enter basic pay: "))
    agp = 0.5 * basic_pay
    merged_basic = agp + basic_pay
    da = 0.5 * merged_basic
    hra = 0.15 * merged_basic
    total_salary = da + hra + merged_basic
    print("Total salary: ", total_salary)

def Asg3A():
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    c = int(input("Enter 3rd number: "))
    max_num = a if a > b and a > c else b if b > c else c
    print("Maximum = ", max_num)

def Asg3B():
    y = int(input("Enter year: "))
    if 999 < y < 10000:
        print(f"{y} is Leap year") if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0) else print(f"{y} is not Leap Year")
    else:
        print("Invalid year provided")

def Asg3C():
    a = int(input("Enter coefficient A: "))
    b = int(input("Enter coefficient B: "))
    c = int(input("Enter coefficient C: "))
    if a != 0:
        d = (b**2 - 4*a*c)**0.5
        if d == 0:
            print(f"Roots are real and equal: {(-b/a):0.3f}")
        elif d > 0:
            r1 = (-b + d)/a
            r2 = (-b - d)/a
            print(f"Roots are real and distinct: {r1:0.3f} and {r2:0.3f}")
        else:
            r1 = (-b + d)/a
            r2 = (-b - d)/a
            print(f"Roots are imaginary: {r1:.3f} and {r2:.3f}")
    else:
        print("Equation is not quadratic")

def Asg3D():
    c = input("Enter character: ")
    match c.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            print("Vowel")
        case _ if len(c) == 1 and c.isalpha():
            print("Consonant")
        case _:
            print("Invalid input")

def Asg4A():
    n = int(input("Enter limit: "))
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

def Asg4B():
    n = input("Enter range: ")
    start = int(n.split()[0])
    end = int(n.split()[1])
    for i in range(start, end):
        if i >= 2:
            for j in range(2, int(i**0.5) + 1):
                if j % i == 0:
                    break
            else:
                print(i, end=" ")

def Asg4C():
    n = int(input("n digit automorphic number: "))
    for i in range(10**(n-1), 10**n):
        if (i**2) % (10**n) == i:
            print(i, end=" ")

def Asg4D_1():
    n = int(input("Number of lines: "))
    for i in range(1, n + 1):
        print(" " * (n - 1), end=" ")
        for j in range(i-1, -1, -1):
            print(chr(65 + j % 26), end=" ")
        print()

def Asg4D_2():
    n = int(input("Number of lines: "))
    for i in range(1, 2*n):
        if i < n:
            print("*" * i)
        if i == n:
            print("*" * (2*n-1))
        if i > n:
            print(" " * (i-1) + "*" * (2*n-i))

def Asg5A():
    s = input("Enter statement: ")
    swapped_s = s.swapcase()
    print(swapped_s)

def Asg5B():
    email = input("Enter Email ID: ")
    roll = email.split("@")[0]
    institute = email.split("@")[1].split(".")[0]
    print(f"Roll: {roll}\nInstitute: {institute}")

def Asg5C():
    s = input("Enter statement: ")
    l = u = 0
    for i in s:
        if i.isupper():
            u += 1
        if i.islower():
            l += 1
    print(f"UpperCase: {u}\nLowerCase: {l}")

def Asg5D():
    s = input("Enter statement: ")
    index_range = input("Enter starting and ending index: ")
    start = index_range.split()[0]
    end = index_range.split()[1]
    sub_s = s[start:end]
    print("Sub_String: ", sub_s)
    if sub_s == sub_s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

def Asg6A():
    s = input("Enter numbers: ")
    l = [int(x) for x in s.split()]
    second_max = sorted(l)[-2]
    second_min = sorted(l)[1]
    print(f"Second Maximum = {second_max}\nSecond Minimum = {second_min}")

def Asg6B():
    l = eval(input("Enter list of numbers: "))
    out_l = [0] * (max(l) + 1)
    for i in l:
        out_l[i] = i
    print(out_l)

def Asg6C():
    s1 = print("Enter 1st statement: ")
    s2 = print("Enter 2nd statement: ")
    print("Unique common words: ", set(s1).intersection(set(s2)))
    print("All unique words: ", set(s1).union(set(s2)))
    print("All unique words present in 1st statement but not in 2nd: ", set(s1) - set(s2))

def Asg6D():
    s = input("Enter statement: ")
    d = dict()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)

def Asg6E():
    l = eval(input("Enter list of names: "))
    if type(l) != list:
        print("Input is not a list")
    else:
        l.sort(key = lambda x: x[-1])
        print(l)

def Asg7A():
    def fibo_n(n = 1):
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n > 2:
            return fibo_n(n-1) + fibo_n(n-2)
    n = input("Enter term: ")
    print("N-th term of fibonacci: ", fibo_n(n))

def Asg7B():
    def fibo_s(a=0, b=1, n = 1):
        if n > 0:
            print(a, end=" ")
            fibo_s(b, a+b, n-1)
    n = input("Enter limit: ")
    print("Fibonacci Series: ", fibo_s(0, 1, n))

def Asg7C():
    def is_prime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    l = list(filter(is_prime, range(5500, 251, -1)))
    print(l)

def Asg7D():
    year = lambda y: (y % 100 != 0 and y % 4 == 0) or (y % 400 == 0)
    leap_years = list(filter(year, range(2024, 3011)))
    print(leap_years)

def Asg8A():
    i = int(input("Enter number: "))
    print(f"Palindrome: {nc.is_palindrome(i)}\nPrime: {nc.is_prime(i)}")

def Asg8B():
    m = int(input("Enter rows: "))
    n = int(input("Enter columns: "))
    val = eval(input("Enter value of matrix A in 2D Array: "))
    mat_a = np.matrix(val)
    mat_b = np.random.randint(1, 20, size=(n, m))
    mat_c = np.matmul(mat_a, mat_b)
    print(mat_c)

def Asg9A():
    class myException(Exception):
        pass
    def well_brackated(exp):
        try:
            if type(exp) != str:
                raise myException
            stack = []
            for i in exp:
                if i in ['(', '{', '[']:
                    stack.append(i)
                if i in [')', '}', ']']:
                    c = stack.pop()
                    if c == i:
                        check = True
                    else:
                        check = False
                        break            
                            
        except myException as e:
            print("Not a string")
            check = False
        except IndexError as i:
            print("List is empty")
            check = False
        finally:
            print("Done!")
            return check
    exp = input("Enter expression: ")
    print("Expression is balanced") if well_brackated(exp) == True else print("Expression is unbalanced")

def Asg9B():
    class myException(Exception):
        pass
    def rotate_list(l, n=0):
        try:
            if len(l) == 0:
                raise IndexError
            if n > len(l):
                raise myException
            if n < 0:
                out = l[abs(n):] + l[:abs(n)]
            if n > 0:
                out = l[-n:] + l[n:]
        except IndexError as i:
            print("List is empty!")
        except myException as e:
            print("Number of rotation is greater than number of elements in list")
            out = l
        finally:
            return out
    l = eval(input("Enter list of numbers: "))
    n = int(input("Number of rotations: "))
    print(rotate_list(l, n))

def Asg10():
    class A:
        def __init__(self):
            print("Class A object created")
        def show(self):
            print("Showing Class A")
        def __del__(self):
            print("Object deleted!!!")
    class B:
        def __init__(self, n):
            self.val1 = n
            print("Class B object created")
        def show(self):
            print("Showing Class B object having value ", self.val1)
    class C(B):
        def __init__(self, n1, n2):
            super().__init__(n1)
            self.val2 = n2
            print("Class C object created")
        def show(self):
            print(f"Showing Class C object with {self.val1}, {self.val2}")
    class F:
        def __init__(self, s):
            self.string = s
        def __sub__(self, other):
            res = ""
            for i in self.string:
                if i not in other.string:
                    res += i
            return res
        
    a = A()
    print(a)
    a.show()

    b = B(10)
    print(b)
    b.show()

    c = C(20, 30)
    print(c)
    c.show()

    f1 = F("Hello World")
    f2 = F("Hey There")
    print(f1 - f2)

def Asg11A():
    f = open("TextFile1.txt", "w")
    f.write("Welcome to Python")
    f.close()

def Asg11B():
    n = int(input("Enter limit: "))
    i = 2
    f = open("TextFile2.txt", "a")
    while n:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            f.write(f"{i} ")
            n -= 1
        i += 1
    f.close()

def Asg11C():
    a = 0
    b = 1
    n = int(input("Enter limit: "))
    f = open("TextFile3.txt", "a")
    while a < n:
        f.write(f"{a} ")
        a, b = b, a + b
    f.close()

def Asg11D():
    f = open("TextFile4.txt", "r")
    f.read()
    f.close()

def Asg11E():
    f = open("TextFile5.txt", "r")
    f.read()
    size = os.path.getsize("TextFile5.txt")
    print(f"Size of file: {f.tell()}\nSize of file (with os module): {size}")

if __name__ == "__main__":
    # Execute any assignment here by calling respective functions
    Asg1A()
