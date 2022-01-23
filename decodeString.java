class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                l = ''
                while stack and stack[-1] != '[':  
                    l = stack.pop() + l
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(l * int(num))
        return ''.join(stack)
