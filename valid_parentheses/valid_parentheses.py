
def isValid(s):
    stack = []
    for x in s:
        if x in "[{(":
            stack.append(x)
        elif stack:
            if(x == "]" and stack[-1] == "[") or (x == "}" and stack[-1] == "{") or (x == ")" and stack[-1] == "("):
                stack.pop()
            else:
                return False
        else:
            return False
    return True if stack==[] else False
