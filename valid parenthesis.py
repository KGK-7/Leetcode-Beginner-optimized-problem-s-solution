def is_valid_brackets(s):
    stack = []
    
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        elif ch == ')':
            if not stack or stack[-1] != '(':
                return False
            stack.pop()
        elif ch == ']':
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
        elif ch == '}':
            if not stack or stack[-1] != '{':
                return False
            stack.pop()

    return len(stack) == 0

# Test cases
print(is_valid_brackets("()"))  # True
print(is_valid_brackets("()[]{}"))  # True
print(is_valid_brackets("(]"))  # False
print(is_valid_brackets("([)]"))  # False
print(is_valid_brackets("{[]}"))  # True