# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
#  
# 参考以下这颗二叉搜索树：
#      5
#     / \
#    2   6
#   / \
#  1   3
#
# 示例 1：
# 输入: [1,6,3,2,5]
# 输出: false
#  
# 示例 2：
# 输入: [1,3,2,6,5]
# 输出: true
#  
# 提示：
# 数组长度 <= 1000

class Solution:
    def verifyPostorder(self, postorder: list) -> bool:
        if len(postorder) <= 1:
            return True
        root_val = postorder.pop()
        left_idx, right_idx = None, None
        for idx in range(len(postorder) - 1, -1, -1):
            if postorder[idx] < root_val and left_idx is None:
                left_idx = idx
            if postorder[idx] > root_val:
                right_idx = idx
        print(postorder, root_val, left_idx, right_idx)
        if left_idx is not None and right_idx is not None and right_idx < left_idx:
            return False
        else:
            is_correct_tree = True
            if left_idx is not None:
                is_correct_tree = is_correct_tree and self.verifyPostorder(postorder[:left_idx+1])
            if right_idx is not None:
                is_correct_tree = is_correct_tree and self.verifyPostorder(postorder[right_idx:len(postorder)])
            return is_correct_tree

# print(Solution().verifyPostorder([1,6,3,2,5]))
# print(Solution().verifyPostorder([1,3,2,6,5]))
# print(Solution().verifyPostorder([7, 4, 6, 5]))
print(Solution().verifyPostorder([3,10,6,9,2]))