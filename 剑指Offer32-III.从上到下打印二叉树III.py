# 请实现一个函数按照之字形顺序打印二叉树，
# 即第一行按照从左到右的顺序打印，
# 第二层按照从右到左的顺序打印，
# 第三行再按照从左到右的顺序打印，
# 其他行以此类推。
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
#   [20,9],
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
        return [ i if idx % 2 == 0 else i[::-1] for idx, i in enumerate(res)]
    
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