def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fibo(n-1) + fibo(n-2))

x = int(input("Enter a number : "))
print([fibo(i) for i in range(0, x+1)])