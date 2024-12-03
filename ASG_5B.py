e = input("Enter email: ")
if '@' in e:
    roll = e.split('@')[0]
    institute = e.split('@')[1].split('.')[0].upper()
    print(f"Roll No - {roll}\nInstitute - {institute}")
else:
    print('Invalid email')