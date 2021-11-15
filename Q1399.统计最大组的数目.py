# 给你一个整数 n 。请你先求出从 1 到 n 的每个整数 10 进制表示下的数位和（每一位上的数字相加），然后把数位和相等的数字放到同一个组中。
# 请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。
#  
# 示例 1：
# 输入：n = 13
# 输出：4
# 解释：总共有 9 个组，将 1 到 13 按数位求和后这些组分别是：
# [1,10]，[2,11]，[3,12]，[4,13]，[5]，[6]，[7]，[8]，[9]。总共有 4 个组拥有的数字并列最多。
#  
# 示例 2：
# 输入：n = 2
# 输出：2
# 解释：总共有 2 个大小为 1 的组 [1]，[2]。
#  
# 示例 3：
# 输入：n = 15
# 输出：6
#  
# 示例 4：
# 输入：n = 24
# 输出：5
#  
# 提示：
# 1 <= n <= 10^4

class Solution:
    def countLargestGroup(self, n: int) -> int:
        res_dict = dict()
        max_count = 0
        for val in range(1, n+1):
            sum_val = sum([int(i) for i in list(str(val))])
            res_dict[sum_val] = res_dict.get(sum_val, 0) + 1
            max_count = max(max_count, res_dict[sum_val])
        res = 0
        for value in res_dict.values():
            if value == max_count:
                res += 1
        return res

print(Solution().countLargestGroup(13)) # 4
print(Solution().countLargestGroup(2))  # 2
print(Solution().countLargestGroup(15)) # 6
print(Solution().countLargestGroup(24)) # 5
