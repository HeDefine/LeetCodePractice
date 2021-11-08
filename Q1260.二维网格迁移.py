# 给你一个 m 行 n 列的二维网格 grid 和一个整数 k。你需要将 grid 迁移 k 次。
# 每次「迁移」操作将会引发下述活动：

# 位于 grid[i][j] 的元素将会移动到 grid[i][j + 1]。
# 位于 grid[i][n - 1] 的元素将会移动到 grid[i + 1][0]。
# 位于 grid[m - 1][n - 1] 的元素将会移动到 grid[0][0]。
# 请你返回 k 次迁移操作后最终得到的 二维网格。

class Solution:
    def shiftGrid(self, grid: list, k: int) -> list:
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)
        res = [[0]*n for i in range(m)]
        for x in range(0, m):
            for y in range(0, n):
                val = grid[x][y]
                temp = (x * n + y + k) % (m * n)
                newRow = temp // n 
                newCol = temp % n
                res[newRow][newCol] = val
        return res
# print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))    # [[9,1,2],[3,4,5],[6,7,8]]
# print(Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))    # [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
# print(Solution().shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))    #[[1,2,3],[4,5,6],[7,8,9]]
print(Solution().shiftGrid(grid = [[1],[2],[3],[4],[7],[6],[5]], k=23))