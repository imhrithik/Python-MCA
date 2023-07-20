def comulative_product(l):
    arr = [l[0]]
    for i in range(1, len(l)):
        arr.append(arr[i-1] * l[i])
    return sum(arr)
 
print(comulative_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))