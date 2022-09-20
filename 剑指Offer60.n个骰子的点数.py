# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
#  
# 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
#  
# 示例 1:
# 输入: 1
# 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
#  
# 示例 2:
# 输入: 2
# 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
#  
# 限制：
# 1 <= n <= 11

class Solution:
    def dicesProbability(self, n: int) -> list:
        res = [1]
        for count in range(1, n + 1):
            temp = list()
            for sum in range(count * 6 + 1):
                percent = 0
                for num in range(1, 7):
                    if 0 <= sum - num < len(res):
                        percent += 1/6 * res[sum-num]
                temp.append(percent) 
            res = temp
        return res[count:]
        
print(Solution().dicesProbability(1))
print(Solution().dicesProbability(2))
print(Solution().dicesProbability(3))