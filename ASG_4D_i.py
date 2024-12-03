n = int(input("Number of Lines: "))
for i in range(1, n+1):
    print(" "*(n-i), end='')
    for j in range(i-1, -1, -1):
        print(chr(65+j%26), end='')
    print()