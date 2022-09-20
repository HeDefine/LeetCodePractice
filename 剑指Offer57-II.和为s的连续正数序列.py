# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#  
# 示例 1：
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 
# 示例 2：
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]

class Solution:
    def findContinuousSequence(self, target: int) :
        def dfs(start_idx, res_val, cur_list):
            if res_val < 0:
                return
            elif res_val == 0:
                res.append(cur_list)
                return
            dfs(start_idx+1, res_val - start_idx, cur_list+[start_idx])
                    
        res = list()
        for i in range(1, target):
            if i < target - i:
                dfs(i + 1, target - i, [i])
        return res

print(Solution().findContinuousSequence(9)) # [[2,3,4],[4,5]]
print(Solution().findContinuousSequence(15))    # [[1,2,3,4,5],[4,5,6],[7,8]]