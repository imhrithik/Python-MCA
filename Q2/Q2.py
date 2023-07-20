a, b = 0, 1
fib_seq = [a]
fib_sum = 0

while b <= 1000:
    if b % 2 == 0:
        fib_sum += b
        fib_seq.append(b)
    a, b = b, a+b

print(f"The even-valued terms in the Fibonacci sequence up to 1000 are {fib_seq}")
print(f"The sum of the even-valued terms in the Fibonacci sequence up to 1000 is {fib_sum}")