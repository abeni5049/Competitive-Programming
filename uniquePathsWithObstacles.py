class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    obstacleGrid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
                elif obstacleGrid[i][j] == 0:
                    if i-1 >= 0:
                        obstacleGrid[i][j] += obstacleGrid[i-1][j]
                    if j-1 >= 0:
                        obstacleGrid[i][j] += obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        print(obstacleGrid)
        return obstacleGrid[-1][-1]
