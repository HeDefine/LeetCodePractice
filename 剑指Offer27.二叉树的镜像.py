# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#
# 例如输入：
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# 镜像输出：
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#  
# 示例 1：
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
#  
# 限制：
# 0 <= 节点个数 <= 1000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
    
    
    
t0 = TreeNode(4)
t1_1 = TreeNode(2)
t1_2 = TreeNode(7)
t1_1_1 = TreeNode(1)
t1_1_2 = TreeNode(3)
t1_2_1 = TreeNode(6)
t1_2_2 = TreeNode(9)

t0.left = t1_1
t0.right = t1_2
t1_1.left = t1_1_1
t1_1.right = t1_1_2
t1_2.left = t1_2_1
t1_2.right = t1_2_2

def PrintFromTopToBottom(root):
        # write code here
        outList=[]
        queue=[root]
        while queue!=[] and root:
            outList.append(queue[0].val)
            if queue[0].left!=None:
                queue.append(queue[0].left)
            if queue[0].right!=None:
                queue.append(queue[0].right)
            queue.pop(0)
        return outList

print(PrintFromTopToBottom(t0))
res = Solution().mirrorTree(t0)
print(PrintFromTopToBottom(res))


