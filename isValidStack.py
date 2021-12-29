class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack  = [] 
        for i in s:
            if len(stack) == 0 and (i == ')' or i == '}' or i == "]"):
                return False
            if i == '(' or i == '{' or i == "[":
                stack.append(i) 
                continue 
            last = stack.pop()
            if i != ')' and last == '(':
                return False
            if i != '}' and last == '{':
                return False
            if i != ']' and last == '[':
                return False
        if len(stack) == 0:
            return True
        return False
        