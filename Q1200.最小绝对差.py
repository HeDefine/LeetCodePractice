# 给你个整数数组 arr，其中每个元素都 不相同。
# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

# 示例 1：
# 输入：arr = [4,2,1,3]
# 输出：[[1,2],[2,3],[3,4]]

# 示例 2：
# 输入：arr = [1,3,6,10,15]
# 输出：[[1,3]]

# 示例 3：
# 输入：arr = [3,8,-10,23,19,-4,-14,27]
# 输出：[[-14,-10],[19,23],[23,27]]

# 提示：
# 2 <= arr.length <= 10^5
# -10^6 <= arr[i] <= 10^6

class Solution:
    def minimumAbsDifference(self, arr: list) -> list:
        minVal = max(arr) - min(arr)
        res = []
        arr = sorted(arr)
        for idx, val in enumerate(sorted(arr)) :
            if idx < len(arr) - 1:
                nextVal = arr[idx + 1]
                temp = nextVal - val
                if minVal == temp:
                    res.append([val, nextVal])
                elif minVal > temp:
                    minVal = temp
                    res.clear()
                    res.append([val, nextVal])
        return res
    
print(Solution().minimumAbsDifference([4,2,1,3]))   # [[1,2],[2,3],[3,4]]
print(Solution().minimumAbsDifference([1,3,6,10,15]))   # [[1,3]]
print(Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))   # [[-14,-10],[19,23],[23,27]]
