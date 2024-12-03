import numberCheck as nc

if __name__ == "__main__":
    num = int(input("Enter integer number: "))
    print(f"Prime: {nc.is_prime(num)}\nPalindrome: {nc.is_palindrome(num)}")