start = int(input("Starting point: "))
end = int(input("Ending point: "))
for i in range(start, end):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                print(i)