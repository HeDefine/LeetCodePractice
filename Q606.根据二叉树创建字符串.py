#!/usr/bin/env python3

# https://leetcode-cn.com/problems/construct-string-from-binary-tree
# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
#
# 示例 1:
# 输入: 二叉树: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /
#   4
# 输出: "1(2(4))(3)"
# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。
#
# 示例 2:
# 输入: 二叉树: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \
#       4
# 输出: "1(2()(4))(3)"
# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t is None:
            return ""
        res = str(t.val)
        if t.right is not None:
            res += "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"
        else:
            if t.left is None:
                return res
            res += "(" + self.tree2str(t.left) + ")"
        return res


T1 = TreeNode(1)
T2 = TreeNode(2)
T3 = TreeNode(3)
T4 = TreeNode(4)
T1.left = T2
T1.right = T3
T2.left = T4

print(Solution().tree2str(T1))  # 1(2(4))(3)
