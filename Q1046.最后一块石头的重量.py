#!/usr/bin/env python3

# https://leetcode-cn.com/problems/last-stone-weight
# 有一堆石头，每块石头的重量都是正整数。
# 每一回合，从中选出两块最重的石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
#
# 如果 x == y，那么两块石头都会被完全粉碎；
# 如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
# 最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。
#
# 提示：
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000


class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        def addNewStone(l: [int], target: int) -> [int]:
            low = 0
            high = len(l) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if low == high:
                    if l[mid] > target:
                        return l[:mid] + [target] + l[mid:]
                    else:
                        return l[:mid + 1] + [target] + l[mid + 1:]
                elif l[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return l[:low] + [target] + l[low:]

        stones.sort()
        while len(stones) > 1:
            maxStone = stones.pop(-1)
            maxStone_1 = stones.pop(-1)
            if maxStone != maxStone_1:
                stones = addNewStone(stones, abs(maxStone - maxStone_1))
        return 0 if len(stones) == 0 else stones[0]


# print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))  # 1
print(Solution().lastStoneWeight([9, 3, 2, 10]))
