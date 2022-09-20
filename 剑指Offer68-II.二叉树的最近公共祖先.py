# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：
# “对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#  
# 示例 1:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
# 示例 2:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def recursion(node: TreeNode):
            nonlocal res
            if node is not None:
                left_node = recursion(node.left)
                right_node = recursion(node.right)
                if left_node == p and right_node == q:
                    res = node
                elif left_node == q and right_node == p:
                    res = node
                elif node == p and (left_node == q or right_node == q):
                    res = node
                elif node == q and (left_node == p or right_node == p):
                    res = node
                if node == p or node == q:
                    return node
                elif left_node is not None:
                    return left_node
                elif right_node is not None:
                    return right_node
                
                
        res = None
        recursion(root)
        return res


    
t0 = TreeNode(3)
t1 = TreeNode(5)
t2 = TreeNode(1)
t3 = TreeNode(6)
t4 = TreeNode(2)
t5 = TreeNode(0)
t6 = TreeNode(8)
t7 = TreeNode(7)
t8 = TreeNode(4)

t0.left = t1
t0.right = t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
t4.left = t7
t4.right = t8

r1 = Solution().lowestCommonAncestor(t0, t1, t2)
print(r1.val)   # 3
r2 =  Solution().lowestCommonAncestor(t0, t1, t8)
print(r2.val)   # 5
