L = eval(input("Enter list: "))
new_L = [0] * (max(L)+1)
for i in L:
    new_L[i] = i
print("New List:", new_L)