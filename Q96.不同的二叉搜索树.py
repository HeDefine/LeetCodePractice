#!/usr/bin/env python3

# https://leetcode-cn.com/problems/unique-binary-search-trees
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


class Solution:
    def numTrees(self, n: int) -> int:
        res = [1, 1]
        for i in range(2, n + 1):
            res.append(0)
            for j in range(1, i + 1):
                res[i] += res[j - 1] * res[i - j]
        return res[n]


print(Solution().numTrees(3))  # 5
