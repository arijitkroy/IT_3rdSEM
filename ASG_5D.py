s = input("Enter string: ")
indices = input("Enter indices: ")
start = int(indices.split()[0]) - 1
end = int(indices.split()[1])
sub = s[start:end]
print(f"Substring: {sub}")
if sub == sub[::-1]:
    print('Type: Palindrome')
else:
    print('Type: Not Palindrome')