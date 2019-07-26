#!/usr/bin/env python3

# https://leetcode-cn.com/problems/factorial-trailing-zeroes
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
# 示例 1:
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
# 示例 2:
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
#
# 说明: 你算法的时间复杂度应为 O(log n) 。


class Solution:
    # 方法1
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 1:
            if n % 5 == 0:
                temp = n
                while temp % 5 == 0 and temp != 0:
                    count += 1
                    temp = temp // 5
            n -= 1
        return count

    # 方法2
    def trailingZeroes2(self, n: int) -> int:
        count = 0
        i = 5 * 1
        while i <= n:
            count += n // i
            i = i * 5
        return count


print(Solution().trailingZeroes2(0))  # 0
print(Solution().trailingZeroes2(3))  # 0
print(Solution().trailingZeroes2(5))  # 1
print(Solution().trailingZeroes2(126))  # 1
print(Solution().trailingZeroes2(1808548329))  # 1

# 题解: "尾数的零的数量":
#       "尾数" = 不考虑 中间可能为0的情况
#       "零"   = 尾数为0, 那么只和 5 + 偶数 有关   再仔细想想, 1个5 * 1个2  =  10   即  一个5 + 一个2  组成一个0
#               即 那么每个阶乘里的每个数的因子中  min(5的个数, 2的个数) 就是 0的个数
#               2的个数 肯定比 5 多 。 这个毋庸置疑， 所以只要求 所有数里面有多少个5即可
#
#
#
#       到上面这一步为止，我们想到了方法一，在前面示例都成功的情况下，提交后显示 超时了，因为有一个相当大的数字
#       显然，上面这题的时间复杂度很高 O(n * (n/5))
#       我们需要找规律
#       阶乘范围    零的个数
#       0!...4!      0          5 * 0
#       5!...9!      1          5 * 1
#      10!...14!     2          5 * 2
#      15!...19!     3          5 * 3
#      20!...24!     4          5 * 4
#      25!...29!     6          5 * 5 +  25 * 1
#         ...
#     125!...129!    31         125 / 5 + 125 / 25 + 125 / 125
#       这里的规律就是最近的那个可以被5整除的数可以求出多少个 5的个数，25的个数，125的个数
#    从而，我们可以得出方法2
