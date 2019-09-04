#!/usr/bin/env python3

# https://leetcode-cn.com/problems/find-the-town-judge
# 在一个小镇里，按从 1 到 N 标记了 N 个人。传言称，这些人中有一个是小镇上的秘密法官。
# 如果小镇的法官真的存在，那么：
# 1. 小镇的法官不相信任何人。
# 2. 每个人（除了小镇法官外）都信任小镇的法官。
# 只有一个人同时满足属性 1 和属性 2 。
# 给定数组 trust，该数组由信任对 trust[i] = [a, b] 组成，表示标记为 a 的人信任标记为 b 的人。
# 如果小镇存在秘密法官并且可以确定他的身份，请返回该法官的标记。否则，返回 -1。
#
# 提示：
# 1. 1 <= N <= 1000
# trust.length <= 10000
# trust[i] 是完全不同的
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N


class Solution:
    def findJudge(self, N: int, trust: [[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1
        trustSet = set()
        purposePeople = set()
        trustDic = dict()
        for t in trust:
            trustSet.add(t[0])
            trustDic[t[1]] = trustDic.get(t[1], 0) + 1
            if trustDic[t[1]] == N-1:
                purposePeople.add(t[1])
        res = purposePeople - trustSet
        if len(res) > 0:
            return res.pop()
        else:
            return -1


print(Solution().findJudge(N=2, trust=[[1, 2]]))  # 2
print(Solution().findJudge(N=3, trust=[[1, 3], [2, 3]]))  # 3
print(Solution().findJudge(N=3, trust=[[1, 3], [2, 3], [3, 1]]))  # -1
print(Solution().findJudge(N=3, trust=[[1, 2], [2, 3]]))  # -1
print(Solution().findJudge(N=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))  # 3
