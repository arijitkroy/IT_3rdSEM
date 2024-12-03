year = int(input("Enter year: "))
if year > 999 and year < 10000:
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print("Invalid year provided")