# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。
#
# 例如:
# 给定的树 A:
#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 B：
#    4 
#   /
#  1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
#
# 示例 1：
# 输入：A = [1,2,3], B = [3,1]
# 输出：false
#
# 示例 2：
# 输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true
#
# 限制：
# 0 <= 节点个数 <= 10000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def checkTree(t1:TreeNode, t2:TreeNode):
            if t1 is None and t2 is not None:
                return False
            elif t1 is None and t2 is None:
                return True
            elif t1 is not None and t2 is None:
                return True
            
            if t1.val == t2.val:
                return checkTree(t1.left, t2.left) and checkTree(t1.right, t2.right)
            else:
                return False
        
        if A is None or B is None:
            return False
        else:
            res = False
            if A.val == B.val:
                res = res or checkTree(A, B)
            res = res or self.isSubStructure(A.left, B)
            res = res or self.isSubStructure(A.right, B)
            return res
[4,2,3,4,5,6,7,8,9]
[4,8,9]

t0 = TreeNode(4)        
t1 = TreeNode(2)
t2 = TreeNode(3)
t3 = TreeNode(4)
t4 = TreeNode(5)
t5 = TreeNode(6)
t6 = TreeNode(7)
t7 = TreeNode(8)
t8 = TreeNode(9)

t0.left = t1
t0.right = t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
t3.left = t7
t3.right = t8

p1 = TreeNode(4)
p2 = TreeNode(8)
p3 = TreeNode(9)
p1.left = p2
p1.right = p3
print(Solution().isSubStructure(t0, p1))
        