#!/usr/bin/env python3

# https://leetcode-cn.com/problems/relative-sort-array
# 给你两个数组，arr1 和 arr2，
#
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
#
# 示例：
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#
# 提示：
# arr1.length, arr2.length <= 1000
# 0 <= arr1[i], arr2[i] <= 1000
# arr2 中的元素 arr2[i] 各不相同
# arr2 中的每个元素 arr2[i] 都出现在 arr1 中


class Solution:
    def relativeSortArray(self, arr1: [int], arr2: [int]) -> [int]:
        arr1Dic = dict()
        for n in arr1:
            arr1Dic[n] = arr1Dic.get(n, 0) + 1
        res = []
        for n in arr2:
            if arr1Dic.get(n) is not None:
                res += [n] * arr1Dic[n]
                del arr1Dic[n]
        for key, val in sorted(arr1Dic.items(), key=lambda x: x[0]):
            res += [key] * val
        return res


# print(Solution().relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
#                                    arr2=[2, 1, 4, 3, 9, 6]))  # [2,2,2,1,4,3,3,9,6,7,19]
print(Solution().relativeSortArray([28, 6, 22, 8, 44, 17]
                                   , [22, 28, 8, 6]))
