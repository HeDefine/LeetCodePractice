#!/usr/bin/env python3

# https://leetcode-cn.com/problems/plus-one
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。


class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        digits.reverse()
        for idx, v in enumerate(digits):
            print(v)
            digits[idx] = v + 1
            if v + 1 == 10:
                digits[idx] = 0
                if idx == len(digits) - 1:
                    digits.append(1)
                    break
                continue
            else:
                break
        digits.reverse()
        return digits


# print(Solution().plusOne([1, 2, 3]))  # [1,2,4]
# print(Solution().plusOne([4, 3, 2, 1]))  # [4,3,2,1]
print(Solution().plusOne([9, 9, 9, 9]))  # [4,3,2,1]
