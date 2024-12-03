n = int(input("Number of Lines: "))
for i in range(1, 2*n):
    if i < n:
        print("*"*i)
    if i == n:
        print("*"*(2*n-1))
    if i > n:
        print(" "*(i-1) + "*"*(2*n-i))