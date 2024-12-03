def fibo_n(n=1):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fibo_n(n-1) + fibo_n(n-2)
    
if __name__ == "__main__":
    n = int(input("N-th Term: "))
    print(fibo_n(n))