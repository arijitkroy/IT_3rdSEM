bs = float(input("Enter basic pay: "))
agp = 0.5 * bs
mb = bs + agp
da = 0.5 * mb
hra = 0.15 * mb
sal = mb + da + hra
print(f"Total salary: {sal:0.2f}")