class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i,state,count):
            if i == len(prices) or count == 2: return 0
            if state == 0:
                buy = dfs(i+1,1,count)-prices[i]
                dont_buy = dfs(i+1,state,count)
                return max(buy,dont_buy)
            else:
                sell = dfs(i+1,0,count+1)+prices[i]
                dont_sell = dfs(i+1,state,count)
                return max(sell,dont_sell)
        return dfs(0,0,0)
