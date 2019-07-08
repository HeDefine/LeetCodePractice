#!/user/bin/env python3
import time


# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution:
    # 方法一
    # 暴力法, 其实是循环里面又套了个循环。时间复杂度 O(n^2), 空间复杂度 O(1)
    @staticmethod
    def function1(nums: [int], target: int) -> [int]:
        result = set()
        for num in nums:
            if (target - num) in nums:
                index1 = nums.index(num)
                index2 = [i for (i, x) in enumerate(nums) if x == (target - num) and i != index1]
                if len(index2) > 0:
                    result.add(index1)
                    result.add(index2[0])
        return list(result)

    # 方法二
    # 两遍循环, 第一遍循环先将值赋值给字典。再循环查值。 时间复杂度 O(n), 空间复杂度 O(n)
    @staticmethod
    def function2(nums: [int], target: int) -> [int]:
        _dict = {}
        for i, v in enumerate(nums):
            _dict[v] = i
        for i, v in enumerate(nums):
            j = _dict.get(target - v)
            if j is not None and j != i:
                return [i, j]

    # 方法三
    # 一遍循环, 和上面差不多。 不过不需要再判断是否重复了, 有点二分法的意思
    @staticmethod
    def function3(nums: [int], target: int) -> [int]:
        _dict = {}
        for i, m in enumerate(nums):
            if _dict.get(target - m) is not None:
                return [i, _dict.get(target - m)]
            _dict[m] = i


inputNums = [3, 2, 4, 0, 7, 11, 15, 0]
inputTarget = 0
print("输入: nums = ", inputNums, "target = ", inputTarget)

# 调用方法1
startTime = time.time_ns()
result1 = Solution.function1(nums=inputNums, target=inputTarget)
endTime = time.time_ns()
print("方法1:", result1, "\t耗时:", (endTime - startTime) / 1000, "ms")

# 调用方法2
startTime = time.time_ns()
result2 = Solution.function2(nums=inputNums, target=inputTarget)
endTime = time.time_ns()
print("方法1:", result2, "\t耗时:", (endTime - startTime) / 1000, "ms")

# 调用方法3
startTime = time.time_ns()
result3 = Solution.function3(nums=inputNums, target=inputTarget)
endTime = time.time_ns()
print("方法1:", result3, "\t耗时:", (endTime - startTime) / 1000, "ms")

'''
后记: 这道题里面, 暴力法比较容易想到. 因为用到了两次循环。所以时间复杂度是O(n^2)

后两种方法其实可以看做一种, 就是利用了 字典dict。   将空间转为时间

1. 这里可以学到 如果需要追求响应时间 而不考虑占用内存空间 的话，我们可以用字典来解决。
2. 数组的indexof等获取下标的方法，其实它的时间复杂度也是 O(n)
3. 二分法的思想

'''
