# 环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。
# 我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。
# 环线上的公交车都可以按顺时针和逆时针的方向行驶。
# 返回乘客从出发点 start 到目的地 destination 之间的最短距离。

# 提示：
# 1 <= n <= 10^4
# distance.length == n
# 0 <= start, destination < n
# 0 <= distance[i] <= 10^4

class Solution:
    def distanceBetweenBusStops(self, distance: list, start: int, destination: int) -> int:
        sumV = 0
        aheadV = 0
        if start > destination:
            start, destination = destination, start
        for idx, val in enumerate(distance):
            if start <= idx < destination:
                aheadV += distance[idx]
            sumV += distance[idx]
        return min(aheadV, sumV - aheadV)
        
    
# print(Solution().distanceBetweenBusStops([1,2,3,4], 0, 1))  # 1
# print(Solution().distanceBetweenBusStops([1,2,3,4], 0, 2))  # 3
# print(Solution().distanceBetweenBusStops([1,2,3,4], 0, 3))  # 4

print(Solution().distanceBetweenBusStops([7,10,1,12,11,14,5,0],7,2 ))   # 17