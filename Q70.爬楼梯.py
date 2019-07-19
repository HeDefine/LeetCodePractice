#!/usr/bin/env python3

# https://leetcode-cn.com/problems/climbing-stairs
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。
#
# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        temp = list()
        for i in range(1, n + 1):
            if i == 1:
                temp.append(1)
            elif i == 2:
                temp.append(2)
            else:
                temp.append(temp[i - 3] + temp[i - 2])
        return temp[-1]


# print(Solution().climbStairs(2))  # 2
print(Solution().climbStairs(3))  # 3
# print(Solution().climbStairs(35))

# 草稿:
# 1 阶    1 种 (1)
# 2 阶    2 种 (1,1)  (2)
# 3 阶    3 种 (1,1,1)  (2,1) (1,2)
# 4 阶    5 种 (1,1,1,1) (2,1,1) (1,2,1) (1,1,2) (2,2)
# 5 阶    8 种 (1,1,1,1,1) (2,1,1,1) (1,2,1,1) (1,1,2,1) (1,1,1,2)
#             (2,2,1) (2,1,2) (1,2,2)
# 6 阶    13 种 (1,1,1,1,1,1) (2,1,1,1,1) (1,2,1,1,1) (1,1,2,1,1)
#             (1,1,1,2,1) (1,1,1,1,2) (2,2,1,1) (2,1,2,1) (2,1,1,2)
#             (1,2,2,1) (1,2,1,2) (1,1,2,2) (2,2,2)

# 规律就是菲波那切数列
