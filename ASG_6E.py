ls = eval(input("Enter list of strings: "))
ls.sort(key=lambda x : x[-1])
print(ls)