#!/usr/bin/env python3

# https://leetcode-cn.com/problems/word-search
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.


class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        def isExist(enterX, enterY, idx: int, path: set) -> bool:
            # print(path)
            if idx >= len(word):
                return True
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in direction:
                s = str(enterX + d[0]) + "_" + str(enterY + d[1])
                if 0 <= enterX + d[0] < len(board) and 0 <= enterY + d[1] < len(board[enterX + d[0]]):
                    if board[enterX + d[0]][enterY + d[1]] == word[idx] and s not in path:
                        path.add(s)
                        if isExist(enterX + d[0], enterY + d[1], idx + 1, path):
                            return True
                        path.remove(s)
            return False

        for x, line in enumerate(board):
            for y, val in enumerate(line):
                if len(word) > 0 and val == word[0]:
                    set0 = set("")
                    set0.add(str(x) + '_' + str(y))
                    if isExist(x, y, 1, set0):
                        return True
        return False


t = [['A', 'B', 'C', 'E'],
     ['S', 'F', 'C', 'S'],
     ['A', 'D', 'E', 'E']]

print(Solution().exist(t, "ABCCED"))
print(Solution().exist(t, "SEE"))
print(Solution().exist(t, "ABCB"))
#
print(Solution().exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))
print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
