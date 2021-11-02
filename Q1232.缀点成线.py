#在一个 XY 坐标系中有一些点，我们用数组 coordinates 来分别记录它们的坐标，其中 coordinates[i] = [x, y] 表示横坐标为 x、纵坐标为 y 的点。
#请你来判断，这些点是否在该坐标系中属于同一条直线上，是则返回 true，否则请返回 false。
#
# 示例 1：
# 输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# 输出：true
#
# 示例 2：
# 输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# 输出：false
#  
# 提示：
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates 中不含重复的点

class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
        # y = kx + b
        k = 0
        if coordinates[0][0] != coordinates[1][0]:
            k = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])   # 斜率(y2 - y1)/(x2- x1)
        b = coordinates[0][1] - k * coordinates[0][0]
        print('y =', k , '* x +', b)
        for pos in coordinates:
            x, y = pos[0], pos[1]
            if k == 0:
                if coordinates[0][0] == coordinates[1][0] and x != coordinates[0][0]:
                    return False
                elif coordinates[0][1] == coordinates[1][1] and y != coordinates[0][1]:
                    return False
            else:
                if y != k * x + b :
                    return False
        return True
    
# print(Solution().checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))  # true
# print(Solution().checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))  # false
print(Solution().checkStraightLine([[0,0],[0,1],[0,-1]]))   # true
