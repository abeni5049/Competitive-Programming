class Solution:
    def knightDialer(self, n: int) -> int:
        graph = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[4,2]]
        memo = {}
        def dfs(i,n):
            if n == 0: return 1
            if (i,n) in memo: return memo[(i,n)]
            count = 0
            for cell in graph[i]:
                count += dfs(cell,n-1)
            memo[(i,n)] = count
            return count
        count = 0
        for i in range(10):
            count += dfs(i,n-1)
        return count % (10**9+7)
