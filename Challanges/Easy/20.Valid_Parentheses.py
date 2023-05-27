"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

##########################################################
def isValid1(s):
    stack =  []
    CloseToOpen = {")" : "(", "]" : "[", "}" : "{"}

    for c in s:
        if c in CloseToOpen:
            if stack and stack[-1] == CloseToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False  

#########################################################
def isValid2(s):
    stack =  []
    Close = {")", "]","}"}

    for c in s:
        if c in Close:
            if stack and stack[-1] == "(" and c == ")":
                stack.pop()
            elif stack and stack[-1] == "[" and c == "]":
                stack.pop()
            elif stack and stack[-1] == "{" and c == "}":
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False  

###############################################################
def isValid3(s: str) -> bool:
        stack = []
        for char in s:
            if char == "{" or char == "(" or char == "[":
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == "}" and stack[-1] == "{":
                    stack.pop(-1)
                elif char == ")" and stack[-1] == "(":
                    stack.pop(-1)
                elif char == "]" and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
        return not stack

###############################################################
res = isValid1("(]")
print(res)
