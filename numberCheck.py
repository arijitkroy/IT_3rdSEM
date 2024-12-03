def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False     