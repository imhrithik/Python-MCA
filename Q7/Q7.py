tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mid = len(tup) // 2
first_half = tup[:mid]
last_half = tup[mid:]

print("First half:", end=" ")
for i in first_half:
    print(i, end=" ")
print()

print("Last half:", end=" ")
for i in last_half:
    print(i, end=" ")
print()