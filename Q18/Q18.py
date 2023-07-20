def check_balanced_parentheses(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']

    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False

    return len(stack) == 0

string = '({[()]})'
balanced = check_balanced_parentheses(string)
print(f"Is the string '{string}' balanced? {balanced}")
