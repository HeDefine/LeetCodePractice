# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7]，
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。
#  
# 提示：
# 节点总数 <= 10000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, level:int):
            if node is None:
                return level
            level += 1
            return max(dfs(node.left, level), dfs(node.right, level))
        return dfs(root, 0)
                
    
t0 = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)
t0.left = t1
t0.right = t2
t2.left = t3
t2.right = t4
print(Solution().maxDepth(t0))