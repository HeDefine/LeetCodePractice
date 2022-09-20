# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
# 叶子节点 是指没有子节点的节点。
#  
# 示例 1：
#          5
#         / \
#        4   8
#       /   / \
#      11  13  4
#     / \     / \
#    7   2   5   1
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#  
# 示例 2：
#          1
#         / \
#        2   3
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#  
# 示例 3：
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#  
# 提示：
# 树中节点总数在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int):
        def recursion(node: TreeNode, sum_val:int, cur_list:list):
            if node is not None :
                if sum_val - node.val == 0 and node.left is None and node.right is None:
                    res.append(cur_list + [node.val])
                else:
                    recursion(node.left, sum_val - node.val, cur_list + [node.val])
                    recursion(node.right, sum_val - node.val, cur_list + [node.val])
        
        res = list()
        recursion(root, target, [])
        return res

t = TreeNode(5)
t1 = TreeNode(4)
t2 = TreeNode(8)
t3 = TreeNode(11)
t4 = TreeNode(13)
t5 = TreeNode(4)
t6 = TreeNode(7)
t7 = TreeNode(2)
t8 = TreeNode(5)
t9 = TreeNode(1)

t.left = t1
t.right = t2
t1.left = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
t5.left = t8
t5.right = t9
# print(Solution().pathSum(t, 22))

q = TreeNode(-2)
q1 = TreeNode(-3)
q.right = q1
print(Solution().pathSum(q, -5))