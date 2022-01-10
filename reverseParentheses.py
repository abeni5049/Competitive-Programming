class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ""
        for ch in s:
            if ch == '(':
                stack.append(res)
                res = ''
            elif ch == ')':
                res = stack.pop() + res[::-1]
            else:
                res += ch
        return res
