# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#  
# 示例 1:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 示例 2:
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 限制：
# 0 <= 节点个数 <= 5000

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if len(inorder) > 0 and len(preorder) > 0:
            val = preorder.pop(0)
            node = TreeNode(val)
            idx = inorder.index(val)
            node.left = self.buildTree(preorder, inorder[:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])
            return node
        

def Print(pRoot):
        # write code here
        if not pRoot:
            return []
        queue=[pRoot]
        outList=[]
        while queue:
            res=[]
            nextQueue=[]
            for point in queue:     #这里再遍历每一层
                if point:
                    res.append(point.val)
                    nextQueue.append(point.left)
                    nextQueue.append(point.right)
                else:
                    res.append('null')
            outList.append(res)
            queue=nextQueue     #这一步很巧妙，用当前层覆盖上一层
        return outList    
t = Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
# t = Solution().buildTree(preorder = list('DBEFAGHCI'), inorder = list("ABDFECGHI"))
print(Print(t))