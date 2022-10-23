class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i,state):
            if i == len(prices): return 0
            if state == 0:
                buy = dfs(i+1,1)-prices[i]
                dont_buy = dfs(i+1,state)
                return max(buy,dont_buy)
            elif state == 1:
                sell = dfs(i+1,2)+prices[i]
                dont_sell = dfs(i+1,state)
                return max(sell,dont_sell)
            else:
                cooldown = dfs(i+1,0)
                dont_cooldown = dfs(i+1,state)
                return max(cooldown,dont_cooldown)
        return dfs(0,0)
