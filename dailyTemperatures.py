class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i,num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        
        return answer
        
