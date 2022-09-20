# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#  
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 限制：
# 0 <= matrix.length <= 100
# 0 <= matrix[i].length <= 100

class Solution:
    def spiralOrder(self, matrix: list) -> list:
        res = []
        while len(matrix) > 0:
            if len(matrix) > 0:
                res += matrix.pop(0)
            if len(matrix) > 0:
                for i in range(len(matrix)):
                    if len(matrix[i]) > 0:
                        res += [matrix[i].pop(-1)]
            if len(matrix) > 0:
                res += matrix.pop(-1)[::-1]
            if len(matrix) > 0:
                for i in range(len(matrix)-1, -1, -1):
                    if len(matrix[i]) > 0:
                        res += [matrix[i].pop(0)]
        return res        
    
print(Solution().spiralOrder(matrix = [[1,2,3],
                                       [4,5,6],
                                       [7,8,9]]))

print(Solution().spiralOrder(matrix =[[1, 2, 3, 4],
                                      [5, 6, 7, 8],
                                      [9,10,11,12]]))