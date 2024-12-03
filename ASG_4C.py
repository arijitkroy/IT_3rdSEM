print("Two digits automorphic numbers:")
for i in range(10, 100):
    if i**2 % 100 == i:
        print(i)