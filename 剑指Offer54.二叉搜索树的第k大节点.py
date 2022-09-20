# 给定一棵二叉搜索树，请找出其中第k大的节点。
#  
# 示例 1:
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
#  
# 示例 2:
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4
#  
# 限制：
# 1 ≤ k ≤ 二叉搜索树元素个数

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def kthLargest(self, root: TreeNode, k: int) -> int:
        def recursion(node:TreeNode):
            nonlocal cur_length, res
            if node is None or cur_length > k:
                return
            recursion(node.right)
            cur_length += 1
            if cur_length == k:
                res = node.val
            recursion(node.left)

        res, cur_length = 0, 0
        recursion(root)
        return res



t0 = TreeNode(3)
t1 = TreeNode(1)
t2 = TreeNode(4)
t3 = TreeNode(2)
t0.left = t1
t0.right = t2
t1.right = t3
print(Solution().kthLargest(t0, 1)) # 4

n0 = TreeNode(5)
n1 = TreeNode(3)
n2 = TreeNode(6)
n3 = TreeNode(2)
n4 = TreeNode(4)
n5 = TreeNode(1)
n0.left = n1
n0.right = n2
n1.left = n3
n1.right = n4
n3.left = n5
print(Solution().kthLargest(n0, 3)) # 4