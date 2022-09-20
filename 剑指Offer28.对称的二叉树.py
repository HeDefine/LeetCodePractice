# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 示例 1：
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
# 示例 2：
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recursion(t: TreeNode, level):
            if t is not None:
                if len(res) <= level:
                    res.append([t.val])
                else:
                    res[level].append(t.val)
                recursion(t.left, level+1)
                recursion(t.right, level+1)
            else:
                if len(res) <= level:
                    res.append([''])
                else:
                    res[level].append('')
        
        res = list()
        recursion(root, 0)
        res.pop(0)
        
        for line in res:
            if len(line) % 2 == 0:
                val1 = line[:len(line)//2]
                val2 = line[:len(line)//2-1:-1]
                print(val1, val2, val1==val2)
                if line[:len(line)//2] != line[:len(line)//2-1:-1]:
                    return False
            else:
                print(line)
                return False
        return True

t = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(4)
t6 = TreeNode(3)
t7 = TreeNode(7)

t.left = t1
t.right =t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
# t3.left = t7
print(Solution().isSymmetric(t))