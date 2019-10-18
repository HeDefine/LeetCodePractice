#!/usr/bin/env python3

# https://leetcode-cn.com/problems/merge-intervals
# 给出一个区间的集合，请合并所有重叠的区间。
#
# 示例 1:
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 示例 2:
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        idx = 0
        intervals.sort()
        while idx < len(intervals) - 1:
            curI = intervals[idx]
            nextI = intervals[idx + 1]
            if curI[0] <= nextI[0] <= curI[1] or curI[0] <= nextI[1] <= curI[1] or nextI[0] <= curI[0] <= nextI[1] or \
                    nextI[0] <= curI[1] <= nextI[1]:
                intervals.pop(idx)
                intervals[idx] = [min(curI[0], nextI[0]), max(curI[1], nextI[1])]
                idx -= 1 if idx > 0 else 0
            else:
                idx += 1
        return intervals


# print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
# print(Solution().merge([[1, 4], [4, 5]]))  # [[1,5]]
# print(Solution().merge([[1, 4], [0, 4]]))
# print(Solution().merge([[1, 4], [0, 5]]))
# print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
print(Solution().merge([[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]))
