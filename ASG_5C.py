s = input()
u = l = 0
for i in s:
    if i.isupper():
        u += 1
    if i.islower():
        l += 1
print(f"UpperCase: {u}\nLowerCase: {l}")