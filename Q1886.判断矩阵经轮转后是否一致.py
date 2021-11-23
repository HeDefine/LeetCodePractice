# 给你两个大小为 n x n 的二进制矩阵 mat 和 target 。
# 现 以 90 度顺时针轮转 矩阵 mat 中的元素 若干次 ，
# 如果能够使 mat 与 target 一致，返回 true ；否则，返回 false 。
#  
# 示例 1：
# 输入：mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# 输出：true
# 解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。
#  
# 示例 2：
# 输入：mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# 输出：false
# 解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。
#  
# 示例 3：
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# 输出：true
# 解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。
#  
# 提示：
# n == mat.length == target.length
# n == mat[i].length == target[i].length
# 1 <= n <= 10
# mat[i][j] 和 target[i][j] 不是 0 就是 1

class Solution:
    def findRotation(self, mat: list, target: list) -> bool:
        def rotate(arr) -> list:
            new_arr = list()
            for i in range(0, len(arr[0])):
                t = list()
                for j in range(len(arr)-1,-1,-1):
                    t.append(arr[j][i])
                new_arr.append(t)
            return new_arr
        k = 0
        while k < 4:
            if mat == target:
                return True
            mat = rotate(mat)
            k += 1
        return False
    
print(Solution().findRotation(mat = [[1,2],[3,4]], target = [[3,1],[4,2]]))
print(Solution().findRotation(mat = [[0,1],[1,0]], target = [[1,0],[0,1]])) # True
print(Solution().findRotation(mat = [[0,1],[1,1]], target = [[1,0],[0,1]])) # False
print(Solution().findRotation(mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]])) # True