s = input("Enter string: ").split()
d = dict()
for i in s:
    d[i] = s.count(i)
print(d)