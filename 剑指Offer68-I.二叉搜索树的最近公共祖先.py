# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：
# “对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
#  
# 示例 1:
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
#
# 示例 2:
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
#  
# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
    
# 6,2,8,0,4,7,9,null,null,3,5
t0 = TreeNode(6)
t1 = TreeNode(2)
t2 = TreeNode(8)
t3 = TreeNode(0)
t4 = TreeNode(4)
t5 = TreeNode(7)
t6 = TreeNode(9)
t7 = TreeNode(3)
t8 = TreeNode(5)

t0.left = t1
t0.right = t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
t4.left = t7
t4.right = t8

res0 = Solution().lowestCommonAncestor(t0, t1, t2)
print(res0.val)     # 6
res1 = Solution().lowestCommonAncestor(t0, t1, t4)
print(res1.val)     # 2
