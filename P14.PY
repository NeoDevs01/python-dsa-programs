def bracketmatching(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(' and char != ")":
                return False
            if current_char == '{' and char != "}":
                return False
            if current_char == '[' and char != "]":
                return False
    return not stack

expr = "{()[]}"
if bracketmatching(expr):
    print("Matching")
else:
    print("Not Matching")
# End of P14.PY