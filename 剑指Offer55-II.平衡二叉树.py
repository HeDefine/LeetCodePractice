# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
#  
# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。
#  
# 示例 2:
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。
#  
# 限制：
# 0 <= 树的结点个数 <= 10000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode, level:int):
            nonlocal res
            if node is None:
                return level
            level += 1
            left_level = dfs(node.left, level)
            right_level = dfs(node.right, level)
            if abs(left_level - right_level) > 1:
                res = False
            return max(left_level, right_level)
        
        res = True
        dfs(root, 0)
        return res
        
