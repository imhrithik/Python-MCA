def series_sum(x, n):
    sum = 0
    sign = 1
    fact = 1
    for i in range(n):
        term = sign * (x**(2*i) / fact)
        sum += term
        sign *= -1
        fact *= (2*i+1) * (2*i+2)
    return sum

print(series_sum(5,10))