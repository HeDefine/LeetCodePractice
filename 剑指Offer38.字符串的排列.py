# 输入一个字符串，打印出该字符串中字符的所有排列。
#  
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#  
# 示例:
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
# 
# 限制：
# 1 <= s 的长度 <= 8

class Solution:
    def permutation(self, s: str):
        def recursion(cur_str, res_str):
            if len(res_str) > 0:
                for idx, ch in enumerate(res_str) :
                    recursion(cur_str + ch, res_str[:idx] + res_str[idx+1:])
            else:
                res.add(cur_str)
        
        res = set()
        recursion('', s)
        return res

print(Solution().permutation('abc'))