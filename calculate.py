class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        op = '+'
        num = 0
        
        for index,i in enumerate(s):
            if i.isdigit():
                num = (num * 10) + int(i)
            if (not i.isdigit() and not i.isspace() ) or index == len(s) -1:
                if op == '*':
                    stack.append(stack.pop()*num)  
                elif op == '/':
                    temp = stack.pop()
                    if temp < 0 and temp % num != 0:
                        stack.append(temp//num+1)
                    else:
                        stack.append(temp//num)
                elif op == '-':
                    stack.append(-num)
                elif op == '+':
                    stack.append(num) 
                op = i
                num = 0
        res = 0
        while stack:
            res += stack.pop()
            
        return res
            
