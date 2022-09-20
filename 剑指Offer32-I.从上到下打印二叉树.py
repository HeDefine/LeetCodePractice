# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
#  
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回：
# [3,9,20,15,7]
#  
# 提示：
# 节点总数 <= 1000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        
        def recursion(node: TreeNode):
            list = []
            if node is not None:
                list = [node.val] + recursion(node.left) + recursion(node.right)
            return list
        res = recursion(root)
        return res
        

t = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t3 = TreeNode(15)
t4 = TreeNode(7)
 
t.left = t1
t.right = t2
t2.left = t3
t2.right = t4
print(Solution().levelOrder(t))
        