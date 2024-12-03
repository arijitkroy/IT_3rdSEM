leap = lambda y : y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)
leap_years = list(filter(leap, range(2024, 3031)))
print(leap_years)