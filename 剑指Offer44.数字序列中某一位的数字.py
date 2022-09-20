# 数字以0123456789101112131415…的格式序列化到一个字符序列中。
# 在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
# 请写一个函数，求任意第n位对应的数字。
#  
# 示例 1：
# 输入：n = 3
# 输出：3
#  
# 示例 2：
# 输入：n = 11
# 输出：0
#  
# 限制：
# 0 <= n < 2^31

class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        res = 1
        while n > res + (10 ** i - 10 ** (i-1)) * i:
            res += (10 ** i - 10 ** (i-1)) * i
            i += 1
        num = 10 ** (i-1) + (n - res) // i
        return int(str(num)[(n - res) % i])

print(Solution().findNthDigit(3))   # 3
print(Solution().findNthDigit(11))  # 0
print(Solution().findNthDigit(1000))  # 3

# print(Solution().findNthDigit(2**31))
q = 370
s = ''
for i in range(q):
    s = s + str(i)
print(s)
print(len(s))