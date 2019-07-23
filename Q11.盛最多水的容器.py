#!/usr/bin/env python3

# https://leetcode-cn.com/problems/container-with-most-water
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
# 示例:
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
#


class Solution:
    # 暴力法
    def maxArea(self, height: [int]) -> int:
        if len(height) < 2:
            return 0
        result = 0
        for i in range(2, len(height)):
            for j in range(i + 1):
                result = max(result, j * min(height[i], height[i - j]))
        return result

    # 双指针
    def maxArea2(self, height: [int]) -> int:
        i = 0
        j = len(height) - 1
        result = 0
        while i < j:
            v1 = height[i]
            v2 = height[j]
            result = max(result, min(v1, v2) * (j - i))

            if v1 > v2:
                j -= 1
            else:
                i += 1
        return result


print(Solution().maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49

# 第一种方法超时。第二种方法是利用双指针法。那为什么双指针不会错过所有值呢?

