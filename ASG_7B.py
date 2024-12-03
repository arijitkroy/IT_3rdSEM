def fibo_s(a = 0, b = 1, n=1):
    if n > 0:
        print(a)
        fibo_s(b, a+b, n-1)
    
if __name__ == "__main__":
    n = int(input("Number of terms: "))
    fibo_s(n=n)