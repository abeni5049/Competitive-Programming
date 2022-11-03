class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.dfs(1,set(days),days[-1],costs,{})
    
    def dfs(self,current_day,days,lastDay,costs,memo):
        if current_day > lastDay: return 0
        if current_day in memo: return memo[current_day]
        if current_day not in days: return self.dfs(current_day+1,days,lastDay,costs,memo)
        minimum_cost = float('inf')
        passes = [1,7,30]
        for i in range(3):
            minimum_cost = min(minimum_cost,self.dfs(current_day+passes[i],days,lastDay,costs,memo) + costs[i])
        memo[current_day] = minimum_cost
        return minimum_cost
