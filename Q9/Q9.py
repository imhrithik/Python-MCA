def remove_spaces(s):
    if s == '':
        return ''
    elif s[0] == ' ':
        return remove_spaces(s[1:])
    else:
        return s[0] + remove_spaces(s[1:])

str = input("Enter a string :")
print(remove_spaces(str))