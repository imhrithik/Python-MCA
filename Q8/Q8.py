string = input("Enter a string: ")
char_count = {}

for i in string:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1

print("character count:", char_count)