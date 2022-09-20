# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
# 一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），
# 也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
# 但它不能进入方格 [35, 38]，因为3+5+3+8=19。
# 请问该机器人能够到达多少个格子？
#  
# 示例 1：
# 输入：m = 2, n = 3, k = 1
# 输出：3
#  
# 示例 2：
# 输入：m = 3, n = 1, k = 0
# 输出：1
#  
# 提示：
# 1 <= n,m <= 100
# 0 <= k <= 20

class Solution:
    def movingCount(self, m: int, n: int, k: int):
        def recursion(i, j):
            if i % 10 + i // 100 + i // 10 % 10 + j % 10 + j // 100 + j // 10 % 10 > k:
                return 0
            visited[i][j] = 1
            res = 1
            walk_list = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for walk in walk_list:
                if 0 <= i + walk[0] < m and 0 <= j + walk[1] < n and visited[i + walk[0]][j + walk[1]] == 0:
                    res += recursion(i + walk[0], j + walk[1])
            return res
        visited = [[0] * n for i in range(m)]
        return recursion(0, 0)

print(Solution().movingCount(2,3,1))    # 3
print(Solution().movingCount(3,1,0))