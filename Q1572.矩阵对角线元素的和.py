# 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

class Solution:
    def diagonalSum(self, mat: list) -> int:
        res = 0
        for i in range(len(mat)):
            if i == len(mat) - i - 1:
                res += mat[i][i]
            else:
                res += mat[i][i] + mat[i][len(mat) - i - 1]
        return res

print(Solution().diagonalSum(mat = [[1,2,3],[4,5,6],[7,8,9]]))