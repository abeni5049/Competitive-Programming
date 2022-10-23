class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dfs(i,state):
            if i == len(prices): return 0
            if state == 0:
                buy = dfs(i+1,1)-prices[i]
                dont_buy = dfs(i+1,state)
                return max(buy,dont_buy)
            else:
                sell = dfs(i+1,0)+prices[i]-fee
                dont_sell = dfs(i+1,state)
                return max(sell,dont_sell)
        return dfs(0,0)
