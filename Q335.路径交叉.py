#!/usr/bin/env python3

# 给你一个整数数组 distance 。
# 
# 从 X-Y 平面上的点 (0,0) 开始，
# 先向北移动 distance[0] 米，
# 然后向西移动 distance[1] 米，
# 向南移动 distance[2] 米，
# 向东移动 distance[3] 米，持续移动。
# 也就是说，每次移动后你的方位会发生逆时针变化。
#
# 判断你所经过的路径是否相交。如果相交，返回 true ；否则，返回 false 。
class Solution:
    def isSelfCrossing(self, distance) -> bool:
        if len(distance) < 4: 
            return False
        i = 2;
        #从内往外的圈
        while i < len(distance) and distance[i] > distance[i-2]:
            i += 1
        if i == len(distance):
            return False
        # 内卷
        if i == 3 and distance[i] >= distance[i-2]:
            distance[i-1] = distance[i-1] - distance[i-3]
        
        if i >= 4 and distance[i] >= distance[i-2] - distance[i-4]:
            distance[i-1] = distance[i-1] - distance[i-3]

        i += 1
        while i < len(distance) and distance[i] < distance[i-2]:
            i += 1
        if i == len(distance):
            return False
        
        return True
            
                
            
    
    
# print(Solution().isSelfCrossing([2,1,1,2]))     # True
# print(Solution().isSelfCrossing([1,2,3,4]))     # False
# print(Solution().isSelfCrossing([1,1,1,1]))     # True
# print(Solution().isSelfCrossing([4,3,2,1]))     # False
# print(Solution().isSelfCrossing([3,3,4,2,2]))     # False
# print(Solution().isSelfCrossing([1,1,2,2,1,1]))      # True
print(Solution().isSelfCrossing([3,3,3,2,1,1]))     # False