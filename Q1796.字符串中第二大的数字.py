# 给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
# 混合字符串 由小写英文字母和数字组成。
#  
# 示例 1：
# 输入：s = "dfa12321afd"
# 输出：2
# 解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
#  
# 示例 2：
# 输入：s = "abc1111"
# 输出：-1
# 解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
#  
# 提示：
# 1 <= s.length <= 500
# s 只包含小写英文字母和（或）数字。

class Solution:
    def secondHighest(self, s: str) -> int:
        max_val = -1
        next_max_val = -1
        for ch in s:
            if '0' <= ch <= '9':
                val = int(ch)
                if val > max_val:
                    max_val, next_max_val = val, max_val
                elif val == max_val:
                    continue
                elif val > next_max_val:
                    next_max_val = val
        return next_max_val

print(Solution().secondHighest(s = "dfa12321afd"))  # 2
print(Solution().secondHighest(s = "abc1111"))  # -1