class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i != '+' and i != '-' and i != '*' and i != '/':
                stack.append(i)
                continue
            elif i == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2) + int(num1)
                stack.append(result)
            elif i == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2) - int(num1)
                stack.append(result)
            elif i == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2) * int(num1)
                stack.append(result)
            elif i == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                result = int(num2) // int(num1)
                if int(num2) // int(num1) >= 0:
                    stack.append(result) 
                elif int(num2)%int(num1) == 0:
                    stack.append(result)
                else:
                    stack.append(result+1)
        return stack.pop()
