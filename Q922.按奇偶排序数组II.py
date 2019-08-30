#!/usr/bin/env python3

# https://leetcode-cn.com/problems/sort-array-by-parity-ii
# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
# 你可以返回任何满足上述条件的数组作为答案。
#
# 示例：
# 输入：[4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#
# 提示：
# 1. 2 <= A.length <= 20000
# 2. A.length % 2 == 0
# 3. 0 <= A[i] <= 1000


class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        idx0 = list()  # 不符合的偶数idx
        idx1 = list()  # 不符合的奇数idx
        for idx, val in enumerate(A):
            if idx % 2 == 0 and val % 2 != 0:
                idx0.append(idx)
            if idx % 2 != 0 and val % 2 == 0:
                idx1.append(idx)
            if len(idx0) > 0 and len(idx1) > 0:
                A[idx0[-1]], A[idx1[-1]] = A[idx1[-1]], A[idx0[-1]]
                idx0.pop()
                idx1.pop()
        return A


# print(Solution().sortArrayByParityII([4, 2, 5, 7]))
# print(Solution().sortArrayByParityII([3, 1, 4, 2]))

print(Solution().sortArrayByParityII([4, 2, 5, 7]))
