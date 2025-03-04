def is_balanced(expression: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack
