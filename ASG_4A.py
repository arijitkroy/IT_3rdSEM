n = int(input("Number of terms: "))
a = 0
b = 1
for i in range(0, n):
    print(a, end=' ')
    a, b = b, a + b