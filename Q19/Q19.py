def linear_search(element, lst):
    for i in range(len(lst)):
        if lst[i] == element:
            return True
    return False

def binary_search(element, lst):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == element:
            return True
        elif lst[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

    return False

element = 7
lst = [2, 4, 6, 8, 10]
linear_result = linear_search(element, lst)
binary_result = binary_search(element, lst)
print(f"Is {element} present in the list? (Linear Search): {linear_result}")
print(f"Is {element} present in the list? (Binary Search): {binary_result}")
