# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。
# 求按从小到大的顺序的第 n 个丑数。
#  
# 示例:
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  
# 1 是丑数。
# n 不超过1690。

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        cur_idx_list = [0, 0, 0]
        for _ in range(1,n):
            val_1 = res[cur_idx_list[0]] * 2
            val_2 = res[cur_idx_list[1]] * 3
            val_3 = res[cur_idx_list[2]] * 5
            min_val = min(val_1, val_2, val_3)
            if val_1 == min_val:
                cur_idx_list[0] += 1
            if val_2 == min_val:
                 cur_idx_list[1] += 1
            if val_3 == min_val:
                 cur_idx_list[2] += 1
            res.append(min_val)
        return res[-1]
        
    
print(Solution().nthUglyNumber(10)) # 12