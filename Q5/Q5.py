def reverse(l):
    for i in range(int(len(l)/2)):
        arr[i], arr[len(l) - 1 - i] = arr[len(l) - 1 - i], arr[i]
    return arr
 
arr = [1, 2, 3, 4, 5]
print(reverse(arr))