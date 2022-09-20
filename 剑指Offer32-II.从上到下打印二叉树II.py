# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
#  
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
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
        def recursion(node: TreeNode, level):
            if node is not None:
                if level < len(res):
                    res[level] += [node.val]
                else:
                    res.append([node.val])
                
                recursion(node.left, level + 1)
                recursion(node.right, level + 1)
                
        res = list()
        recursion(root, 0)
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